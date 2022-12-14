
grid = [["." for n in range(107)] for n in range(201)]

def add_to_grid(path):
    print(path)
    (start_col,start_row) = path[0]
    for n in range(1, len(path)):
        (end_col, end_row) = path[n]
        if end_col == start_col:
            if end_row > start_row:
                for i in range(start_row, end_row + 1):
                    grid[i][start_col] = "#" 
            else:
                for i in range(end_row, start_row + 1):
                    grid[i][start_col] = "#"
        if end_row == start_row:
            if start_col > end_col:
                for i in range(end_col, start_col + 1):
                    grid[start_row][i] = "#"
            if start_col < end_col:
                for i in range(start_col, end_col + 1):
                    grid[start_row][i] = "#"
        (start_col, start_row) = (end_col, end_row)   

with open("D14input.txt") as file:
    line = file.readline()
    while line != "":
        path = [(int(x)-400, int(y)) for [x,y] in [pair.split(",") for pair in line.split(" -> ")]]
        add_to_grid(path)
        line = file.readline()

def drop_sand():
    sand_row = 0
    sand_col = 100


    while(True):
        print(f'{sand_row},{sand_col}')
        if sand_row >= 200 or sand_col >= 106 or sand_col < 0:
            break
        if grid[sand_row + 1][sand_col] == ".":
            sand_row += 1
        elif grid[sand_row + 1][sand_col - 1]  == ".":
            sand_row += 1
            sand_col -= 1
        elif grid[sand_row + 1][sand_col + 1]  == ".":
            sand_row += 1
            sand_col += 1
        else:
            break

    grid[sand_row][sand_col] = "O"

    #did the sand fall into the void?
    return sand_row >= 200 or sand_col >= 106 or sand_col < 0

sand_falling_forever = False
counter = 0
while(not sand_falling_forever):
    sand_falling_forever = drop_sand()
    counter+=1

[print(''.join(row)) for row in grid]
print(counter)
