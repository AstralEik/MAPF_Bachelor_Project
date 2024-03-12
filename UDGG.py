maptype = input()
height = int(input().split(" ")[1])
width = int(input().split(" ")[1])
map = input()
mapArray = []
vertexArray = []
edgeDict = {}
hasSeen = set()

for i in range(height):
    line = list(input())
    mapArray.append(line)

vertexStack = []
vertexStack.append((1,1))

for x in range(height):
    for y in range(width):
        edgeDict[(x,y)] = []


def check_vertex(x,y):
    if x == 0 and y == 0:
        check_set_right(x,y)
        check_set_down(x,y)
        if(mapArray[x][y] == '.'):
            if mapArray[x+1][y] == '.':
                create_edge_down(x,y)
            if mapArray[x][y+1] == '.':
                create_edge_right(x,y)
                
    elif x == 0 and y == width-1:
        check_set_left(x,y)
        check_set_down(x,y)
        if(mapArray[x][y] == '.'):
                if mapArray[x+1][y] == '.':
                    create_edge_down(x,y)
                if mapArray[x][y-1] == '.':
                    create_edge_left(x,y)
    elif x == height-1 and y == 0:
        check_set_up(x,y)
        check_set_right(x,y)
        if(mapArray[x][y] == '.'):
                if mapArray[x-1][y] == '.':
                    create_edge_up(x,y)
                if mapArray[x][y+1] == '.':
                    create_edge_right(x,y)
    elif x == height-1 and y == width-1:
        check_set_up(x,y)
        check_set_left(x,y)
        if(mapArray[x][y] == '.'):
                if mapArray[x-1][y] == '.':
                    create_edge_up(x,y)
                if mapArray[x][y-1] == '.':
                    create_edge_left(x,y)
    elif x == 0:
        check_set_right(x,y)
        check_set_left(x,y)
        check_set_down(x,y)
        if(mapArray[x][y] == '.'):
                if mapArray[x][y+1] == '.':
                    create_edge_right(x,y)
                if mapArray[x][y-1] == '.':
                    create_edge_left(x,y)
                if mapArray[x+1][y] == '.':
                    create_edge_down(x,y)
    elif x == height-1:
        check_set_right(x,y)
        check_set_left(x,y)
        check_set_up(x,y)        
        if(mapArray[x][y] == '.'):
                if mapArray[x][y+1] == '.':
                    create_edge_right(x,y)
                if mapArray[x][y-1] == '.':
                    create_edge_left(x,y)
                if mapArray[x-1][y] == '.':
                    create_edge_up(x,y)
                    
    elif y == 0:
        check_set_down(x,y)
        check_set_right(x,y)
        check_set_up(x,y)
        if(mapArray[x][y] == '.'):
                if mapArray[x+1][y] == '.':
                    create_edge_down(x,y)
                if mapArray[x-1][y] == '.':
                    create_edge_up(x,y)
                if mapArray[x][y+1] == '.':
                    create_edge_right(x,y)
    elif y == width-1:
        check_set_down(x,y)
        check_set_left(x,y)
        check_set_up(x,y)
        if(mapArray[x][y] == '.'):
                if mapArray[x+1][y] == '.':
                    create_edge_down(x,y)
                if mapArray[x-1][y] == '.':
                    create_edge_up(x,y)
                if mapArray[x][y-1] == '.':
                    create_edge_left(x,y)

    elif(x != 0 and y!= width-1 and x != height-1 and y != 0):
        check_set_right(x,y)
        check_set_left(x,y)
        check_set_down(x,y)
        check_set_up(x,y)
            
        if (mapArray[x][y] == '.'):
            if(mapArray[x+1][y] == '.'):    
                create_edge_down(x,y)
            if(mapArray[x-1][y] == '.'):
                create_edge_up(x,y)
            if(mapArray[x][y+1] == '.'):
                create_edge_right(x,y)
            if(mapArray[x][y-1] == '.'):
                create_edge_left(x,y)


def create_edge_down(x,y):
    if(edgeDict[(x,y)].count((x+1,y)) == 0):
        edgeDict[(x,y)].append(((x+1,y)))
        edgeDict[(x+1,y)].append(((x,y)))
def create_edge_up(x,y):
    if(edgeDict[(x,y)].count((x-1,y)) == 0):
        edgeDict[(x,y)].append(((x-1,y)))
        edgeDict[(x-1,y)].append(((x,y)))
def create_edge_right(x,y):
    if(edgeDict[(x,y)].count((x,y+1)) == 0):
        edgeDict[(x,y)].append(((x,y+1)))
        edgeDict[(x,y+1)].append(((x,y)))
def create_edge_left(x,y):
    if(edgeDict[(x,y)].count((x,y-1)) == 0):
        edgeDict[(x,y)].append(((x,y-1)))
        edgeDict[(x,y-1)].append(((x,y)))


def check_set_down(x,y):
    if((x+1,y) not in hasSeen):
        vertexStack.append((x+1,y))
        hasSeen.add((x+1,y))
def check_set_up(x,y):
    if((x-1,y) not in hasSeen):
        vertexStack.append((x-1,y))
        hasSeen.add((x-1,y))
def check_set_right(x,y):
    if((x,y+1) not in hasSeen):
        vertexStack.append((x,y+1))
        hasSeen.add((x,y+1))
def check_set_left(x,y):
    if((x,y-1) not in hasSeen):
        vertexStack.append((x,y-1))
        hasSeen.add((x,y-1))


def create_udir_graph():
    while len(vertexStack) != 0:
        x,y = vertexStack.pop()
        check_vertex(x,y)

create_udir_graph()
print(edgeDict)