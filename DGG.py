maptype = input()
height = int(input().split(" ")[1])
width = int(input().split(" ")[1])
map = input()
mapArray = []
vertexArray = []
edgeArray = []

for i in range(height):
    line = list(input())
    mapArray.append(line)

print(mapArray)