import AoCparse
import queue

input = AoCparse.getinput(18)
def pt1(input):
    def digtrench(line, board, pos):
        direction = getdirection(line.split(" ")[0])
        length = int(line.split(" ")[1])
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
        print(f"east {east}, north {north}")
        return (max(east,west), max(south,north))

    def floodfill(board):
        q = queue.SimpleQueue()
        q.put((422,356))

        while not q.empty():
            curr = q.get()
            if board[curr[1]][curr[0]] == ".":
                board[curr[1]][curr[0]] = "#"
                for i in [(0,1),(1,0),(-1,0),(0,-1)]: 
                        xn = curr[0]+i[0]
                        yn = curr[1]+i[1]
                        if xn >= 0 and yn >= 0 and yn < len(board) and xn < len(board[0]):
                            if board[yn][xn] == ".":
                                q.put((xn,yn))
    print("setting up the map")
    maxx = getmaxsize(input)[0]
    maxy = getmaxsize(input)[1]
    board = [["." for x in range(maxx//2 +1)] for i in range(maxy//2+1)]
    pos = (0,0)
    print("start diggig")
    for l in input:
        pos = digtrench(l, board, pos)


    board = [y[len(y)//2+int(len(y)%2):len(y)]+y[0:len(y)//2] for y in board]
    board = board[len(board)//4+ int(len(board)%2):len(board)]+board[0:len(board)//4]
    floodfill(board)
    #print(board)
    AoCparse.tofile(board)
    result =0
    for y in board:
        result += y.count("#")
    print(result)
    
def pt2(input):
    def converttoDir(i):
        if i == 0:
            return "R "
        elif i == 1:
            return "D "
        elif i== 2:
            return "L "
        elif i == 3:
            return "U "
        
    def digtrench(line, board, pos):
        direction = getdirection(line.split(" ")[0])
        length = int(line.split(" ")[1])
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
        print(f"east {east}, north {north}")
        return (max(east,west), max(south,north))

    def floodfill(board):
        q = queue.SimpleQueue()
        q.put((422,356))

        while not q.empty():
            curr = q.get()
            if board[curr[1]][curr[0]] == ".":
                board[curr[1]][curr[0]] = "#"
                for i in [(0,1),(1,0),(-1,0),(0,-1)]: 
                        xn = curr[0]+i[0]
                        yn = curr[1]+i[1]
                        if xn >= 0 and yn >= 0 and yn < len(board) and xn < len(board[0]):
                            if board[yn][xn] == ".":
                                q.put((xn,yn))
    print("setting up the map")
    maxx = getmaxsize(input)[0]
    maxy = getmaxsize(input)[1]
    board = [["." for x in range(maxx//2 +1)] for i in range(maxy//2+1)]
    pos = (0,0)
    print("start diggig")
    for l in input:
        pos = digtrench(l, board, pos) 
        
    newinput = []
    for line in input:
        color = line.split(" ")[2].split("#")[1]
        direction = converttoDir(int(color[5]))
        number = int(color[0:5], 16)
        print(number)
        newinput.append(direction+str(number))
    
    
#pt1(input)
pt2(input)