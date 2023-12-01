f = open("D:\Code\\advent of code\\adventofcode2.txt", "r")
t = f.readlines()
score1 = 0
newscore = 0


def evalchoice(s):

    if s == "X":  # rock
        return 1
    elif s == "Y":  # paper
        return 2
    elif s == "Z":  # scissors
        return 3
    elif s == "A":  # rock
        return 1
    elif s == "B":  # papar
        return 2
    elif s == "C":  # scissors
        return 3


def evalround(li):
    s = evalchoice(li[-1])
    o = evalchoice(li[0])
    if (s - o) == 0:
        return 3
    elif s == 1 and o == 3:
        return 6
    elif s == 1 and o == 2:
        return 0
    elif s == 3 and o == 2:
        return 6
    elif s == 2 and o == 3:
        return 0
    elif s == 2 and o == 1:
        return 6
    elif s == 3 and o == 1:
        return 0


def evalres(s):
    if s == "X":  # rock
        return 0
    elif s == "Y":  # paper
        return 6
    elif s == "Z":  # scissors
        return 3


def pick(s, w):
    if s == 1 and w == 0:
        return 3
    elif s == 2 and w == 0:
        return 1
    elif s == 3 and w == 0:
        return 2
    elif s == 1 and w == 6:
        return 2
    elif s == 2 and w == 6:
        return 3
    elif s == 3 and w == 6:
        return 1


def evalpick(rps):
    if evalres(rps[-1]) == 3:
        return evalchoice(rps[0])
    else:
        return pick(evalchoice(rps[0]), evalres(rps[-1]))


for l in t:
    rps = l.split()
    print(score1, rps, evalchoice(rps[-1]), evalround(rps))
    score1 += evalround(rps)
    score1 += evalchoice(rps[-1])
    print(score1, rps, evalres(rps[-1]), evalpick(rps))
    newscore += evalres(rps[-1])
    newscore += evalpick(rps)


print(score1)
print(newscore)
# day(x, t)
f.close()
