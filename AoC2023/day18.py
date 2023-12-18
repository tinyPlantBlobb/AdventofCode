import AoCparse

input = AoCparse.getinput(18)

def digtrench(line, board, pos):
    
    direction = getdirection(line.split(" ")[0])
    length = int(line.split(" ")[1])
    color = line.split(" ")[2]
    endx = pos[0]
    endy = pos[1]
    for i in range(length):
        board[endy][endx] = "#"
        endx = endx+direction[0]
        endy = endy+direction[1]
    return (endx,endy)
def getdirection(d):
    if "L" == d:
        return (-1,0)
    elif "R" == d:
        return (1,0)
    elif "U" in l:
        return (0,-1)
    elif "D" == d:
        return(0,1)
    return (0,0)
def getmaxsize(input):
    west=0 
    north=0
    south=0
    east = 0
    for l in input:
        if "L" in l:
            west += int(l.split(" ")[1])
        elif "R" in l:
            east += int(l.split(" ")[1])
        elif "U" in l:
            north += int(l.split(" ")[1])
        elif "D" in l:
            south += int(l.split(" ")[1])
    return (max(east,west), max(south,north))

board = [["." for x in range(getmaxsize(input)[0] +1)] for i in range(getmaxsize(input)[1]+1)]
print(board)
pos = (len(board)/2,len(board[0])/2)
for l in input:
    print(pos)
    pos = digtrench(l, board, pos)
print(board)
AoCparse.tofile(board)