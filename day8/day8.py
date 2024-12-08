import numpy as np


def check_bound(p, map):
    return 0 <= p[0] and p[0] < map.shape[0] and 0 <= p[1] and p[1] < map.shape[1]


map = np.genfromtxt("input.txt", delimiter=1, dtype="U1", comments=None)

## Part 1
antinodes = set()
for freq in np.unique(map):
    if freq == ".":
        continue

    positions = np.array(np.where(map == freq))

    for pos1 in positions.T:
        for pos2 in positions.T:
            if np.all(pos1 == pos2):
                continue

            diff = pos1 - pos2

            p1 = pos1 + diff
            if check_bound(p1, map):
                antinodes.add(tuple(p1))

            p2 = pos2 - diff
            if check_bound(p2, map):
                antinodes.add(tuple(p2))

print("Part 1:", len(antinodes))

## Part 2
antinodes = set()
for freq in np.unique(map):
    if freq == ".":
        continue

    positions = np.array(np.where(map == freq))
    if 1 < positions.shape[1]:
        for pos1 in positions.T:
            antinodes.add(tuple(pos1))

    for pos1 in positions.T:
        for pos2 in positions.T:
            if np.all(pos1 == pos2):
                continue

            diff = pos1 - pos2

            p1 = pos1
            while check_bound(p1 := p1 + diff, map):
                antinodes.add(tuple(p1))

            p2 = pos2
            if check_bound(p2 := p2 - diff, map):
                antinodes.add(tuple(p2))

print("Part 2:", len(antinodes))
