from STAstar import *
from UDGG import *

UDG = createGraph()
path = STAstar((1,1),(11,7),UDG)

for i in path:
    print(i.coord)
