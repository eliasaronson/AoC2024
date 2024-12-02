import collections

import numpy as np

## Part 1
inp = np.genfromtxt("input.txt", delimiter="   ")
dist = np.abs(inp[np.argsort(inp[:, 0]), 0] - inp[np.argsort(inp[:, 1]), 1])

print(np.sum(dist))

## Part 2
counter = collections.Counter(inp[:, 1])

score = 0
for e in inp[:, 0]:
    score += e * counter[e]

print(score)
