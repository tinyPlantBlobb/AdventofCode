from itertools import pairwise


def run(input):
    reports = [x.strip().split(" ") for x in input]
    result = [testlevel(report) for report in reports]
    result2 = [testlevelwithoutone(report) for report in reports]
    print(sum(result))
    print(sum(result2 or result))


def testlevel(report):
    levels = [int(i) for i in report]
    return all([abs(x - y) <= 3 and abs(x - y) > 0 for x, y in pairwise(levels)]) and (
        all([x < y for x, y in pairwise(levels)])
        or all([x > y for x, y in pairwise(levels)])
    )


def testlevelwithoutone(report):
    level = [int(i) for i in report]
    levles = [level[:i] + level[i + 1 :] for i in range(len(level))]

    res = [
        all([abs(x - y) <= 3 and abs(x - y) > 0 for x, y in pairwise(j)])
        and (
            all([x < y for x, y in pairwise(j)]) or all([x > y for x, y in pairwise(j)])
        )
        for j in [level[:i] + level[i + 1 :] for i in range(len(level))]
    ]
    return any(res)
