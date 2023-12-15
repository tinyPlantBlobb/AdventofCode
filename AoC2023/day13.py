import AoCparse
from itertools import groupby
input = AoCparse.getinput(13)

def findmirror(area):
    print(area)
    mirrorv = len(area)
    mirrorh= len(area[0])
    length = len(area)
    # find the horizontal mirror
    for y in enumerate(area):
        print(y)
        for i in range(y[0], len(area)):
            print(f"{y[0]-(len(area)-i)}")
            if y[0]-(len(area)-i) < 0:
                break
            if area[y[0]-(len(area)-i)] == area[i]:
                if checkotherlines(area, y[0]): 
                    mirrorv = min(y[0], mirrorv)
                print(f"{area[i]} and {area[y[0]-(len(area)-i)]} in {i} and {y[0]-(len(area)-i)}")
                print(f"mirror at {mirrorv} in line {y[0]}")
    return mirrorv


def checkotherlines(area, index):
    return True

areas= [list(g) for k, g in groupby(input, key=bool) if k]
result = 0
for part in areas:
    result += findmirror(part)
    print(f"area done result = {result}")

print(f"result pt1 : {result}")
    