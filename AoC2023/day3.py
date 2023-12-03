import AoCparse
import re
from string import punctuation

def addat(li, str, index):
    li[index:index]= [str]
    return li

input = AoCparse.getinput(3)
print(input)
i = 0
j=0
specialchar= "[!\"#$%&'()*+,-\\/:;<=>?@[\]^_`{|}~]"
for l in input:
    characterindex = re.findall(specialchar,l)
    l = l.split(punctuation)
    print(l)
    j=0
    for k in l:
        if len(str(k)) > 1:
            for o in range(len(str(k))):
                addat(l, k, j)
            j+=(len(k)-1)

        j+=1
    i+=1
    #print(characterindex)
    #print(sep)
print(input)

