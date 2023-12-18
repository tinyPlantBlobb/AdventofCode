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
            #print(newpoint)
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
    
    def floodfill(board,pipe):
        q = queue.SimpleQueue()
        for i in range(len(board[0])):
            q.put((i,0))
            q.put((i,len(board)-1))
        for i in range(len(board)):
            q.put((0,i))
            q.put((len(board[0])-1,i))
        while not q.empty():
            curr = q.get()
            if board[curr[1]][curr[0]] == ".":
                board[curr[1]][curr[0]] = "#"
                for i in [(0,1),(1,0),(-1,0),(0,-1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]: 
                    xn = curr[0]+i[0]
                    yn = curr[1]+i[1]
                    
                    if xn >= 0 and yn >= 0 and yn < len(board) and xn < len(board[0]):
                        if board[yn][xn] == ".":
                            q.put((xn,yn))
                        if board[yn][xn] in "FL|S" and board[yn][xn-1] == "J7|":
                            q.put((xn,yn+1))
                            q.put((xn+1,yn+1))
                        if board[yn][xn] in "J7|" and board[yn][xn+1] == "FL|":
                            q.put((xn,yn+1))
                            q.put((xn+1,yn+1))
                        if board[yn][xn] in "SJL-" and board[yn+1][xn] == "F7-":
                            q.put((xn+1,yn))
                            q.put((xn+1,yn+1))
            else:
                if board[yn][xn] in "FL|S" and board[yn][xn-1] == "J7|S":
                    xn = curr[0]
                    yn = curr[1] + 1
                if board[yn-1][xn] in "SJL-" and board[yn][xn] == "SF7-":
                    xn = curr[0] + 1
                    yn = curr[1]
                
                if xn >= 0 and yn >= 0 and yn < len(board)-1 and xn < len(board[0])-1:
                    if board[yn][xn] == ".":
                        q.put((xn,yn))
                    if board[yn][xn] in "FL|S" and board[yn][xn-1] == "J7|":
                        q.put((xn,yn+1))
                        q.put((xn+1,yn+1))
                    if board[yn][xn] in "J7|" and board[yn][xn+1] == "FL|":
                        q.put((xn,yn+1))
                        q.put((xn+1,yn+1))
                    if board[yn][xn] in "SJL-" and board[yn+1][xn] == "F7-":
                        q.put((xn+1,yn))
                        q.put((xn+1,yn+1))
                        # if board[yn][xn] =="F" and board[yn][xn-1] == "7":
                        #     #get next possible filled horizontal
                        # elif board[yn][xn] =="L" and board[yn][xn-1] == "J":
                        #     #get next possible filled horizontal
                        # elif board[yn][xn] =="|" and board[yn][xn+1] == "|":
                            
                        # elif board[yn][xn] =="-" and board[yn-1][xn] == "-":
                        # #     q.put((xn,yn))
                        # elif board[yn][xn] == "L" and board[yn-1][xn]== "F":
                        # #     q.put((xn,yn))
                        # elif board[yn][xn] == "J" and board[yn][xn+1]== "F":
                            
        
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
    #print(index)
    board = [["." for x in range(len(y))] for y in input]
    
    for y in range(len(input)):
        for x in range(len(input[y])):
            if (x,y) in pipe:
                board[y][x] = input[y][x]
            else:
                board[y][x] = "."
    floodfill(board, pipe)
    AoCparse.tofile(board)
    counter = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == ".":
                counter +=1
                
    print(counter)
        
input = AoCparse.getinput(10)
pt1(input)
pt2(input)




