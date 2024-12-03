def run(input):
    lists = [i.split("   ") for i in input]
    list1 = sorted([int(i[0]) for i in lists])
    list2 = sorted([int(i[1]) for i in lists])
    result = sum(list(map(lambda x: abs(x[0] - x[1]), zip(list1, list2))))
    print(result)
    l2mapping = {i: list2.count(i) for i in list2}
    result2 = sum(list(map(lambda x: x * l2mapping.get(x, 0), list1)))
    print(result2)
