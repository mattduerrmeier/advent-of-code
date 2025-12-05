def solve_1(id_ranges: list[str], ids: list[str]) -> int:
    counter = 0
    for idx in ids:
        for ranges in id_ranges:
            start, stop = ranges.split("-")
            if int(start) < int(idx) <= int(stop):
                counter += 1
                break

    return counter

id_ranges = []
ids = []
with open("input05.txt", "r") as f:
    for line in f:
        if "-" in line:
            id_ranges.append(line)
        elif len(line) > 1:
            ids.append(line)
        else:
            continue

example_ranges = ["3-5", "10-14", "16-20", "12-18"]
example_ids = ["1", "5", "8", "11", "17", "32"]

print(solve_1(id_ranges, ids))
