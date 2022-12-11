
import math

monkeys = [{} for i in range(8)]

def parse_monkey(index: int,raw_monkey: str):
    [starting_line, operation_line, test_line, true_line, false_line] = range(1, 6)
    lines = raw_monkey.split('\n')
    monkey = monkeys[index]

    monkey['items'] = [int(num) for num in lines[starting_line].split(": ")[1].split(",")]
    monkey['inspect'] = lines[operation_line].split("= ")[1]
    test_int = int(lines[test_line].split(" ")[-1])
    true_int = int(lines[true_line].split(" ")[-1])
    false_int = int(lines[false_line].split(" ")[-1])
    monkey['test'] = lambda item: true_int if item % test_int == 0 else false_int
    monkey['counter'] = 0

with open("D11input.txt") as input:
    monkey_index = 0
    raw_monkies = input.read().split("\n\n")
    monkies = [parse_monkey(index, monkey) for index, monkey in enumerate(raw_monkies)]
    

for n in range(20):
    for monkey in monkeys:
        for old in monkey['items']:
            monkey['counter'] += 1
            new_worry = math.floor(eval(monkey['inspect']) / 3)
            new_monkey = monkey['test'](new_worry)
            monkeys[new_monkey]['items'].append(new_worry)
        monkey['items'] = []


counters = [monkey['counter'] for monkey in monkeys]
counters.sort()
print(counters[-2] * counters[-1])