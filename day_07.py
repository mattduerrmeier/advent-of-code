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

def solve_2(lines: list[list[str]]) -> int:
    split_idxs = set()
    split_idxs.add(lines[0].index("S"))

    for j in range(1, len(lines)):
        temp_split = set()
        for i in range(len(lines[0])):
            if lines[j][i] == "^" and lines[j-1][i].isdigit():
                if lines[j][i-1].isdigit():
                    lines[j][i-1] = str(int(lines[j][i-1]) + int(lines[j-1][i]))
                else:
                    lines[j][i-1] = lines[j-1][i]

                lines[j][i+1] = lines[j-1][i]

                split_idxs.remove(i)
                temp_split.add(i-1)
                temp_split.add(i+1)
            elif i in split_idxs:
                if lines[j-1][i].isdigit():
                    if lines[j][i].isdigit():
                        lines[j][i] = str(int(lines[j][i]) + int(lines[j-1][i]))
                    else:
                        lines[j][i] = lines[j-1][i]
                else:
                    lines[j][i] = str(1)

        split_idxs = split_idxs.union(temp_split)

    return(sum([int(i) for i in lines[-1] if i != "."]))


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
print("Answer 2:", solve_2(lines))
