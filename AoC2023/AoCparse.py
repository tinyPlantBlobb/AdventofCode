
def getinput(day):
    base = "AoC2023"
    path = base + "\\input-Day" + str(day)+ ".txt"
    f = open(path, "r")
    t = [l.strip() for l in f.readlines()]
    f.close()
    return t

def tofile(board):
    output = open("AoC2023\\output.txt", "w")
    for each in board:
        output.write("".join(each))
        output.write("\n")
    output.close()
    