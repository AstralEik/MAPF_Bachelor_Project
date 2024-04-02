from STAstar import *
from UDGG import *

graph, reservationTable = createGraph()


path = STAstar((1,1),(11,7),graph,reservationTable)

for i in path:
    print(i[0].coord[0],i[0].coord[1],i[1])
    reservationTable[i[0].coord[0],i[0].coord[1],i[1]] = True
