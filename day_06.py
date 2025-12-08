import math

def solve_1(lines: list[str]) -> int:
    answers: list[int] = []
    acc: list[str] = [""] * len(lines)

    for i in range(len(lines[0])):
        chars = [""] * len(lines)
        for j in range(len(lines)):
            chars[j] = lines[j][i]
            if chars[j] != " ":
                acc[j] += chars[j]

        if all([c == " " for c in chars]) or i == len(lines[0])-1:
            values = [int(val) for val in acc if val not in ["*", "+"]]
            operator = acc[-1]
            if operator == "*":
                result = math.prod(values)
            elif operator == "+":
                result = sum(values)

            answers.append(result)
            acc = [""] * len(lines)

    return sum(answers)

def solve_2(lines: list[str]) -> int:
    answers: list[int] = []
    acc: list[str] = [""] * len(lines)

    for i in range(len(lines[0])):
        chars = [""] * len(lines)
        for j in range(len(lines)):
            chars[j] = lines[j][i]
            acc[j] += chars[j]

        if all([c == " " for c in chars]) or i == len(lines[0])-1:
            operator = acc[-1].rstrip()
            values = acc[:-1]

            num_values = max([len(c.rstrip()) for c in values])
            re_order: list[int] = [0] * num_values
            for x in range(num_values):
                val = ""
                for y in range(len(values)):
                    val += values[y][x]

                re_order[x] = int(val)

            result: int = 0
            if operator == "*":
                result = math.prod(re_order)
            elif operator == "+":
                result = sum(re_order)

            answers.append(result)
            acc = [""] * len(lines)

    return sum(answers)



with open("input06.txt", "r") as f:
    lines = f.read().rstrip("\n").split("\n")

example = [
    "123 328  51 64 ",
    " 45 64  387 23 ",
    "  6 98  215 314",
    "*   +   *   +  ",
]

print("Answer 1:", solve_1(lines))
print("Answer 2:", solve_2(lines))
