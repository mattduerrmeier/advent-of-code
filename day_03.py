def solve_1(lines: list[str]) -> str:
    counter = 0
    for line in lines:
        max_char, max_idx = search(line)
        line_left, line_right = line[:max_idx], line[max_idx+1:]
        max_char_left, max_idx_left = search(line_left)
        max_char_right, max_idx_right = search(line_right)

        if max_idx_left is None:
            counter += int(max_char + max_char_right)
        elif max_idx_right is None:
            counter += int(max_char_left + max_char)
        else:
            left = int(max_char_left + max_char_left)
            right = int(max_char + max_char_right)
            counter += left if left > right else right

    return counter

def search(line: str) -> tuple[str, int]:
    max_char, max_idx = "0", None
    for idx, char in enumerate(line):
        if int(char) >= int(max_char):
            max_char = char
            max_idx = idx

    return (max_char, max_idx)

def solve_2(lines: list[str]) -> str:
    counter = 0
    for line in lines:
        acc = ""
        start, stop = 0, len(line) - 11
        while stop <= len(line):
            window = line[start:stop]
            max_val = max(window)
            acc += max_val
            idx = window.index(max_val)
            start += (idx + 1)
            stop += 1

        counter += int(acc)

    return counter


with open("input-03.txt", "r") as f:
    lines = f.read().rstrip().split("\n")

example = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]

print("Answer 1:", solve_1(lines))
print("Answer 1:", solve_2(lines))
