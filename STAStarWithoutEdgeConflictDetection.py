import copy
from math import sqrt
from UDGG import *
import heapq
def STAstar(fromCoords,toCoords,graph,reservationTable):
    #https://mat.uab.cat/~alseda/MasterOpt/AStar-Algorithm.pdf
    startVertex = (graph[0][fromCoords])
    #print(graph.keys())
    targetVertex = (graph[0][toCoords]) #time does not really matter here since this returns a vertex object
    heuristicDict = dict()
    
    heuristicDict[targetVertex] = 0
    
    def calculateStraightLineDistance(vertex):
        d1 = sqrt(pow(targetVertex.coord[0]-vertex.coord[0],2))
        d2 = sqrt(pow(targetVertex.coord[1]-vertex.coord[1],2))
        if(d1 < 0):
            d1 = d1*-1
        if(d2 < 0):
            d2 = d2*-1
        distance = d1 + d2
        return distance

    def calculateHeuristicDistance(vertex):
        if vertex not in heuristicDict.keys():
            path = findPathTo(targetVertex, vertex, True)
            for pathVertex in path:
                heuristicDict[pathVertex[0]] = pathVertex[1]
                #print(pathVertex[0].coord, pathVertex[1])
            heuristicDict[vertex] = len(path)
            return heuristicDict[vertex]
        else:
            return heuristicDict[vertex]

    def expandVertex(vertex,costToReach,path, open, closed, frontierQueue, heuristicBool):
        if(heuristicBool == False):
            #print(vertex.coord, costToReach)
            closed[vertex,costToReach] = costToReach
            del open[vertex,costToReach]
        else:
            closed[vertex] = costToReach
            del open[vertex]
        
        neighbours = vertex.neighbours
        shallowPath = copy.copy(path)
        shallowPath.append((vertex,costToReach))
        spawnWaitTimeline = False
        for targetingVertex in neighbours:
            #if heuristicBool == False:
                #print("-----", targetingVertex.coord, costToReach+1)
                #print(reservationTable[1,1,2])
            if(heuristicBool == True):
                distanceToGoal = calculateStraightLineDistance(targetingVertex) 
            else:
                distanceToGoal = calculateHeuristicDistance(targetingVertex) 
            
            timeCost = costToReach+1
            
            if(heuristicBool == False):
                if (targetingVertex,timeCost) in open.keys():
                    if open[targetingVertex,timeCost] <= timeCost:
                        continue
                elif (targetingVertex,timeCost) in closed.keys():
                    if closed[targetingVertex,timeCost] <= timeCost:
                        continue
                    del closed[targetingVertex,timeCost]
                    if reservationTable[targetingVertex.coord[0],targetingVertex.coord[1],timeCost] == False:
                        #print("----------------", targetingVertex.coord, costToReach+1)
                        open[targetingVertex,timeCost] = timeCost
                        heapq.heappush(frontierQueue,((distanceToGoal+timeCost),timeCost,targetingVertex,shallowPath))
                    if reservationTable[vertex.coord[0],vertex.coord[1],timeCost] == False:
                        spawnWaitTimeline = True
                else:
                    
                    if reservationTable[targetingVertex.coord[0],targetingVertex.coord[1],timeCost] == False:
                        #print("----------------", targetingVertex.coord, costToReach+1)
                        open[targetingVertex,timeCost] = timeCost
                        heapq.heappush(frontierQueue,((distanceToGoal+timeCost),timeCost,targetingVertex,shallowPath))
                    if reservationTable[vertex.coord[0],vertex.coord[1],timeCost] == False:
                        spawnWaitTimeline = True
            else:
                if (targetingVertex) in open.keys():
                    if open[targetingVertex] <= timeCost:
                        continue
                elif (targetingVertex) in closed.keys():
                    if closed[targetingVertex] <= timeCost:
                        continue
                    del closed[targetingVertex]
                    open[targetingVertex] = timeCost
                    heapq.heappush(frontierQueue,((distanceToGoal+timeCost),timeCost,targetingVertex,shallowPath))
                else:
                    open[targetingVertex] = timeCost
                    heapq.heappush(frontierQueue,((distanceToGoal+timeCost),timeCost,targetingVertex,shallowPath))
            
                    
                    
        if spawnWaitTimeline == True and (vertex,costToReach+1) not in open.keys():
            timeCost = costToReach+1
            open[vertex,timeCost] = timeCost 
            if(heuristicBool == True):
                distanceToGoal = calculateStraightLineDistance(vertex) 
            else:
                distanceToGoal = calculateHeuristicDistance(vertex) 
            heapq.heappush(frontierQueue,((distanceToGoal+timeCost),timeCost,vertex,shallowPath))
            
            
        

    def findPathTo(startVertex,targetVertex, heuristicBool):
        #print(startVertex.coord, targetVertex.coord, heuristicBool)
        #start of program
        frontierQueue = []
        open = dict()
        closed = dict()
        distanceToGoal = calculateHeuristicDistance(startVertex)
        if(heuristicBool == False):
            open[startVertex, 0] = 0
        else:
            open[startVertex] = 0
        heapq.heappush(frontierQueue,(distanceToGoal,0,startVertex,[]))
        while len(frontierQueue) != 0:
            currentVertex = heapq.heappop(frontierQueue)
            if(currentVertex[2] == targetVertex):
                #print("found path!")
                pathTaken = currentVertex[3]
                pathTaken.append((currentVertex[2],currentVertex[1]))
                #if heuristicBool == False:
                    #print((currentVertex[2].coord,currentVertex[1]))
                return pathTaken
            if heuristicBool == True:
                expandVertex(currentVertex[2],currentVertex[1],currentVertex[3], open, closed, frontierQueue, True)
            else:
                expandVertex(currentVertex[2],currentVertex[1],currentVertex[3], open, closed, frontierQueue, False)
    #print(" ")
    path = findPathTo(startVertex,targetVertex, False)
    if(path != None):
        return path
    else:
        return []


