import copy
from math import sqrt
from UDGG import *
import heapq
UDG = createGraph()


startVertex = (UDG[1,1])
targetVertex = (UDG[11,7])

frontierQueue = []
hasSeenSet = set()
lowestPathCost = float(20000.00000) 
pathTaken = []

def snd(x:tuple):
    return x[1]

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
    global lowestPathCost
    global hasSeenSet
    hasSeenSet.add(vertex)
    neighbours = vertex.neighbours
    realPath = copy.copy(path)
    realPath.append(vertex)
    for vertexB in neighbours:
        distanceToGoal = calculateDistance(vertexB) 
        timeCost = costToReach+1
        if vertexB not in hasSeenSet or distanceToGoal+timeCost < lowestPathCost:
            lowestPathCost = distanceToGoal
            heapq.heappush(frontierQueue,(distanceToGoal,timeCost,vertexB,realPath))
            
def findPathTo(startVertex,targetVertex):
    global hasSeenSet
    global pathTaken
    #start of program
    distanceToGoal = calculateDistance(startVertex)
    heapq.heappush(frontierQueue,(distanceToGoal,0,startVertex,[]))
    while len(frontierQueue) != 0:
        currentVertex = heapq.heappop(frontierQueue)
        if(currentVertex[2] == targetVertex):
            print("found path!")
            hasSeenSet.add(targetVertex)
            pathTaken = currentVertex[3]
            pathTaken.append(currentVertex[2])
            break
        expandVertex(currentVertex[2],currentVertex[1],currentVertex[3])
findPathTo(startVertex,targetVertex)

for i in pathTaken:
   print(i.coord)
