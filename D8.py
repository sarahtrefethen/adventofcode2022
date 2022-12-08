
with open("D8input.txt", 'r') as input:
    string = input.read()
    grid = [[int(char) for char in line] for line in string.split('\n')]
    
    part1_count = 0

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if x==0 or x == len(grid)-1 or y==0 or y == len(grid[x])-1:
                part1_count+=1
            else:
                tree = grid[x][y]
                left = [grid[x][n] for n in range(y)]
                if tree > max(left):
                    part1_count += 1
                else:
                    right = [grid[x][n] for n in range(y+1, len(grid[x]))]
                    if tree > max(right):
                        part1_count += 1
                    else: 
                        up = [grid[n][y] for n in range(x)]
                        if tree > max(up):
                            part1_count += 1
                        else:
                            down = [grid[n][y] for n in range(x+1, len(grid))]
                            if tree > max(down):
                                part1_count += 1
    print("part 1:", part1_count)

    def window_view(tree: int, trees: list):
        for i in range(len(trees)):
            if trees[i] >= tree:
                return i+1
        return len(trees)

    max_view = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            left = [grid[x][n] for n in range(y)] 
            left.reverse()
            right = [grid[x][n] for n in range(y+1, len(grid[x]))]
            up = [grid[n][y] for n in range(x)]
            up.reverse()
            down = [grid[n][y] for n in range(x+1, len(grid))]
            total_score = window_view(grid[x][y], left) * window_view(grid[x][y], right) * window_view(grid[x][y], up) * window_view(grid[x][y], down)
            if total_score > max_view:
                max_view = total_score
    print("part 2:", max_view)

