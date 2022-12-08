
with open("D1input.txt", 'r') as input:
    line = input.readline()
    max = 0
    second = 0
    third = 0
    total = 0
    while line != '':
        if (line == '\n'):
            total = 0
        else:
            total += int(line)
            if total > max:
                third = second
                second = max
                max = total
            elif total > second:
                third = second
                second = total
            elif total > third:
                third = total
        line = input.readline()
    
    print(max)    
    print(max+second+third)