inp = open("input.txt")
part = 2


def plus(v1, v2):
    return v1 + v2


def mul(v1, v2):
    return v1 * v2


def concat(v1, v2):
    return int(str(v1) + str(v2))


def check(target, inputs, opt, val):
    new_val = opt(val, inputs[0])
    if len(inputs) == 1:
        return new_val == target
    if new_val > target:
        return False

    if check(target, inputs[1:], plus, new_val):
        return True
    if check(target, inputs[1:], mul, new_val):
        return True
    if part == 2 and check(target, inputs[1:], concat, new_val):
        return True

    return False


def check_opt(target, inputs):
    if part == 1:
        return check(target, inputs, plus, 0) or check(target, inputs, mul, 0)
    else:
        return (
            check(target, inputs, plus, 0)
            or check(target, inputs, mul, 0)
            or check(target, inputs, concat, 0)
        )


res = 0
for line in inp.readlines():
    target, inputs = line.replace("\n", "").split(": ")
    target = int(target)
    inputs = [int(x) for x in inputs.split()]
    test = check_opt(target, inputs)

    if test:
        res += target

print(res)
