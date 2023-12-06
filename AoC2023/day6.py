import AoCparse
#import primefac
import re

inp = AoCparse.getinput(6)
def pt1(inp):
    time = list(map(int, inp[0].split(":")[1].strip().split("   ")))
    print(time)
    distance = list(map(int, inp[1].split(":")[1].strip().split("   ")))
    print(distance)
    nbr=[]
    result = 1
    for i in range(len(time)):
        nbr =[]
        print(f"{time[i]}, {distance[i]}")
        for n in range(time[i]):
            if (time[i]-n)*n > distance[i]:
                nbr.append(n)
            print(nbr)
        result *= len(nbr)
        print(result)
        
def pt2(inp):
    step = 10000
    time = int(inp[0].split(":")[1].strip().replace(" ", ''))
    print(time)
    distance = int(inp[1].split(":")[1].strip().replace(" ", ''))
    print(distance)
    nbr=0
    result = 1
    n = 9651138
    while n <= time:
        if (time-n)*n > distance and (time-(n+step))*(n+step)> distance:
            nbr+=step
            n = n+step
        else:
            if (time-n)*n > distance:
                nbr+=1
            n+=1
        
        result = nbr
        print(f"{result}, n = {n}")
    print(result)
pt1(inp)
pt2(inp)
print("iii")