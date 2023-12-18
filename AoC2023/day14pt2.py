import AoCparse

def moveNorth(board, squarerocks, roundrocks):
    reslut = 0
    
    return roundrocks.copy()

def getsquarerocks(board):
    # defined as the x value as the key and the y value as the value in the dict
    rocks = {}
    newval = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x]== "#":
                newval = rocks.get(x, [])
                newval.append(y)
                rocks.update({x:newval})
    return rocks

def getroundrocks(board):
    rocks = {}
    inrow = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x]== "O":
                inrow = rocks.get(x, [])
                inrow.append(y)
                rocks.update({x:inrow})
    return rocks

def generateBoard(input):
    board = [[a for a in line] for line in input]
    # print(board)
    return board


input = AoCparse.getinput(14)
rocks = getsquarerocks(input)
board = generateBoard(input)
roundrocks  = getroundrocks(input)


# print(rocks)
# print(roundrocks)

roundrocks = moveNorth(board, rocks, roundrocks)
result =0

print(roundrocks)
print(result)