def solve_1(lines: list[str]) -> int:
    max_area = 0
    for i in range(len(lines)):
        x1, y1 = map(int, lines[i].split(","))
        for j in range(i+1, len(lines)):
            x2, y2 = map(int, lines[j].split(","))
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

            if area > max_area:
                max_area = area

    return max_area

def solve_2(lines: list[str]) -> int:
    green_tiles = []
    for i in range(len(lines)):
        x1, y1 = map(int, lines[i].split(","))
        green_tiles.append((x1, y1))

    max_area = 0
    for i in range(len(lines)):
        x1, y1 = map(int, lines[i].split(","))
        for j in range(i+1, len(lines)):
            x2, y2 = map(int, lines[j].split(","))
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

            if area > max_area:
                is_valid = True
                x1, x2, y1, y2 = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
                for i in range(len(green_tiles)):
                    a, b = green_tiles[i]
                    c, d = green_tiles[(i+1) % len(green_tiles)]

                    a1, c2 = min(a, c), max(a, c)
                    b1, d2 = min(b, d), max(b, d)
                    if a1 < x2 and b1 < y2 and c2 > x1 and d2 > y1:
                        is_valid = False
                        break

                if is_valid:
                    max_area = area

    return(max_area)



with open("input09.txt", "r") as f:
    lines = f.read().rstrip().split("\n")

example = ["7,1", "11,1", "11,7", "9,7", "9,5", "2,5", "2,3", "7,3"]
print("Answer 1: ", solve_1(lines))
print("Answer 2: ", solve_2(lines))
