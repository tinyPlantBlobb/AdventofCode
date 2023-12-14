import AoCparse
# square rocks in a specific line
def getclosestprevrock(rock, squarerocks):
    print(squarerocks)
    squarerock = [i for i in squarerocks if i < rock]
    closesrock = -1
    print(squarerock)
    if not squarerock:
        closesrock = min(squarerock, key=lambda x: (abs(x - rock)))
    print(f"rock {rock}, closest rock {closesrock}, all rocks in consideration {squarerock} all rocks given {squarerocks}")
    return closesrock

def moveNorth(board, squarerocks, roundrocks):
    reslut = 0
    # got over all x values 
    for i in range(len(board)):
        allroundx = sorted(roundrocks.keys())
        allsquarex = sorted(squarerocks.keys())
        # check if i is in both the lists
        if i in allroundx and i in allsquarex:
            allroundrocks = roundrocks.pop(i)
            print(f"round {i}")
            for rock in enumerate(allroundrocks):
                closesrock = min(squarerocks.get(i), key=lambda x: (abs(x - rock[1])))
                print(f" current y {rock[1]} closest rock {closesrock}")
                # if the closest rock is after the current round one
                if closesrock > rock[1]:
                    
                    prevrocks = roundrocks.get(i, [])
                    print(f"prevrocks {prevrocks}")
                    if not prevrocks:
                        prevrocks.append(0)
                    else:
                        print(prevrocks)
                        prevrocks.append(prevrocks[-1] +1)
                    roundrocks.update({i:prevrocks})
                    print(roundrocks.get(i))
                # if the closest rock is before the current round one
                else:
                    prevrocks = roundrocks.get(i, [])
                    print(f"prevrocks {prevrocks}")
                    if not prevrocks:
                        prevrocks.append(closesrock+1)
                    else:
                        
                        print(prevrocks)
                        # if the closest previous round rock is before the colosest square rock 
                        if(prevrocks[-1]< closesrock):
                            prevrocks.append(closesrock +1)
                        else: 
                            print("get the 2. closest rock")
                            sclosesrock= getclosestprevrock(rock[1],squarerocks.get(i))
                            if sclosesrock != -1:
                                closesrock = sclosesrock
                            prevrocks.append(prevrocks[-1]+1)
                    roundrocks.update({i:prevrocks})
                    print(roundrocks.get(i))
                    print("i")
        # if there are no square rocks in a column
        elif i in allroundx and i not in allsquarex:
            l = roundrocks.pop(i)
            newl = [x for x in range(0,len(l))]
            roundrocks.update({i: newl})
    print(roundrocks)
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

input = AoCparse.getinput(14)
rocks = getsquarerocks(input)

roundrocks  = getroundrocks(input)
print(rocks)
print(roundrocks)
roundrocks = moveNorth(input, rocks, roundrocks)
result =0
for k in roundrocks.keys():
    print(k)
    print(roundrocks.get(k))
    l = roundrocks.get(k)
    values =list(map(lambda x: len(input) -x , l))
    print(f"values{values}")
    result += sum(values)

print(result)