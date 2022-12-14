from functools import cmp_to_key

def compare_items(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l == r:
            return 0
        else:
            return 1 if l < r else -1   
    if isinstance(l, list) and isinstance(r, list):
        return compare_lists(l, r)
    elif isinstance(l, int):
        return compare_lists([l], r)
    elif isinstance(r, int):
        return compare_lists(l, [r])
        

def compare_lists(left, right):
    if left == right:
        return 0
    elif left == []:
        return 1
    elif right == []:
        return -1

    response = 0
    idx = 0
    while response == 0:
        if idx == len(left) == len(right):
            return 0
        if idx == len(left):
            return 1
        if idx == len(right):
            return -1
        response = compare_items(left[idx], right[idx])
        idx += 1

    return response


def part1():
    with open("D13input.txt") as input:
        text = input.read()
        pairs = [(eval(x), eval(y)) for [x, y] in [pair.split('\n') for pair in text.split('\n\n')]]

    sum = 0
    for index, (left, right) in enumerate(pairs):
        if compare_lists(left, right) == 1:
            sum += index+1

    print(sum)

def part2():
    with open("D13input.txt") as input:
        text = input.read()
        lines = [eval(line) for pair in text.split('\n\n') for line in pair.split('\n') ] + [[[2]], [[6]]]

    compare_key = cmp_to_key(compare_lists)
    in_order = sorted(lines, key = compare_key, reverse = True)

    print((in_order.index([[2]]) + 1) * (in_order.index([[6]]) + 1))