import AoCparse

def getstartingpoint(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "S":
                return (x,y)

def getnextfields(map, current):
    newfields = []
    for f in current:
        for i in (0,1), (1,0), (-1,0), (0,-1):
            if f[1]+i[1] >= 0 and f[0]+i[0] >= 0 and f[1]+i[1] < len(map) and f[0]+i[0] < len(map[0]):
                if map[f[1]+i[1]][f[0]+i[0]] == "." or map[f[1]+i[1]][f[0]+i[0]] == "S":
                    if (f[0]+i[0],f[1]+i[1]) not in newfields:
                        newfields.append((f[0]+i[0],f[1]+i[1]))
    return newfields
    
    
map = AoCparse.getinput(21)
currentpoints = [getstartingpoint(map)]
print(currentpoints)
for i in range(64):
    currentpoints = getnextfields(map, currentpoints)

print(len(currentpoints))