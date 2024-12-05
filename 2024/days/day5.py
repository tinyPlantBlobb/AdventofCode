def run(input):
    ruleslist = [i.strip() for i in input if "|" in i]
    pages = [i.strip().split(",") for i in input if "|" not in i and i]
    # print(ruleslist, pages)
    rules = parseRules(ruleslist)

    result = 0
    for i in pages:
        if i[0]:
            intermidiate = testpage(i, rules)
            if intermidiate != 0:
                result += intermidiate
            else:
                print("found violation, fixing")
                newpage = sortpage(i, rules)
                if testpage(newpage, rules) != 0:
                    result += testpage(newpage, rules)
                else:
                    print("could not fix")

    print("result 1 is: ", result)


def parseRules(ruleslist):
    rules = {}
    for rule in ruleslist:
        rule = rule.split("|")
        if rule[0] not in rules:
            rules.update({rule[0]: [rule[1]]})
        else:
            rules.get(rule[0], []).append(rule[1])

    return dict(sorted(rules.items()))


def testpage(page, rules):
    result = 0
    # print(page)
    for rule in rules:
        # print("current looked at rule is", rule)
        if rule in page:
            for i in rules.get(rule):
                if i in page:
                    # print(
                    #     "found rule",
                    #     i,
                    #     "with index",
                    #     page.index(i),
                    #     "and rule index",
                    #     page.index(rule),
                    # )
                    if page.index(i) > page.index(rule):
                        continue
                    else:
                        # print("found violation")
                        return 0
    # print("added ", len(page) // 2, page[(len(page) // 2) + 1], "to result")

    result += int(page[(len(page) // 2)])
    return result


def sortpage(page, rules):
    for rule in rules:
        if rule in page:
            for i in rules.get(rule):
                if i in page:
                    if page.index(i) > page.index(rule):
                        continue
                    else:
                        # print("found violation")
                        page.remove(i)
                        page.append(i)
                        return page
    return page
