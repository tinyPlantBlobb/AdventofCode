import AoCparse
import math
def predictnext(l):
    li = []
    done = False
    depth = 0
    c =0
    li.append(list(map(int, l)))
    while not done:
        n = [li[depth][i]-li[depth][i-1] for i in range(1,(len(li[depth])))]
        li.append(n)
        depth +=1
        if sum(li[depth]) == 0:
            done = True
            break
    for d in range(depth):
        c += li[d][-1]
    return c

input = AoCparse.getinput(9)
result =0
res2 = 0
for i in input:
    nextnbr =predictnext(i.strip().split(" "))
    prevnbr = predictnext(list(reversed(i.strip().split(" "))))
    result += nextnbr
    res2 +=prevnbr
    
print(result)
print(res2)