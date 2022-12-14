 

chars = 'SabcdefghijklmnopqrstuvwxyzE'

chars_to_ints = {chars[x]: x for x in range(len(chars))}

with open("D12input.txt") as input:
    map = input.read().split('\n')

map_area = len(map) * len(map[0])

[start] = [(x, y) for x in range(len(map)) for y in range(len(map[x])) if map[x][y] == "S"]
[end] = [(x, y) for x in range(len(map)) for y in range(len(map[x])) if map[x][y] == "E"]

n = 0

paths = [{
    'current': end,
    'visited': set(),
}]

def test_step(current_char_value, next_x, next_y): 
    next_char = "z" if map[next_x][next_y] == "E" else map[next_x][next_y]

    return  chars_to_ints[next_char] >= current_char_value - 1   

found = False
while(not found):

    if n > map_area:
        print("something went wrong")
        break

    new_paths = []

    for index, path in enumerate(paths):
        (x, y) = path['current']
        visited = path['visited']
        visited.add(f'{x},{y}')  
        if(map[x][y] == "a"):
            print(f'part 1: {n}')
            found = True
            break

        current_char_value = chars_to_ints[map[x][y]] 
        for (test_x, test_y) in [(x,y-1), (x,y+1), (x-1,y), (x+1,y)]:
            if 0<=test_x<len(map) and 0<=test_y<len(map[test_x]) and f'{test_x},{test_y}' not in visited:
                if test_step(current_char_value, test_x, test_y):
                    if (test_x,test_y) not in [new_path['current'] for new_path in new_paths]:
                        new_paths.append({
                            'current': (test_x,test_y),
                            'visited': visited.copy()
                        }) 
        
    paths = new_paths
    n+=1

