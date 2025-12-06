def solve_1(id_ranges: list[str], ids: list[str]) -> int:
    counter = 0
    for idx in ids:
        for ranges in id_ranges:
            start, stop = ranges.split("-")
            if int(start) < int(idx) <= int(stop):
                counter += 1
                break

    return counter

def solve_2(id_ranges: list[str]) -> int:
    list_ranges = []
    for ranges in id_ranges:
        start, stop = ranges.split("-")
        list_ranges.append((int(start), int(stop)))

    list_ranges = sorted(list_ranges, key=lambda x: x[0])

    final_ranges = []
    for start, stop in list_ranges:
        if final_ranges and start <= final_ranges[-1][1]:
            new_stop = max(stop, final_ranges[-1][1])
            final_ranges[-1] = (final_ranges[-1][0], new_stop)
        else:
            final_ranges.append((start, stop))

    result = sum([(stop +1 - start) for start, stop in final_ranges])
    return result


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

print("Answer 1:", solve_1(id_ranges, ids))
print("Answer 2:", solve_2(id_ranges))
