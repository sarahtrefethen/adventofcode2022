

def contains (pair: str):
    [p1_start, p1_end, p2_start, p2_end] = [int(plot) for plots in pair.split(",") for plot in plots.split('-')]
    if p1_start <= p2_start and p1_end >= p2_end:
        return 1
    elif p1_start >= p2_start and p1_end <= p2_end:
        return 1
    else:
        return 0

def overlaps (pair: str):
    [p1_start, p1_end, p2_start, p2_end] = [int(plot) for plots in pair.split(",") for plot in plots.split('-')]
    if p1_start <= p2_start and p1_end >= p2_start:
        return 1
    elif p1_start >= p2_start and p1_start <= p2_end:
        return 1
    else:
        return 0


with open("D4input.txt", 'r') as input:
    pairs = input.read().split('\n')
    print("part1:", sum([contains(pair) for pair in pairs]))    
    print("part2:", sum([overlaps(pair) for pair in pairs]))    