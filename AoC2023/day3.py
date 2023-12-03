import AoCparse
from collections import defaultdict

lines = AoCparse.getinput(3)
print(lines)

# create a mapping between each number and it's coordinate
mapping = defaultdict(str)
for ln, line in enumerate(lines):
  row = 0
  while row < len(line):
    char = line[row]
    if char.isdigit():
      num = ""
      track = []
      while row < len(line) and line[row].isdigit():
        num += line[row]
        track.append(f"{str(ln)}_{str(row)}")
        row += 1
      for t in track:
        mapping[t] = num
    row += 1
print(mapping)

p1 = 0
p2 = 0
# go over each symbol, and if a number matches, 'visit' it's mapped number
for ln, line in enumerate(lines):
  for row, char in enumerate(line):
    # check a symbol
    if char != "." and not char.isdigit():
      values = []
      for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
          obj = lines[ln + x][row + y]
          if obj.isdigit():
            position = f"{ln + x}_{row + y}"
            num = mapping[position]
            # record numbers around this symbol
            if int(num) not in values:
              values.append(int(num))
              p1 += int(num)
      # check * gear, for part 2
      if char == "*" and len(values) == 2:
        p2 += values[0] * values[1]

print("answer of part 1:" + str(p1))
print("answer of part 2:" + str(p2))
# tbh this one hurt my head too much trying to parse everything so I gave up
