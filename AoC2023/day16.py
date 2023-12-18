import AoCparse
import queue

def generateboard(input):
    # board[y][x] = [char, energized]
    board = [[[input[y][x], 0] for x in range(len(input[y]))] for y in range(len(input))]
    print(board)
    return board

right = (1,0)
left= (-1,0)
up = (0,-1)
down = (0,1)
# gets the next direction on the field
def getnextfield(board,x,y, direction):
    if board[y][x][0]==".":
        return [direction]
    elif board[y][x][0]== "|":
        if direction == right or direction == left:
            return [up,down]
        else: 
            return [direction]
    elif board[y][x][0]== "-":
        if (direction == up) or (direction == down):
            return [left, right]
        else: 
            return [direction]
    elif board[y][x][0]=="/":
        if direction == left:
            return [down]
        if direction == down:
            return [left]
        if direction == right:
            return [up]
        if direction == up:
            return [right]
    elif board[y][x][0] == "\\":
        if direction == left:
            return [up]
        if direction == down:
            return [right]
        if direction == right:
            return [down]
        if direction == up:
            return [left]
    return [direction]
    

def shootbeam(board, startingpoint):
    # startingpoint is (x,y, (direction of the beam))
    q = queue.SimpleQueue()
    q.put(startingpoint)
    while not q.empty(): 
        current = q.get()
        board[current[1]][current[0]][1] += 1
        xnew= current[0]+current[2][0]
        ynew= current[1]+current[2][1]
        if xnew < len(board[0]) and xnew >= 0 and ynew < len(board)and ynew >= 0 and board[ynew][xnew][1] < 100:
            directions = getnextfield(board, xnew, ynew, current[2])
            if len(directions) >1:
                for d in directions:
                    newpoint = (xnew, ynew, d)
                    q.put(newpoint)
            else:
                newpoint = (xnew, ynew, directions[0])
                q.put(newpoint)
        
def getenergized(board):
    result = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x][1] > 0:
                result +=1
                board[y][x][1] = 0
    return result 
    
    
input = AoCparse.getinput(16)
board = generateboard(input)
startingpoint = (0,0, right)
shootbeam(board, startingpoint)
result = 0
for y in range(len(board)):
    for x in range(len(board[y])):
        if board[y][x][1] > 0:
            result +=1

startingpoints =[]           
print(f"pt1 {result}")
for i in range(len(input)):
    startingpoints.append((0,i, right))
    startingpoints.append((len(input)-1,i, left))
for i in range(len(input[0])):
    startingpoints.append((i,len(input[0])-1, up))
    startingpoints.append((i,0, down))
results =[]
for s in startingpoints:
    shootbeam(board, s)
    results.append(getenergized(board))
    print(results[-1])

print(f"pt 2 {max(results)}")