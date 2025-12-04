def solve_1(lines: list[str], verbose: bool = False) -> tuple[int, list[tuple[int, int]]]:
    to_remove = []
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
                    to_remove.append((i, start))
                    if verbose: print("x", end="")
                else:
                    if verbose: print("@", end="")
            else:
                if verbose: print(".", end="")

            start +=1
            stop += 1

        if verbose: print()

    return (counter, to_remove)

def solve_2(lines: list[str], verbose: bool = False) -> int:
    counter = 0
    while True:
        local_counter, to_remove = solve_1(lines, verbose=verbose)
        if local_counter == 0:
            break

        lines = remove_roll(lines, to_remove)
        if verbose:
            for l in lines:
                print(l)
            print()

        counter += local_counter

    return counter

def remove_roll(lines: list[str], to_remove: list[tuple[int, int]]) -> list[str]:
    new_lines = lines.copy()
    for (i, j) in to_remove:
        new_lines[i] = new_lines[i][:j] + "." + new_lines[i][j+1:]

    return new_lines


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

print("Answer 1:", solve_1(lines, verbose=False)[0])
print("Answer 2:", solve_2(lines, verbose=False))
