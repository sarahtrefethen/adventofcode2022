def part1():
    with open("D9input.txt", 'r') as input:
        
        head = [0,0]
        tail = [0,0]
        x = 0
        y = 1

        visited = set()

        def move_head(direction):
            if direction == 'R':
                head[x]+=1
            if direction == "U":
                head[y]+=1
            if direction == "L":
                head[x]-=1
            if direction == "D":
                head[y]-=1

        def move_tail():
            visited.add(f'{tail[x]}{tail[y]}')
            x_delta = head[x] - tail[x]
            y_delta = head[y] - tail[y]
            if x_delta != 0 and y_delta != 0:
                if abs(x_delta) == abs(y_delta) == 1:
                    return
                
                if x_delta > 0:
                    tail[x] += 1
                else:  
                    tail[x] -= 1
                if y_delta > 0:
                    tail[y] += 1
                else:  
                    tail[y] -= 1
                
            elif x_delta == 2:
                tail[x] += 1
            elif x_delta == -2:
                tail[x] -= 1
            elif y_delta == 2:
                tail[y] += 1
            elif y_delta == -2:
                tail[y] -= 1
            visited.add(f'{tail[x]}{tail[y]}')
            



        line = input.readline()
        while line != "":
            [direction, count] = line.split(" ")
            count = int(count)

            for i in range(count):
                move_head(direction)
                move_tail()

            line = input.readline()

        print("part 1:", len(visited))

