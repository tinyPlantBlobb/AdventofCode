import AoCparse
def expand(image):
    for y in range(len(image)):
        if "#" not in image[y]:
            emptyspace.append((-1,y))
        column = [row[y] for row in image]
        if "#" not in column:
            emptyspace.append((y, -1))
    sorted(emptyspace)
            
def galaxies(image):
    for y in range(len(image)):
        for x in range(len(image[y])):
            if image[y][x] == "#":
                galaxy.append((x,y))

def getexpansion(g1, g2, space):
    expansionfactor= 1000000 - 1
    count = 0
    lowerx = min(g1[0], g2[0])
    higherx = max (g1[0], g2[0])
    lowery = min(g1[1], g2[1])
    highery = max (g1[1], g2[1])
    for s in space:
        if s[1] in range(lowery, highery): 
            count += expansionfactor
        if s[0] in range(lowerx, higherx): 
            count += expansionfactor
    return count

def distances(galaxy):
    result = 0
    while galaxy:
        currentgalaxy = galaxy.pop()
        for g in galaxy:
            result += abs(g[0]- currentgalaxy[0]) + abs(g[1]- currentgalaxy[1]) + getexpansion(g, currentgalaxy, emptyspace)
    return result
    
    
emptyspace=[]
galaxy = []
input = AoCparse.getinput(11)
expand(input)

galaxies(input)

print(distances(galaxy))