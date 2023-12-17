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
                    return min(y[0], mirrorv)
                print(f"{area[i]} and {area[y[0]-(len(area)-i)]} in {i} and {y[0]-(len(area)-i)}")
                print(f"mirror at {mirrorv} in line {y[0]}")
    for x in enumerate(area[0]):
        for i in range(x[0], len(area)):
            if x[0]-(len(area[0])-i) < 0:
                break
            if area[x[0]-(len(area)-i)] == area[i]:
                if checkotherlines(area, x[0]): 
                    return min(x[0], mirrorh)
                print(f"{area[i]} and {area[x[0]-(len(area)-i)]} in {i} and {x[0]-(len(area)-i)}")
                print(f"mirror at {mirrorh} in line {x[0]}")
    return mirrorh


def checkotherlines(area, index):
    if index > len(area)/2:
        for i in range(0,len(area) -index ,1):
            if area[index +i] != area[index-1-i]:
                return False
    else:
        for i in range(0, index, 1):
            if area[index +1+i] != area[index-i]:
                return False
    return True
            
            
    return True

areas= [list(g) for k, g in groupby(input, key=bool) if k]
result = 0
for part in areas:
    result += findmirror(part)
    print(f"area done result = {result}")

print(f"result pt1 : {result}")
    