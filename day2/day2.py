import numpy as np

inp = np.genfromtxt("test.txt", delimiter=" ")

diff = np.diff(inp, axis=1)
max = np.any(np.abs(diff) > 3, axis=1)
min = np.any(np.abs(diff) < 1, axis=1)
in_bounds = np.logical_or(max, min)

sign = np.sign(diff)
