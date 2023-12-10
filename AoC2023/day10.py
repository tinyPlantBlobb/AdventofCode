import AoCparse
north=(0,-1)
south = (0,1)
east=(1,0)
west=(-1, 0)


def getstartingpoint(input):
    for y in range(len(input)):
        for x in range(len(input[y])-1):
            if input[y][x] == "S":
                return (x,y)
    
def isconnected(board, x, y):
    print(f"{x},{y}, {board[y][x]}")
    tocheck = connections(board[y][x])
    connect = [] 
    for nextfield in tocheck:
        xn = x+nextfield[0]
        yn = y+nextfield[1]
        if xn >= 0 and yn >= 0:
            newcon =connections(board[yn][xn])
            print(newcon)
            if newcon is not None:
                for i in newcon:
                    xc = xn+i[0]
                    yc = yn+i[1]
                    print(f"{xc}, {yc}, {board[yn][xn]} and {xn}, {yn}")
                    # compare if the coords of the new fields that is looked at are the same as the og field
                    if xc == x and yc == y:
                        print("added")
                        connect.append((xn,yn))
                        break
    print(connect)   
    return connect
            
def connections(char):
    if char == "|":
        return [north,south]
    elif char == "-":
        return [west, east]
    elif char == "L":
        return [north, east]
    elif char == "J":
        return [north, west]
    elif char == "7":
        return [west, south]
    elif char == "F":
        return [south,east]
    
    elif char == "S":
        return [south, east, west, north]
    elif char == ".":
        return []
    else:
        return "error"

input = AoCparse.getinput(10)
pipe = []
startingpoint = getstartingpoint(input)

pipe.append((startingpoint))
#pipe.append(isconnected(input, *startingpoint))
# newpoint = (0,0)
# newpoint2 = (0,0)
# while newpoint != newpoint2:
#     newpoint = isconnected(input, *pipe[-1][1])
#     if newpoint not in pipe:
#         pipe.append(newpoint)
#     newpoint2 = isconnected(input, *pipe[-1][0])
    
print(pipe)