import re

## Part 1
inp = open("input.txt").read()
matches = re.findall(r"(?<=mul\()(\d+),(\d+)(?=\))", inp)

part1 = sum(int(x) * int(y) for x, y in matches)
print(f"{part1=}")

## Part 2
inp = open("input.txt").read()

dos = [0] + [x.span()[1] for x in re.finditer(r"do\(\)", inp)]
donts = [x.span()[1] for x in re.finditer(r"don't\(\)", inp)] + [len(inp)]

ranges = []
for do in dos:
    for dont in donts:
        if dont > do:
            ranges.append((do, dont))
            break


def in_range(ranges, i):
    for range in ranges:
        if range[0] < i and i < range[1]:
            return True
    return False


matches = re.findall(r"(?<=mul\()(\d+),(\d+)(?=\))", inp)

part2 = 0
for mul in re.finditer(r"(?<=mul\()(\d+),(\d+)(?=\))", inp):
    if in_range(ranges, mul.span()[1]):
        part2 += int(mul.groups()[0]) * int(mul.groups()[1])

print(f"{part2=}")
