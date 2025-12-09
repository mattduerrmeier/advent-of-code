def solve_1(lines: list[str]) -> int:
    max_area = 0
    for i in range(len(lines)):
        x1, y1 = lines[i].split(",")
        x1, y1 = int(x1), int(y1)
        for j in range(i+1, len(lines)):
            x2, y2 = lines[j].split(",")
            x2, y2 = int(x2), int(y2)
            x = abs(x1 - x2) + 1
            y = abs(y1 - y2) + 1
            area = x*y

            if area > max_area:
                max_area = area

    return max_area

with open("input09.txt", "r") as f:
    lines = f.read().rstrip().split("\n")

example = ["7,1", "11,1", "11,7", "9,7", "9,5", "2,5", "2,3", "7,3"]
print(solve_1(lines))
