import time
from CBS import *
from HCAstar import *
from UDGG import *
from AStar import *
import random


class scenarioResult:
        def __init__(self, cbsTime, hcaTime, optimalString) -> None:
            self.cbsTimeString = cbsTime
            self.hcaTimeString = hcaTime
            self.optimalString = optimalString

graph, probableMaxTime, height, width = createGraph()



def testWithAgentNr (nr):
    agents = []

    #print("hello")
    startingCoords = set()
    targetCoords = set()

    while len(agents) < nr:
        pathExists = None
        y1 = random.randint(0,height-1)
        x1 = random.randint(0,width-1)
        
        y2 = random.randint(0,height-1)
        x2 = random.randint(0,width-1)
        
        if (y1, x1) != (y2, x2):
            pathExists = Astar((y1, x1),(y2, x2),graph)
        if pathExists != None and (y1, x1) not in startingCoords and (y2,x2) not in targetCoords: 
            agents.append((y1,x1,y2,x2))
            startingCoords.add((y1,x1))
            targetCoords.add((y2,x2))

    print(agents)



    #agents = ([1,0,2,3],[0,1,3,2])
    #agents = ([1,1,1,4],[1,3,1,0])
    agents = [(5, 1, 4, 5), (3, 3, 2, 4), (7, 1, 5, 4), (1, 7, 7, 7), (6, 3, 7, 6), (2, 2, 6, 5), (6, 1, 3, 0), (0, 0, 7, 1), (6, 2, 1, 5), (7, 6, 5, 0)]
    #agents = [[1, 2, 1, 1], [2, 3, 3, 2], [2, 1, 0, 1]]
    #test = Astar((1,0),(2,3),graph)
    #for i in test:
    #    print(i[0].coord, i[1])

    # generate random list of agents in format [y1,x1,y2,x2]
    #testingCoords = ([1,0,2,3],[0,1,3,2])
    cbsstart = time.time()
    cbsStates = CBS(agents,graph,probableMaxTime)
    cbsend = time.time()
    #print(cbsend-cbsstart)
    #print cbs path
    #print("--------CBS PATH------")

    lowestCostCbsNode = None
    for i in cbsStates:
        if lowestCostCbsNode == None and i.isGoalNode == True:
                lowestCostCbsNode = i
        elif(lowestCostCbsNode != None and i.cost < lowestCostCbsNode.cost and i.isGoalNode == True):
                lowestCostCbsNode = i
    #if lowestCostCbsNode != None:
        #for x in lowestCostCbsNode.paths:
            #print(" ")
            #for y in x:
                #print(y[0].coord[0], y[0].coord[1], y[1])
    #print(lowestCostCbsNode.cost)

    #print("------HCAstar PATH------")
    hcastart = time.time()
    hcaStarPath = HCAstar(agents, graph, probableMaxTime) 
    hcaend = time.time()

    # print hcastar path
    hcacount=0
    for x in hcaStarPath:
        #print(" ")
        for m in x:
            hcacount+=1
            #print(m[0].coord[0],m[0].coord[1],m[1])
    #print(hcacount)
    gamingResult = scenarioResult(cbsend-cbsstart, hcaend-hcastart, hcacount-lowestCostCbsNode.cost)
    return gamingResult
    #print("CBS", cbsend-cbsstart, "seconds")
    #print("HCA*", hcaend-hcastart, "seconds")
    #print("CBS Was", hcacount-lowestCostCbsNode.cost, "nodes more optimal than HCA star")
resultList = list()
resultList.append((testWithAgentNr(10), 10))

for i in resultList:
    #print("With agent amount", i[1])
    print(i[0].cbsTimeString)
    print(i[0].hcaTimeString)
    print(i[0].optimalString)
    