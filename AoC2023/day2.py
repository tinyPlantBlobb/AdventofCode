import AoCparse

def ispossible(set):
    blue = 0
    green = 0
    red = 0
    for single in set:
        print(single)
        colors = single.split(",")
        for c in colors:
            l = c.split(' ')
            if("blue" in l[2]):
                blue= max(blue, int(l[1]))
            if("red" in l[2]):
                red= max(red, int(l[1]))
            if("green" in l[2]):
                green= max(green, int(l[1]))
    print(str(blue)+", "+ str(red) + "; " + str(green))
    print(blue*green*red)
    return (red<=12 and blue <= 14 and green<=13)


def pt2(set):
    blue = 0
    green = 0
    red = 0
    for single in set:
        print(single)
        colors = single.split(",")
        for c in colors:
            l = c.split(' ')
            if("blue" in l[2]):
                blue= max(blue, int(l[1]))
            if("red" in l[2]):
                red= max(red, int(l[1]))
            if("green" in l[2]):
                green= max(green, int(l[1]))
    print(str(blue)+", "+ str(red) + "; " + str(green))
    print(blue*green*red)
    return red*blue*green

games = AoCparse.getinput(2)
sets = []
result1 = 0
result2 = 0
for game in games:
    game = game.split(":")
    sets = game[1].split(";")
    if(ispossible(sets)):
        print(int(game[0].split(' ')[1]))
        result1 += int(game[0].split(' ')[1])
    result2 += pt2(sets)
print(result1)
print(result2)
