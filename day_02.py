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

def solve_2(lines: list[str]) -> int:
    counter = 0
    for line in lines:
        first, last = line.split("-")
        for idx in range(int(first), int(last) + 1):
            string_id, pattern = str(idx), ""
            for x in string_id:
                pattern += x
                repeat = (len(string_id) // len(pattern))
                if repeat == 1:
                    continue

                sub_str = pattern * repeat
                if sub_str == string_id:
                    counter += idx
                    break

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
    "565653-565659",
    "824824821-824824827",
    "2121212118-2121212124",
]

print("Answer 1:", solve_1(lines))
print("Answer 2:", solve_2(lines))
