
pairs = []
with open("D15input.txt") as file:
    line = file.readline()
    while line != "":
        [sensor_str, beacon_str] = line.split(": ")
        sensor_x = int(sensor_str[sensor_str.find("=")+1:sensor_str.find(",")])
        sensor_y = int(sensor_str[sensor_str.rfind("=")+1:])
        beacon_x = int(beacon_str[beacon_str.find("=")+1:beacon_str.find(",")])
        beacon_y = int(beacon_str[beacon_str.rfind("=")+1:])
        pairs.append(((sensor_x, sensor_y), (beacon_x, beacon_y)))    
        line=file.readline()

target_row_index = 2000000

target_row = set()
for ((s_x, s_y), (b_x, b_y)) in pairs:
    distance = abs(s_x - b_x) + abs(s_y-b_y)
    if target_row_index in range(s_y-distance, s_y+distance):
        delta = distance - abs(target_row_index-s_y)
        [target_row.add(x) for x in range(s_x-delta, s_x+delta)]

print('part1:', len(target_row))