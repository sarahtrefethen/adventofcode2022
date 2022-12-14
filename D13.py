

with open("D13input.txt") as input:
    text = input.read()
    pairs = [(eval(x), eval(y)) for [x, y] in [pair.split('\n') for pair in text.split('\n\n')]]

def compare_items(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l == r:
            return "continue"
        else:
            return "yes" if l < r else "no"    
    if isinstance(l, list) and isinstance(r, list):
        return compare_lists(l, r)
    elif isinstance(l, int):
        return compare_lists([l], r)
    elif isinstance(r, int):
        return compare_lists(l, [r])
        

def compare_lists(left, right):
    if left == right:
        return 'continue'
    elif left == []:
        return 'yes'
    elif right == []:
        return 'no'


    response = "continue"
    idx = 0
    while response == "continue":

        if idx == len(left) == len(right):
            return 'continue'
        if idx == len(left):
            return 'yes'
        if idx == len(right):
            return 'no'
        response = compare_items(left[idx], right[idx])
        idx += 1

    return response


sum = 0
for index, (left, right) in enumerate(pairs):
    print(left)
    print(right)
    if compare_lists(left, right) == 'yes':
        sum += index+1
        print(f'{index+1} is in the right order')
    else:
        print(f'{index+1} is not in the right order')

print(sum)