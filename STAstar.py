from UDGG import *

UDG = createGraph()

agent = ((0,1),(2,1))

vertexStack = []
hasSeenSet = set()

def expandVertex(x,y):
    hasSeenSet.add((x,y))
    neighbours = UDG.get((x,y))
    for vertex in range (neighbours):
        if vertex not in hasSeenSet:
            vertexStack.append(vertex)
            

def findPathTo(x1,y1,x2,y2):
    vertexStack.append((x1,y1))
    while len(vertexStack) != 0:
        currentVertex = vertexStack.pop()
        if(currentVertex == (x2,y2)):
            hasSeenSet.add(x2,y2)
            break
        expandVertex(currentVertex[0],currentVertex[1])
print(UDG)

findPathTo(agent[0][0],agent[0][1],agent[1][0],agent[1][1])

print(hasSeenSet)