import numpy as np

inp = np.genfromtxt("input.txt", delimiter=1, dtype="U1", comments=None)

print(inp)

##
start = np.where(inp == "^")

# x, y
pos = complex(start[1][0], start[0][0])
dir = complex(0, -1)

visits = {pos}


def in_range(map, pos):
    if (
        pos.imag >= 0
        and pos.imag < map.shape[0]
        and pos.real >= 0
        and pos.real < map.shape[1]
    ):
        return True
    return False


def to_index(pos):
    return int(pos.imag), int(pos.real)


map2 = inp.copy()
while True:
    next_pos = pos + dir
    if not in_range(inp, next_pos):
        break
    if inp[to_index(next_pos)] == "#":
        dir = dir * complex(0, 1)
    else:
        pos += dir
    map2[to_index(pos)] = "o"
    visits.add(pos)

print()
print(map2)
print("res:", len(visits))
