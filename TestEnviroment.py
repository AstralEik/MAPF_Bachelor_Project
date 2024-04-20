from CBS import *
from HCAstar import *
from UDGG import *
from AStar import *
from STAStarForCbs import *
import random

graph, reservationTable, probableMaxTime, height, width = createGraph()

agents = []

print("hello")


for i in range(3):
    pathExists = None
    y1 = random.randint(0,height-1)
    x1 = random.randint(0,width-1)
    
    y2 = random.randint(0,height-1)
    x2 = random.randint(0,width-1)
    
    if (y1, x1) != (y2, x2):
        pathExists = Astar((y1, x1),(y2, x2),graph)
    if pathExists != None:
        agents.append([y1,x1,y2,x2])

print(agents)



#agents = ([1,0,2,3],[0,1,3,2])
#agents = ([1,1,1,4],[1,3,1,0])
agents = [[1, 2, 1, 1], [2, 3, 3, 2], [2, 1, 0, 1]]
#test = Astar((1,0),(2,3),graph)
#for i in test:
#    print(i[0].coord, i[1])

# generate random list of agents in format [y1,x1,y2,x2]
#testingCoords = ([1,0,2,3],[0,1,3,2])

cbsStates = CBS(agents,graph,reservationTable,probableMaxTime)

#print cbs path
print("--------CBS PATH------")
lowestCostCbsNode = None
for i in cbsStates:
    if lowestCostCbsNode == None and i.isGoalNode == True:
            lowestCostCbsNode = i
    elif(lowestCostCbsNode != None and i.cost < lowestCostCbsNode.cost and i.isGoalNode == True):
            lowestCostCbsNode = i
if lowestCostCbsNode != None:
    for x in lowestCostCbsNode.paths:
        print(" ")
        for y in x:
            print(y[0].coord[0], y[0].coord[1], y[1])

print("------HCAstar PATH------")

hcaStarPath = HCAstar(agents, graph, reservationTable, probableMaxTime) 

# print hcastar path
for x in hcaStarPath:
    print(" ")
    for m in x:
        print(m[0].coord[0],m[0].coord[1],m[1])