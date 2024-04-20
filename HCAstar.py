from STAstar import *
from UDGG import *
def HCAstar(agents, graph, reservationTable, probableMaxTime):
    
    #graph, reservationTable, probableMaxTime = createGraph()
    #testingCoords = ([1,0,1,3],[1,4,1,1])
    #testingCoords = ([1,0,2,3],[0,1,3,2])
    #print("hellu")
    
    
    pathList = []
    for i in agents:
        path = STAstar((i[0],i[1]),(i[2],i[3]),graph,reservationTable)
        pathList.append(path)
        #print(" ")
        for m in path:
            #print(m[0].coord[0],m[0].coord[1],m[1])
            reservationTable[m[0].coord[0],m[0].coord[1],m[1]] = True
        target = path.pop()
        for n in range(target[1], probableMaxTime):
            reservationTable[target[0].coord[0],target[0].coord[1],n] = True
    return pathList

