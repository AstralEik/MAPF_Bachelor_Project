from STAstar import *
from UDGG import *

graph, reservationTable = createGraph()


testingCoords = ([0,1,3,2],[1,0,2,3])

for i in testingCoords:
    path = path = STAstar((i[0],i[1]),(i[2],i[3]),graph,reservationTable)
    for i in path:
        print(i[0].coord[0],i[0].coord[1],i[1])
        reservationTable[i[0].coord[0],i[0].coord[1],i[1]] = True


