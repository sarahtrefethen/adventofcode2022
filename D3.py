
types = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def part1():
    with open("D3input.txt", 'r') as input:
        line = input.readline()
        total = 0
        while line != '':
            second_compartment = line[int(len(line)/2):len(line)]
            for char in line:
                if second_compartment.find(char) > -1:
                    total += types.find(char)
                    break
            line = input.readline()
        print(total)

def part2():
    with open("D3input.txt", 'r') as input:
        line1 = input.readline()
        line2 = input.readline()
        line3 = input.readline()
        total = 0
        while line1 != '':
            for char in line1:
                if line2.find(char) > -1:
                    if line3.find(char) > -1:
                        total += types.find(char)
                        break
            line1 = input.readline()
            line2 = input.readline()
            line3 = input.readline()
        print(total)   
