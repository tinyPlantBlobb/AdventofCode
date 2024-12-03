import re
from operator import mul


def run(input):
    multiplications = list(
        map(lambda x: re.findall(r"mul\(\d{1,3},\d{1,3}\)", x.strip()), input)
    )
    print(multiplications)
    print()
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
