


with open("D7input.txt", 'r') as input:

    nodes = {
        'children': {},
        'parent': "xxx",
        'name': "xxx",
        'type': "dir"
    }
    current_node = nodes

    def add_node(line: str):
        [first_w, second_w] = line.split(" ")
        name = second_w.strip('\n')
        type = 'dir' if first_w == 'dir' else 'file'
        current_node['children'][name] = {
            'type': type,
            'name': name,
            'parent': current_node,
        }
        if type == 'dir':
            current_node['children'][name]['children'] = {}
        else:
            current_node['children'][name]['size'] = int(first_w)

    line = input.readline()
    while line != '':
        if line[0] != '$':
            add_node(line)
        elif line[0:4] == "$ cd":
            new_node_name = line.split(" ")[2].strip('\n')
            if new_node_name == "..":
                current_node = current_node['parent']
            else:
                current_node = current_node['children'][new_node_name]
        
        line = input.readline()
    
    part1_total = 0

    def calculate_size(node: dict):
        global part1_total
        # print(node)
        if 'size' not in node:
            node['size'] = sum([calculate_size(node['children'][child]) for child in node['children']])
        if node['size'] <= 100000 and node['type'] == 'dir':
            part1_total += node['size']
        return node['size']

    needed_space = calculate_size(nodes) - 40000000
    print('part 1', part1_total)

    # for part two I started to keep track of the answer in the return value of 
    # the recursive function, but I got a little bogged down and just threw in an 
    # accumulator to get the answer. So the following chunk of code reflects and 
    # incomplete line of thought in addition to my solution
    part2_total = 1000000000000000000000

    def pick_for_deletion(node: dict):
        global part2_total
        if node["type"] == "dir":
            child_results = ([result for result in [pick_for_deletion(node["children"][child]) for child in node["children"]] if result != 0])
            if node['size'] >= needed_space and node['size'] < part2_total:
                part2_total = node["size"]
                child_results.append(node['size'])
            child_results.sort
            return child_results[0] if len(child_results) > 0 else 0
        if node['size'] >= needed_space and node['type'] == 'dir':
            print(node["name"])
            return node['size']
        return 0

    pick_for_deletion(nodes)

    print("part 2:", part2_total)
