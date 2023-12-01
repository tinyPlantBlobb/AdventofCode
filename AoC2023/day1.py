import AoCparse
import re
def replace(s):
        s = s.replace("one", str(1))
        s = s.replace("two", str(2))
        s = s.replace("three", str(3))
        s = s.replace("four", str(4))
        s = s.replace("five", str(5))
        s = s.replace("six", str(6))
        s = s.replace("seven", str(7))
        s = s.replace("eight", str(8))
        s = s.replace("nine", str(9))
        return s

input = AoCparse.getinput(1)
result = 0
        
for s in input:
        t = replace(s)
        print(t)
        nbrs=re.findall("\d",t)
        line = str(nbrs[0]) + str(nbrs[-1])
        print(line)
        result += int(line)

print(result)