maptype = input()
height = int(input().split(" ")[1])
width = int(input().split(" ")[1])
map = input()
mapArray = []
vertexArray = []
edgeDict = {}

for i in range(height):
    line = list(input())
    mapArray.append(line)

vertexStack = []
vertexStack.append((1,1))

for x in range(height):
    for y in range(width):
        edgeDict[(x,y)] = []

print(edgeDict)

def check_vertex(x,y):
    if(x != 0 and y!= width-1 and x != height and y != 0):
        print(x,y)
        if (mapArray[x][y] == '.'):
            if(mapArray[x+1][y] == '.'):
                vertexStack.append((x+1,y))
                print(x+1,y)
                if(edgeDict[(x,y)].count((x+1,y) == 0)):
                    edgeDict[(x,y)].append(((x+1,y)))
                    edgeDict[(x+1,y)].append(((x,y)))


            if(mapArray[x-1][y] == '.'):
                vertexStack.append((x-1,y))
                print(x-1,y)
                if(edgeDict[(x,y)].count((x-1,y) == 0)):
                    edgeDict[(x,y)].append(((x-1,y)))
                    edgeDict[(x-1,y)].append(((x,y)))


            if(mapArray[x][y+1] == '.'):
                vertexStack.append((x,y+1))
                print(x,y+1)
                if(edgeDict[(x,y)].count((x,y+1) == 0)):
                    edgeDict[(x,y)].append(((x,y+1)))
                    edgeDict[(x,y+1)].append(((x,y)))


            if(mapArray[x][y-1] == '.'):
                vertexStack.append((x,y-1))
                print(x,y-1)
                if(edgeDict[(x,y)].count((x,y-1) == 0)):
                    edgeDict[(x,y)].append(((x,y-1)))
                    edgeDict[(x,y-1)].append(((x,y)))
    else:
        vertexStack.append((x+1,y))
        vertexStack.append((x-1,y))
        vertexStack.append((x,y+1))
        vertexStack.append((x,y-1))



def create_dir_graph():
    while len(vertexStack) != 0:
        x,y = vertexStack.pop()
        print("new vertex")
        print(x,y)    
        check_vertex(x,y)

create_dir_graph()
print(edgeDict)