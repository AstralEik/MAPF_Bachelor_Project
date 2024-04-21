from STAstar import *
from UDGG import *
def HCAstar(agents, graph, probableMaxTime):
    
    #graph, reservationTable, probableMaxTime = createGraph()
    #testingCoords = ([1,0,1,3],[1,4,1,1])
    #testingCoords = ([1,0,2,3],[0,1,3,2])
    #print("hellu")
    reservationSet = set()
    
    pathList = []
    for i in agents:
        path = STAstar((i[0],i[1]),(i[2],i[3]),graph,reservationSet)
        pathList.append(path)
        #print(" ")
        for m in path:
            #print(m[0].coord[0],m[0].coord[1],m[1])
            reservationSet.add((m[0].coord[0],m[0].coord[1],m[1]))
        target = path.pop()
        path.append(target)
        for n in range(target[1], probableMaxTime):
            reservationSet.add((target[0].coord[0],target[0].coord[1],n))
    return pathList

