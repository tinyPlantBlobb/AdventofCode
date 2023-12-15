import AoCparse

input = AoCparse.getinput(15)

def hashchchar(prev, char):
    result = ((prev + ord(char)) *17)% 256
    return result

lines = input[0].split(",")
result = 0
for line in lines:
    temp = 0
    for c in line:
        temp = hashchchar(temp, c)
    result += temp
    
print(result)