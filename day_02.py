def solve_1(lines: list[str]) -> int:
    counter = 0
    for line in lines:
        first, last = line.split("-")
        for i in range(int(first), int(last) + 1):
            idx = str(i)
            if len(idx) % 2 != 0:
                continue

            split = len(idx) // 2
            if idx[:split] == idx[split:]:
                counter += i

    return counter


with open("input-02.txt", "r") as f:
    lines = f.read().rstrip().split(",")

example = [
    "11-22",
    "95-115",
    "998-1012",
    "1188511880-1188511890",
    "222220-222224",
    "1698522-1698528",
    "446443-446449",
    "38593856-38593862",
]

print("Answer 1:", solve_1(lines))
