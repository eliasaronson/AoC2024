import re

inp = open("input.txt").read()
matches = re.findall(r"(?<=mul\()(\d+),(\d+)(?=\))", inp)

part1 = sum(int(x) * int(y) for x, y in matches)
print(f"{part1=}")
