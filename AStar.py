import copy
from math import sqrt
from UDGG import *
import heapq
def Astar(fromCoords,toCoords,graph):
    #https://mat.uab.cat/~alseda/MasterOpt/AStar-Algorithm.pdf
    if fromCoords in graph[0].keys():
        startVertex = (graph[0][fromCoords])
    else:
        return None
    #print(graph.keys())
    if toCoords in graph[0].keys():
        targetVertex = (graph[0][toCoords]) #time does not really matter here since this returns a vertex object
    else:
        return None
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

    def expandVertex(vertex,costToReach,path, open, closed, frontierQueue):
        
        closed[vertex] = costToReach
        del open[vertex]
        
        neighbours = vertex.neighbours
        shallowPath = copy.copy(path)
        shallowPath.append((vertex,costToReach))

        for targetingVertex in neighbours:
            
            distanceToGoal = calculateStraightLineDistance(targetingVertex) 
            
            timeCost = costToReach+1
            
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
            
            
            
        

    def findPathTo(startVertex,targetVertex):
        #print(startVertex.coord, targetVertex.coord, heuristicBool)
        #start of program
        frontierQueue = []
        open = dict()
        closed = dict()
        distanceToGoal = calculateStraightLineDistance(startVertex)
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
            expandVertex(currentVertex[2],currentVertex[1],currentVertex[3], open, closed, frontierQueue)
    #print(" ")
    path = findPathTo(startVertex,targetVertex)
    return path


