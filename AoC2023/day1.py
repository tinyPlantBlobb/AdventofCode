import AoCparse
import re
def replace(s):
        s = s.replace("nine", "nine"+str(9)+"nine")
        s = s.replace("eight", "eigth"+str(8)+"eight")
        s = s.replace("seven", "seven"+str(7) + "seven")
        s = s.replace("six", "six"+str(6)+ "six")
        s = s.replace("five", "five"+str(5)+"five")
        s = s.replace("four", "four"+str(4)+"four")
        s = s.replace("two", "two"+str(2)+"two")
        s = s.replace("three", "three"+str(3)+"three")
        s = s.replace("one", "one"+str(1)+"one")
        
        
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
