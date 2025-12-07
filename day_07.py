def solve_1(lines: list[list[str]]) -> int:
    counter = 0
    split_idxs = set()
    split_idxs.add(lines[0].index("S"))

    for j in range(1, len(lines)):
        for i in range(len(lines[0])):
            if lines[j][i] == "^" and lines[j-1][i] == "|":
                lines[j][i-1] = "|"
                lines[j][i+1] = "|"

                split_idxs.remove(i)
                split_idxs.add(i-1)
                split_idxs.add(i+1)
                counter += 1
            elif i in split_idxs:
                lines[j][i] = "|"

    return counter


with open("input07.txt", "r") as f:
    lines = f.read().rstrip("\n").split("\n")


example = [
    ".......S.......",
    "...............",
    ".......^.......",
    "...............",
    "......^.^......",
    "...............",
    ".....^.^.^.....",
    "...............",
    "....^.^...^....",
    "...............",
    "...^.^...^.^...",
    "...............",
    "..^...^.....^..",
    "...............",
    ".^.^.^.^.^...^.",
    "...............",
]

example = [list(i) for i in example]
lines = [list(i) for i in lines]

print("Answer 1:", solve_1(lines))
