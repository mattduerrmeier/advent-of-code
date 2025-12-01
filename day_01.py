def solve_1(lines: list[str], dial: int = 50) -> int:
    counter = 0
    for line in lines:
        op, val = line[0], int(line[1:])
        dial = (dial + (val if op == "R" else -val)) % 100
        if dial == 0:
            counter += 1

    return counter

def solve_2(lines: list[str], dial: int = 50) -> int:
    counter = 0
    for line in lines:
        op, val = line[0], int(line[1:])
        for i in range(val):
            dial = (dial + (1 if op == "R" else -1)) % 100
            counter += 1 if dial == 0 else 0

    return counter


with open("input.txt", "r") as f:
    lines = f.readlines()

example = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

print("Answer 1:", solve_1(lines))
print("Answer 2:", solve_2(lines))
