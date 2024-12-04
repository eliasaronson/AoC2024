import re

import numpy as np

page = np.genfromtxt("test.txt", delimiter=1, dtype=str)

n_xmas = 0

for row in page:
    line = "".join(row)
    n_xmas += len(re.findall("XMAS", line))
    n_xmas += len(re.findall("SAMX", line))

for col in page.T:
    line = "".join(col)
    n_xmas += len(re.findall("XMAS", line))
    n_xmas += len(re.findall("SAMX", line))

h, w = page.shape
for i in range(-h + 1, w):
    diag = np.diagonal(page, offset=i)
    line = "".join(diag)
    n_xmas += len(re.findall("XMAS", line))
    n_xmas += len(re.findall("SAMX", line))

flipped = np.fliplr(page)
for i in range(-h + 1, w):
    diag = np.diagonal(flipped, offset=i)
    line = "".join(diag)
    n_xmas += len(re.findall("XMAS", line))
    n_xmas += len(re.findall("SAMX", line))

print(f"{n_xmas=}")


##

mas_pos = []

h, w = page.shape
for i in range(-h + 1, w):
    diag = np.diagonal(page, offset=i)
    line = "".join(diag)
    matches = re.finditer("MAS", line)
    for match in matches:
        mas_pos.append((i + 1, match.start() + 1))

    matches = re.finditer("SAM", line)
    for match in matches:
        mas_pos.append((i - 1, match.start() - 1))

flipped = np.fliplr(page)
for i in range(-h + 1, w):
    diag = np.diagonal(flipped, offset=i)
    line = "".join(diag)
    matches = re.finditer("MAS", line)
    for match in matches:
        mas_pos.append((i + 1, match.start() + 1))

    matches = re.finditer("SAM", line)
    for match in matches:
        mas_pos.append((i - 1, match.start() - 1))

n_xmas = 0

for idx1, mas1 in enumerate(mas_pos):
    for idx2, mas2 in enumerate(mas_pos):
        if idx1 == idx2:
            continue
        if mas1 == mas2:
            n_xmas += 1

print(f"{n_xmas=}")


print(mas_pos)
