import re
from operator import mul


enabled = True


def run(input):
    multiplications = list(
        map(lambda x: re.findall(r"mul\(\d{1,3},\d{1,3}\)", x.strip()), input)
    )
    # print(list(map(lambda x: re.findall(r"\d{3,}", x), input)))
    # print(multiplications)
    result = sum(
        list(
            map(
                lambda y: sum(
                    list(
                        map(
                            lambda x: int(re.findall(r"\d+", x)[0])
                            * int(re.findall(r"\d+", x)[1])
                            if x
                            else 0,
                            y,
                        ),
                    )
                ),
                multiplications,
            )
        )
    )
    print(result)

    multiplicationsanddo = list(
        map(
            lambda x: [
                match
                for e in re.findall(
                    r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))", x.strip()
                )
                for match in e
                if match
            ],
            input,
        )
    )

    def enable(element):
        global enabled
        # print(element, enabled)
        if element == "do()":
            enabled = True
            return False
        elif element == "don't()":
            enabled = False
            return False
        else:
            return enabled

    removedisabled = [elem for i in multiplicationsanddo for elem in i if enable(elem)]
    # print(removedisabled)
    result2 = sum(
        list(
            map(
                lambda x: int(re.findall(r"\d+", x)[0]) * int(re.findall(r"\d+", x)[1])
                if x and re.findall(r"\d+", x) and x != "do()" and x != "don't()"
                else 0,
                removedisabled,
            )
        )
    )
    print(result2)
