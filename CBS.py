from UDGG import *
from STAStarForCbs import *
def CBS(agents, graph, reservationTable, probableMaxTime):
    #graph, reservationTable, probableMaxTime = createGraph()

    open = []
    closed = []
    listOfCbsStates = []

    #agents = ([1,0,2,3],[0,1,3,2])
    #agents = ([0,1,2,3],[1,0,3,2])
    #agents = ([1,1,1,4],[1,3,1,0])
    class CBSNode:
        def __init__(self, paths, cost, parent) -> None:
            self.paths = paths
            self.cost = cost
            self.children = []
            self.parent = parent
            self.constraints = []
            self.agentToRecheck = None
            self.isGoalNode = False
            
    def evalCBSNode(node: CBSNode):
        node.isGoalNode = True
        
        if(node.agentToRecheck != None):
            #print(node.agentToRecheck)
            agentId = node.agentToRecheck
            node.paths[agentId] = lowLevelSearch((agents[agentId][0], agents[agentId][1]),(agents[agentId][2], agents[agentId][3]),graph,node.constraints, agentId)
        
        
        longestPath = 0
        for i in node.paths:
            node.cost += len(i)
            if longestPath < len(i):
                longestPath = len(i)

        #print(" ")
        
        ## Check for vertex conflicts
        vertexConflictDict = dict()
        for i in range(longestPath):
        
            for x in range(len(node.paths)):
                
                current = node.paths[x]
                if i < len(current):
                    if current[i] not in vertexConflictDict.keys():
                        vertexConflictDict[current[i]] = x   
                    else:
                        node.isGoalNode = False
                        
                        
                        #print(" ")
                        a1 = vertexConflictDict[current[i]]
                        #print(a1)
                        a2 = x
                        #print(a2)
                        
                        placeAndTime = current[i]
                    
                        leftChild = CBSNode(copy.copy(node.paths),0,node)
                        rightChild = CBSNode(copy.copy(node.paths),0,node)
                        leftChild.constraints = copy.copy(node.constraints)
                        leftChild.constraints.append((a1, placeAndTime[0].coord[0], placeAndTime[0].coord[1], placeAndTime[1]))
                        leftChild.agentToRecheck = a1
                        
                        rightChild.constraints = copy.copy(node.constraints)
                        rightChild.constraints.append((a2, placeAndTime[0].coord[0], placeAndTime[0].coord[1], placeAndTime[1]))
                        rightChild.agentToRecheck = a2
                        
                        node.children.append(leftChild)
                        node.children.append(rightChild)
                        
                        open.append(leftChild)
                        open.append(rightChild)
                        
                        return node
                    
                    
                            
        return node
                    

    def lowLevelSearch(agentStart, agentTarget, graph, constraints, agentId):
        ## add constraints to rT
        constraintsForAgent = set()
        for i in constraints:
            if i[0] == agentId:
                
                #print(i)
                constraintsForAgent.add((i[1], i[2], i[3]))
                
        #print(agentStart, agentTarget)
        path = STAstar(agentStart, agentTarget, graph, constraintsForAgent)
        

        return path


    intialNodeSearch = []

    for i in agents:
        intialNodeSearch.append(lowLevelSearch((i[0],i[1]),(i[2],i[3]),graph,[],0))

    topOfCBSTree = CBSNode(intialNodeSearch, 0, None)

    open.append(topOfCBSTree)

    while len(open) != 0:
        currentNode = open.pop()
        listOfCbsStates.append(evalCBSNode(currentNode))

    return listOfCbsStates
    #lowestCostCbsNode = None
    #for i in listOfCbsStates:
    #    if lowestCostCbsNode == None and i.isGoalNode == True:
    #        lowestCostCbsNode = i
    #    elif(lowestCostCbsNode != None and i.cost < lowestCostCbsNode.cost and i.isGoalNode == True):
    #        lowestCostCbsNode = i
    #for x in lowestCostCbsNode.paths:
    #    print(" ")
    #    for y in x:
    #        print(y[0].coord[0], y[0].coord[1], y[1])

    #somethinglist = []
    #somethinglist.append(topOfCBSTree)
    #while len(somethinglist) != 0:
    #    print(" ")
    #    currentsomething = somethinglist.pop()
    #    for i in currentsomething.constraints:
    #        print((i[0], i[1][0], i[1][1], i[2]))
    #    if(len(currentsomething.children) != 0):
    #        somethinglist.append(currentsomething.children[0])
    #        somethinglist.append(currentsomething.children[1])
