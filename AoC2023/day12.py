import AoCparse

def getsolutions(line, numbers):
    return 0


input = AoCparse.getinput(12)
result = 0
for l in input:
    sysmbols = l.split(" ")[0]
    numbers = map(int, l.split(" ")[1].split(","))
    result +=getsolutions(sysmbols, numbers)