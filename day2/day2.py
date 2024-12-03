from collections import Counter

import numpy as np

## Part 1
inp = open("input.txt")

n_safe = 0
for line in inp.readlines():
    levels = np.array(line.split(" "), dtype=np.int32)

    diff = np.diff(levels)
    sign = np.sign(diff)

    # Not monotonic
    if np.abs(np.sum(sign)) != np.int32(sign.shape[0]):
        continue

    # Out of range
    if np.any(np.abs(diff) > 3) or np.any(np.abs(diff) < 1):
        continue

    n_safe += 1

print(n_safe)


## Part 2
inp = open("input.txt")


def check_monotonic(levels):
    diff = np.diff(levels)
    sign = np.sign(diff)

    # Not monotonic
    if np.abs(np.sum(sign)) != np.int32(sign.shape[0]):
        return False, np.where(sign != Counter(sign).most_common()[0][0])

    return True, -1


def check_monotonics(levels):
    monotonic, offending = check_monotonic(levels)
    if monotonic:
        return True, levels, True

    for i in range(levels.shape[0]):
        dlevels = np.delete(levels, i)
        if check_monotonic(dlevels)[0]:
            return True, dlevels, False

    return False, np.array([-1]), False


def check_oof(levels, directly):
    diff = np.diff(levels)
    if np.any(np.abs(diff) > 3) or np.any(np.abs(diff) < 1):
        if not directly:
            return True

        diff = np.diff(levels[1:])
        if not (np.any(np.abs(diff) > 3) or np.any(np.abs(diff) < 1)):
            return False
        diff = np.diff(levels[:-1])
        if not (np.any(np.abs(diff) > 3) or np.any(np.abs(diff) < 1)):
            return False
        return True
    return False


n_safe = 1
for line in inp.readlines():
    levels = np.array(line.split(" "), dtype=np.int32)

    # Not monotonic
    monotonic, levels, directly = check_monotonics(levels)
    if not monotonic:
        continue

    if check_oof(levels, directly):
        continue

    n_safe += 1

print(n_safe)
