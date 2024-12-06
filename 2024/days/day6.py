def run(input):
    guardpos = [
        (x, y)
        for y in range(len(input))
        for x in range(len(input[y]))
        if input[y][x] in "^v<>"
    ][0]
    guards = (guardpos, translate_direction(input[guardpos[1]][guardpos[0]]))
    obstacles = get_obstacles(input)
    print(guards, obstacles)


def get_obstacles(input):
    return [
        (int(x), int(y))
        for y in range(len(input))
        for x in range(len(input[y]))
        if input[y][x] == "#"
    ]


def translate_direction(char):
    return {
        "v": (0, 1),
        "^": (0, -1),
        "<": (-1, 0),
        ">": (1, 0),
    }[char]
