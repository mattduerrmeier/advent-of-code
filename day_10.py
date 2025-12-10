from scipy.optimize import linprog
from itertools import combinations
import numpy as np

def solve_1(line: list[str]) -> int:
    counter = 0
    for line in lines:
        ind_idx = line.index("]")
        indicator = list(line[1:ind_idx])
        indicator = [True if ind == "#" else False for ind in indicator]

        buttons_idx = line.index("{")
        buttons = line[ind_idx+2:buttons_idx-1]
        buttons = list(eval(buttons.replace("(", "[").replace(")", "]").replace(" ", ",")))

        num_ops = None
        start = [False] * len(indicator)
        for r in range(1, len(indicator)):
            for comb in combinations(buttons, r=r):
                for t in comb:
                    for idx in t:
                        start[idx] = not start[idx]

                if start == indicator:
                    num_ops = r
                    break
                else:
                    start = [False] * len(indicator)

            if num_ops is not None:
                break

        counter += num_ops

    return counter


def solve_2(lines: list[str]) -> int:
    counter = 0
    for line in lines:
        ind_idx = line.index("]")
        buttons_idx = line.index("{")

        buttons = line[ind_idx+2:buttons_idx-1]
        buttons = list(eval(buttons.replace("(", "[").replace(")", "]").replace(" ", ",")))
        joltage = eval(line[buttons_idx:].replace("{", "[").replace("}", "]"))

        c = [1] * len(buttons)
        bounds = [(0, None)] * len(buttons)

        A_eq = []
        for row in buttons:
            l = [0] * len(joltage)
            for i in row:
                l[i] = 1
            A_eq.append(l)

        A_eq = np.array(A_eq).T
        b_eq = joltage
        res = linprog(c=c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, integrality=[1]*len(buttons))
        counter += int(res.fun)

    return counter


with open("input10.txt", "r") as f:
    lines = f.read().rstrip().split("\n")

example = [
    "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
    "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
    "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
]

print("Answer 1:", solve_1(lines))
print("Answer 2:", solve_2(lines))
