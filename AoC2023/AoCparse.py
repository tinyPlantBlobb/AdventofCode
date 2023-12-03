
def getinput(day):
    baselp = "C:\\Users\\isabe\\Code\\AdventofCode\\AoC2023"
    basetw="D:\Code\\advent of code\\AoC2023"
    path = basetw + "\\input-Day" + str(day)+ ".txt"
    f = open(path, "r")
    t = [l.strip() for l in f.readlines()]
    return t