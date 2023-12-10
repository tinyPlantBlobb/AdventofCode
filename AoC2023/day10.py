import AoCparse
import queue
north=(0,-1)
south = (0,1)
east=(1,0)
west=(-1, 0)

def pt1(input):
    def getstartingpoint(input):
        for y in range(len(input)):
            for x in range(len(input[y])-1):
                if input[y][x] == "S":
                    return (x,y)
        
    def isconnectedto(board, x, y):
        tocheck = connections(board[y][x])
        connect = [] 
        for nextfield in tocheck:
            xn = x+nextfield[0]
            yn = y+nextfield[1]
            if xn >= 0 and yn >= 0:
                newcon =connections(board[yn][xn])
                if newcon is not None:
                    for i in newcon:
                        xc = xn+i[0]
                        yc = yn+i[1]
                        # compare if the coords of the new fields that is looked at are the same as the og field
                        if xc == x and yc == y:
                            connect.append((xn,yn))
                            break   
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
    pipe = {}
    startingpoint = getstartingpoint(input)
    q = queue.SimpleQueue()
    q.put(startingpoint)
    # pipe elements are of the structure (distance from startingpoint, connected tiles )
    pipe.update({startingpoint: 0})
    index = 0
    while not q.empty():
        e = q.get()

        newpoint = isconnectedto(input, *e)
        if newpoint:
            print(newpoint)
            for point in newpoint:
                if point not in pipe.keys():
                    q.put(point)
                    pipe.update({e:index})
            index +=1

        
    print((max(pipe.values()) + 2) /2)

def pt2(input):
    def getstartingpoint(input):
        for y in range(len(input)):
            for x in range(len(input[y])-1):
                if input[y][x] == "S":
                    return (x,y)
        
    def isconnectedto(board, x, y):
        tocheck = connections(board[y][x])
        connect = [] 
        for nextfield in tocheck:
            xn = x+nextfield[0]
            yn = y+nextfield[1]
            if xn >= 0 and yn >= 0:
                newcon =connections(board[yn][xn])
                if newcon is not None:
                    for i in newcon:
                        xc = xn+i[0]
                        yc = yn+i[1]
                        # compare if the coords of the new fields that is looked at are the same as the og field
                        if xc == x and yc == y:
                            connect.append((xn,yn))
                            break   
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
    pipe = []
    startingpoint = getstartingpoint(input)
    q = queue.SimpleQueue()
    q.put(startingpoint)
    # pipe elements are of the structure (distance from startingpoint, connected tiles )
    pipe.append(startingpoint)
    index = 0
    while not q.empty():
        e = q.get()
        newpoint = isconnectedto(input, *e)
        if newpoint:
            for point in newpoint:
                if point not in pipe:
                    q.put(point)
                    pipe.append(e)
            index +=1
    print(index)
input = AoCparse.getinput(10)
pt1(input)
pt2(input)
