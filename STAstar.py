from math import sqrt
from UDGG import *

UDG = createGraph()

agent = ((0,1),(2,1))

startVertex = (agent[0][0],agent[0][1])
targetVertex = (agent[1][0], agent[1][1])

frontierQueue = []
hasSeenSet = set()
lowestPathCost = float(20000.00000) 

def snd(x:tuple):
    return x[1]
def calculateSomeFuckingTriangles(x1,y1):
    
    d1 = sqrt(pow(targetVertex[0]-x1,2))
    d2 = sqrt(pow(targetVertex[1]-y1,2))
    if(d1 < 0):
        d1 = d1*-1
    if(d2 < 0):
        d2 = d2*-1
    distance = d1 + d2
    
    
    return distance

def expandVertex(x,y):
    global lowestPathCost
    hasSeenSet.add((x,y))
    neighbours = UDG.get((x,y))
    for vertex in neighbours:
        dis = calculateSomeFuckingTriangles(vertex[0],vertex[1]) 
        if vertex not in hasSeenSet or dis < lowestPathCost:
            lowestPathCost = dis
            print(dis)
            frontierQueue.append((vertex,dis))
            frontierQueue.sort(key=snd, reverse=True)
            

def findPathTo(x1,y1,x2,y2):
    
    #start of program
    distanceToGoal = calculateSomeFuckingTriangles(x1,y1)
    frontierQueue.append(((x1,y1), distanceToGoal))
    
    
    while len(frontierQueue) != 0:
        currentVertex = frontierQueue.pop()
        if((currentVertex[0][0],currentVertex[0][1]) == (x2,y2)):
            hasSeenSet.add((x2,y2))
            break
        expandVertex(currentVertex[0][0],currentVertex[0][1])
print(UDG)

findPathTo(agent[0][0],agent[0][1],agent[1][0],agent[1][1])

print(hasSeenSet)