
with open("D10input.txt", 'r') as input:
    active_command = ""
    cycle = 1
    x = 1
    part1_total = 0
    screen = [["." for i in range(40)] for n in range(6)]

    while(True):
        if (cycle - 20) % 40 == 0:
            part1_total += (cycle * x)


        row = int((cycle-1) / 40)
        column = (cycle-1) % 40

        #okay clearly the control flow here could be better
        if (column - 3) < x-1 <= column and row < 6:
            screen[row][column] = "#"

        if active_command == "":
            line = input.readline()
            if line == "":
                break
            if line != "noop\n":
                active_command = line.split(" ")[1]
        else:
            x += int(active_command)
            active_command = ""

        cycle += 1

    print("part 1:", part1_total)
    [print(''.join(row)) for row in screen]

