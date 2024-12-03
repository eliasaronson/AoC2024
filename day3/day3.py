import re

## Part 1
inp = open("input.txt").read()
matches = re.findall(r"(?<=mul\()(\d+),(\d+)(?=\))", inp)

part1 = sum(int(x) * int(y) for x, y in matches)
print(f"{part1=}")

## Part 2
inp = open("input.txt").read()
matches = re.findall(r"(?<=mul\()(\d+),(\d+)(?=\))", inp)

part1 = sum(int(x) * int(y) for x, y in matches)
print(f"{part1=}")
