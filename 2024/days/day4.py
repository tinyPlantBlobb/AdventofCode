def run(input):
    removedinput = []
    result = 0
    for y in range(1, len(input) - 1):
        for x in range(1, len(input[y]) - 1):
            if x != 0 and x != len(input[y]) - 1 and y != 0 and y != len(input) - 1:
                if input[y][x] == "X":
                    # ignore left side
                    if checkaround(input, x, y, "M"):
                        removedinput.append((x, y))

                elif input[y][x] == "M":
                    if checkaround(input, x, y, "A"):
                        removedinput.append((x, y))
                elif input[y][x] == "A":
                    if checkaround(input, x, y, "S"):
                        removedinput.append((x, y))
                elif input[y][x] == "S":
                    result += 1
    print(result)
    print(removedinput)


def checkaround(input, x, y, nextchar):
    if (
        input[y - 1][x] == nextchar
        or input[y - 1][x - 1] == nextchar
        or input[y - 1][x + 1] == nextchar
        or input[y][x - 1] == nextchar
        or input[y][x + 1] == nextchar
        or input[y + 1][x] == nextchar
        or input[y + 1][x - 1] == nextchar
        or input[y + 1][x + 1] == nextchar
    ):
        return True
    return False
