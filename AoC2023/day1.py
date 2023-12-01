import AoCparse
import re

input = AoCparse.getinput(1)
result = 0
for s in input:
        nbrs=re.findAll("\d",s)
        line = str(nbrs[0]) + str(nbrs[-1])
        print(line)
        result += int(line)

print(result)