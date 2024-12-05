def run(input):
    ruleslist = [i.strip() for i in input if "|" in i]
    pages = [i.strip().split(",") for i in input if "|" not in i and i]
    # print(ruleslist, pages)
    rules = parseRules(ruleslist)
    # print(rules)
    result = 0
    result2 = 0
    for i in pages:
        # print(i)
        if i[0]:
            intermidiate = testpage(i, rules)
            if intermidiate != 0:
                result += intermidiate
            else:
                # print("found violation", i, ", fixing")
                newpage = i
                while testpage(newpage, rules) == 0:
                    newpage = sortpage(newpage, rules)
                # print("fixed page is", newpage, newpage[len(newpage) // 2], result2)
                result2 += testpage(newpage, rules)
                # print(result2)

    print("result 1 is: ", result)
    print("result 2 is: ", result2)


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
    for rule in sorted(rules, key=lambda x: len(x)):
        # print("current looked at rule is", rule)
        if rule in page:
            for i in rules.get(rule):
                if i in page:
                    # print(
                    #     "found rule",
                    #     rule,i,
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
    # print("added ", page, page[(len(page) // 2)], "to result")

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

                        page.insert(page.index(rule) + 1, i)

    return page
