import copy
from math import sqrt
from UDGG import *
import heapq
def STAstar(fromCoords,toCoords,graph):
    udg = graph
    #https://mat.uab.cat/~alseda/MasterOpt/AStar-Algorithm.pdf
    startVertex = (udg[fromCoords])
    targetVertex = (udg[toCoords])

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

    def expandVertex(vertex,costToReach,path):
        closed[vertex] = costToReach
        del open[vertex]
        neighbours = vertex.neighbours
        shallowPath = copy.copy(path)
        shallowPath.append(vertex)
        for targetVertex in neighbours:
            distanceToGoal = calculateDistance(targetVertex) 
            timeCost = costToReach+1
            if targetVertex in open.keys():
                if open[targetVertex] <= timeCost:
                    continue
            elif targetVertex in closed.keys():
                if closed[targetVertex] <= timeCost:
                    continue
                del closed[targetVertex]
                open[targetVertex] = timeCost
                heapq.heappush(frontierQueue,((distanceToGoal+timeCost),timeCost,targetVertex,shallowPath))
            else:
                open[targetVertex] = timeCost
                heapq.heappush(frontierQueue,((distanceToGoal+timeCost),timeCost,targetVertex,shallowPath))

                
    def findPathTo(startVertex,targetVertex):
        #start of program
        distanceToGoal = calculateDistance(startVertex)
        open[startVertex] = 0
        heapq.heappush(frontierQueue,(distanceToGoal,0,startVertex,[]))
        while len(frontierQueue) != 0:
            currentVertex = heapq.heappop(frontierQueue)
            if(currentVertex[2] == targetVertex):
                print("found path!")
                pathTaken = currentVertex[3]
                pathTaken.append(currentVertex[2])
                return pathTaken
            expandVertex(currentVertex[2],currentVertex[1],currentVertex[3])
    path = findPathTo(startVertex,targetVertex)
    return path
