import math
import networkx as nx

def euclidean_dist(p1: list[int], p2: list[int]) -> float:
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5


def solve_1(lines: list[int], num_iter: int = 1000) -> int:
    distances = {}
    for idx1 in range(len(lines)):
        p1 = lines[idx1]
        for idx2 in range(idx1+1, len(lines)):
            p2 = lines[idx2]
            dist = euclidean_dist(p1, p2)
            distances[dist] = (p1, p2)

    circuits = []
    for i in range(num_iter):
        min_dist = min(distances.keys())
        min_points = distances.pop(min_dist)
        min_points = tuple(min_points[0]), tuple(min_points[1])

        circuits.append(min_points)

    acc = find_largest_comps(circuits)
    return math.prod(acc)

def find_largest_comps(circuits: list[tuple[tuple[int, int, int], tuple[int, int, int]]]) -> list[int]:
    G = nx.Graph()
    G.add_edges_from(circuits)

    comps = sorted(nx.connected_components(G), key=len, reverse=True)
    acc = [len(comps[i]) for i in range(3)]
    return acc

def solve_2(lines: list[int]) -> int:
    distances = {}
    for idx1 in range(len(lines)):
        p1 = lines[idx1]
        for idx2 in range(idx1+1, len(lines)):
            p2 = lines[idx2]
            dist = euclidean_dist(p1, p2)
            distances[dist] = (p1, p2)

    G = nx.Graph()
    G.add_nodes_from([tuple(x) for x in lines])
    last_point = (0, 0)
    while len(distances) != 0:
        min_dist = min(distances.keys())
        min_points = distances.pop(min_dist)
        p1, p2 = tuple(min_points[0]), tuple(min_points[1])
        G.add_edge(p1, p2)
        last_point = p1, p2

        if nx.is_connected(G):
            break

    return last_point


with open("input08.txt", "r") as f:
    lines = f.read().rstrip().split("\n")
    lines = [list(map(int, l.split(","))) for l in lines]

example = [
        [162,817,812],
        [57,618,57],
        [906,360,560],
        [592,479,940],
        [352,342,300],
        [466,668,158],
        [542,29,236],
        [431,825,988],
        [739,650,466],
        [52,470,668],
        [216,146,977],
        [819,987,18],
        [117,168,530],
        [805,96,715],
        [346,949,466],
        [970,615,88],
        [941,993,340],
        [862,61,35],
        [984,92,344],
        [425,690,689],
]

print("Answer 1:", solve_1(lines, 1000))
print("Answer 2:", solve_2(lines))

