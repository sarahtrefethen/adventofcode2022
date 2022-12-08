
def split_on_4(string: str):
    ret = []
    start = 0
    end = 3
    while start < len(string):
        ret.append(string[start:end])
        start = end
        end = start + 4
    return ret

with open("D5input.txt", 'r') as input:
    [stacks_str, command_str] = input.read().split("\n\n")
    matrix = [split_on_4(row) for row in stacks_str.split('\n')]

    stacks = [[],[],[],[],[],[],[],[],[]]

    for ri in range(len(matrix)-1, -1, -1):
        for ci in range(len(matrix[ri])):
            content = matrix[ri][ci].strip()
            if content != '':
                stacks[ci].append(content)
    
    for command in command_str.split("\n"):
        count = int(command[5:6] if command[6] == ' ' else command[5:7])
        from_stack = int(command[-6])-1
        to_stack = int(command[-1])-1


        stacks[to_stack].extend(stacks[from_stack][-count:len(stacks[from_stack])])
        stacks[from_stack][-count:len(stacks[from_stack])] = []
    
    print([stack[-1] for stack in stacks])


