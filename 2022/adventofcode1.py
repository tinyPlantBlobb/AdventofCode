f = open("D:\Code\\advent of code\\adventofcode1.txt", "r")
t = f.readlines()
print(t)
maxim = 0
i = 0
o = 0
li = [0, 0]
for l in t:
    if l is "\n":
        maxim = max(maxim, i)
        li.append(i)
        i = 0

    else:
        i += int(l)

max(maxim, i)
li.sort()
print(li)
f.close()
