
def getinput(day):
    baselp = "C:\\Users\\isabe\\Code\\AdventofCode\\AoC2023"
    basetw="D:\Code\\advent of code\\AoC2023"
    path = baselp + "\\input-Day" + str(day)+ ".txt"
    f = open(path, "r")
    t = f.readlines()
    return t