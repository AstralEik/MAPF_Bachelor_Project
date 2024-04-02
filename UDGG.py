import copy
from classdefs import Vertex
import sys
def createGraph():
    maptype = input()
    height = int(input().split(" ")[1])
    width = int(input().split(" ")[1])
    map = input()
    mapArray = []
    hasBuilt = set()
    probableMaxTime = height+width
    
    sys.setrecursionlimit(2000000)

    graph = dict()

    for i in range(height):
        line = list(input())
        mapArray.append(line)
    
    def buildGraph(y,x):
        if((y,x) not in hasBuilt):
            hasBuilt.add((y,x))
            newVertex = Vertex()
            newVertex.coord[0] = y
            newVertex.coord[1] = x
            graph[y,x] = newVertex
        
            if(y-1 >= 0 and y-1 < height):        
                if (y-1,x) not in hasBuilt and mapArray[y-1][x] == '.':
                    buildGraph(y-1,x)
                    newVertex.neighbours.append(graph[y-1,x])
                elif((y-1,x) in hasBuilt and mapArray[y-1][x] == '.'):
                    newVertex.neighbours.append(graph[y-1,x])        
                    
            if(x-1 >= 0 and x-1 < width):
                if (y,x-1) not in hasBuilt and mapArray[y][x-1] == '.':
                    buildGraph(y,x-1)
                    newVertex.neighbours.append(graph[y,x-1])
                elif((y,x-1) in hasBuilt and mapArray[y][x-1] == '.'):
                    newVertex.neighbours.append(graph[y,x-1])
                    
            if(y+1 >= 0 and y+1 < height):
                if (y+1,x) not in hasBuilt and mapArray[y+1][x] == '.':
                    buildGraph(y+1,x)
                    newVertex.neighbours.append(graph[y+1,x])
                elif((y+1,x) in hasBuilt and mapArray[y+1][x] == '.'):
                    newVertex.neighbours.append(graph[y+1,x])
                    
            if(x+1 >= 0 and x+1 < width):   
                if (y,x+1) not in hasBuilt and mapArray[y][x+1] == '.':
                    buildGraph(y,x+1)
                    newVertex.neighbours.append(graph[y,x+1])
                elif((y,x+1) in hasBuilt and mapArray[y][x+1] == '.'):
                    newVertex.neighbours.append(graph[y,x+1])

    for i in range(height):
        for x in range(width):
            buildGraph(i,x)

    graphWithTime = dict()
    for i in range(probableMaxTime):
        graphWithTime[i] = graph
    
    reservationTable = dict()
    for t in range(probableMaxTime):
        for h in range(height):
            for w in range(width):
                reservationTable[h,w,t] = False
    return graphWithTime, reservationTable