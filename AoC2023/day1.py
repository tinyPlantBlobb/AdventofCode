import AoC2023.AoCparse
import re

input = AoCparse.getinput(1)
result = 0
for s in input:
        nbrs=re.findAll("\d",s)
        line = ""+nbrs[0] + nbrs[-1]
        result += int(line)