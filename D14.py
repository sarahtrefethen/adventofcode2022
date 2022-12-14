
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


[print(''.join(row)) for row in grid]

