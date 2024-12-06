def run(input):
    field = [[x for x in y.strip()] for y in input]
    guardpos = [
        (x, y)
        for y in range(len(input))
        for x in range(len(input[y]))
        if input[y][x] in "^v<>"
    ][0]
    # printfield(field)
    print("-------------------")
    guards = (guardpos, translate_direction(input[guardpos[1]][guardpos[0]]))
    obstacles = get_obstacles(input)
    print(guards)
    for i in range(1, 200000):
        obstacle = get_next_obstacle_in_direction(
            obstacles, guards[0][0], guards[0][1], guards[1]
        )
        if obstacle is None or obstacle[0] > len(field[0]):
            markfields(
                field, guards[0][0], guards[0][1], len(field[0]) - 1, guards[0][1]
            )
            break
        if obstacle[1] > len(field):
            markfields(
                field,
                guards[0][0],
                guards[0][1],
                guards[0][0],
                len(field) - 1,
            )
            break
        if obstacle[0] < 0:
            markfields(field, guards[0][0], guards[0][1], 0, guards[0][1])
            break
        if obstacle[1] < 0:
            markfields(
                field,
                guards[0][0],
                guards[0][1],
                guards[0][0],
                0,
            )

            break
        field = markfields(
            field,
            guards[0][0],
            guards[0][1],
            obstacle[0] - guards[1][0],
            obstacle[1] - guards[1][1],
        )
        guards = moveguard(guards, obstacle)
        # printfield(field)

    printfield(field)
    # print(guards, obstacles)


def get_obstacles(input):
    # obsacles = [(-1, y) for y in range(len(input))]
    # obsacles += [(len(input[0]), y) for y in range(len(input))]
    # obsacles += [(x, -1) for x in range(len(input[0]))]
    # obsacles += [(x, len(input)) for x in range(len(input[0]))]
    res = [
        (int(x), int(y))
        for y in range(len(input))
        for x in range(len(input[y]))
        if input[y][x] == "#"
    ]
    return res


def get_next_obstacle_in_direction(obstacles, x, y, direction):
    if direction[0] == (0, 1):
        obstacles = sorted(obstacles, key=lambda x: x[0], reverse=False)
    elif direction[0] == (0, -1):
        obstacles = sorted(obstacles, key=lambda x: x[0], reverse=True)
    elif direction[0] == (1, 0):
        obstacles = sorted(obstacles, key=lambda x: x[1], reverse=False)
    elif direction[0] == (-1, 0):
        obstacles = sorted(obstacles, key=lambda x: x[1], reverse=True)
    # print(obstacles)
    for i in obstacles:
        if direction[0] == 0 and x == i[0]:
            if direction[1] > 0 and y < i[1]:
                # print("taken", i)
                return i

            elif direction[1] < 0 and y > i[1]:
                # print("taken", i)
                return i
        if direction[1] == 0 and y == i[1]:
            if direction[0] > 0 and x < i[0]:
                # print("taken", i)
                return i

            elif direction[0] < 0 and x > i[0]:
                # print("taken", i)
                return i

    if direction == (0, 1):
        return (x, 1000000000)
    elif direction == (0, -1):
        return (x, -1)
    elif direction == (1, 0):
        return (10000000000, y)
    elif direction == (-1, 0):
        return (-1, y)
    else:
        return None


def printfield(field):
    print("\n".join(map(lambda x: "".join(x), field)))
    stringified = "".join(map(lambda x: "".join(x), field))
    print(stringified.count("x") + 1)


def translate_direction(char):
    return {
        "v": (0, 1),
        "^": (0, -1),
        "<": (-1, 0),
        ">": (1, 0),
    }[char]


def markfields(map, x, y, xto, yto):
    if (
        x < 0
        or y < 0
        or x >= len(map[0])
        or y >= len(map)
        or xto < 0
        or yto < 0
        or xto >= len(map[0])
        or yto >= len(map)
    ):
        x = x % len(map[0])
        y = y % len(map)
        xto = xto % len(map[0])
        yto = yto % len(map)

    if (x, y) == (xto, yto):
        map[y][x] = "x"
    map[y][x] = "x"
    if x < xto:
        for i in range(x, xto):
            map[y][i] = "x"

    if x > xto:
        for i in range(xto, x):
            map[y][i] = "x"
    if y < yto:
        for i in range(y, yto):
            map[i][x] = "x"

    if y > yto:
        for i in range(yto, y):
            map[i][x] = "x"

    return map


def moveguard(guard, obstacle):
    # print(guard, obstacle)
    pos = (obstacle[0] - guard[1][0], obstacle[1] - guard[1][1])
    direction = guard[1]
    if guard[1] == (0, -1):
        direction = (1, 0)
    elif guard[1] == (1, 0):
        direction = (0, 1)
    elif guard[1] == (0, 1):
        direction = (-1, 0)
    elif guard[1] == (-1, 0):
        direction = (0, -1)
    # print(pos, direction)
    return (pos, direction)
