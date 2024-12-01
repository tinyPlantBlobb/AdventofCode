print("Day 1 of Advent of Code!")


def run(input):
    lists = [i.split("   ") for i in input]
    list1 = sorted([int(i[0]) for i in lists])
    list2 = sorted([int(i[1]) for i in lists])
    result = sum(list(map(lambda x: abs(x[0] - x[1]), zip(list1, list2))))
    print(result)
