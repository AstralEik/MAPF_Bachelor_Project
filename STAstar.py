import copy
from math import sqrt
from UDGG import *
import heapq
def STAstar(fromCoords,toCoords,graph,reservationTable):
    #https://mat.uab.cat/~alseda/MasterOpt/AStar-Algorithm.pdf
    startVertex = (graph[0][fromCoords])
    targetVertex = (graph[0][toCoords]) #time does not really matter here since this returns a vertex object

    frontierQueue = []
    open = dict()
    closed = dict()

    def calculateDistance(vertex):
        d1 = sqrt(pow(targetVertex.coord[0]-vertex.coord[0],2))
        d2 = sqrt(pow(targetVertex.coord[1]-vertex.coord[1],2))
        if(d1 < 0):
            d1 = d1*-1
        if(d2 < 0):
            d2 = d2*-1
        distance = d1 + d2
        return distance

    def expandVertex(vertex,costToReach,path,waitBool):
        closed[vertex,costToReach] = costToReach
        if(waitBool == False):
            del open[vertex,costToReach]
        neighbours = vertex.neighbours
        shallowPath = copy.copy(path)
        shallowPath.append((vertex,costToReach))
        wait = False
        for targetVertex in neighbours:
            distanceToGoal = calculateDistance(targetVertex) 
            timeCost = costToReach+1
            if (targetVertex,timeCost) in open.keys():
                if open[targetVertex,timeCost] <= timeCost:
                    continue
            elif (targetVertex,timeCost) in closed.keys():
                if closed[targetVertex,timeCost] <= timeCost:
                    continue
                del closed[targetVertex,timeCost]
                open[targetVertex,timeCost] = timeCost
                if reservationTable[targetVertex.coord[0],targetVertex.coord[1],timeCost] == False:
                    heapq.heappush(frontierQueue,((distanceToGoal+timeCost),timeCost,targetVertex,shallowPath))
                elif reservationTable[targetVertex.coord[0],targetVertex.coord[1],timeCost+1] == False:
                    wait = True
            else:
                open[targetVertex,timeCost] = timeCost
                if reservationTable[targetVertex.coord[0],targetVertex.coord[1],timeCost] == False:
                    heapq.heappush(frontierQueue,((distanceToGoal+timeCost),timeCost,targetVertex,shallowPath))
                elif reservationTable[targetVertex.coord[0],targetVertex.coord[1],timeCost+1] == False:
                    wait = True
                    
        if wait == True:
            open[vertex,costToReach+1] = costToReach+1
            expandVertex(vertex,costToReach+1,shallowPath,True)

                
    def findPathTo(startVertex,targetVertex):
        #start of program
        distanceToGoal = calculateDistance(startVertex)
        open[startVertex, 0] = 0
        heapq.heappush(frontierQueue,(distanceToGoal,0,startVertex,[]))
        while len(frontierQueue) != 0:
            currentVertex = heapq.heappop(frontierQueue)
            if(currentVertex[2] == targetVertex):
                print("found path!")
                pathTaken = currentVertex[3]
                pathTaken.append((currentVertex[2],currentVertex[1]))
                return pathTaken
            expandVertex(currentVertex[2],currentVertex[1],currentVertex[3],False)
    path = findPathTo(startVertex,targetVertex)
    return path
