def solve_1(lines: str, verbose: bool = False) -> int:
    counter = 0
    padding = "." * len(lines[0])
    for i in range(len(lines)):
        if i == 0:
            chunk = [padding] + lines[i:i+2]
        elif i == len(lines) - 1:
            chunk = lines[i-1:i+1] + [padding]
        else:
            chunk = lines[i-1:i+2]

        assert(len(chunk)) == 3

        chunk  = ["." + ex + "." for ex in chunk]
        start, stop = 0, 3
        while stop <= len(chunk[0]):
            w_above, w, w_below = chunk[0][start:stop], chunk[1][start:stop], chunk[2][start:stop]
            if w[1] == "@":
                at_count = w_above.count("@") + ((w[0] + w[2]).count("@")) + w_below.count("@")
                if at_count < 4:
                    counter += 1
                    if verbose:
                        print("x", end="")
                else:
                    if verbose:
                        print("@", end="")
            else:
                if verbose:
                    print(".", end="")

            start +=1
            stop += 1

        if verbose:
            print()

    return counter


with open("input04.txt", "r") as f:
    lines = f.read().rstrip().split("\n")

example = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@.",
]

print("Answer 1:", solve_1(lines, verbose=False))
