
with open("D18input.txt") as file:
    cubes =[(int(x), int(y), int(z)) for [x, y, z] in [string.split(",") for string in file.read().split('\n')]]

def touching(c1, c2):
    (x1, y1, z1) = c1 
    (x2,y2,z2) = c2
    if x1==x2:
        if y1==y2:  
          return abs(z1-z2) == 1
        elif z1==z2:  
          return abs(y1-y2) == 1
    elif y1==y2: 
        if x1==x2:  
          return abs(z1-z2) == 1
        elif z1==z2:  
          return abs(x1-x2) == 1
    elif z1==z2: 
        if y1==y2:  
          return abs(x1-x2) == 1
        elif x1==x2:  
          return abs(y1-y2) == 1
    return False


surface = 6 * len(cubes)
for i, c1 in enumerate(cubes):
    for c2 in cubes[i+1:]:
        if touching(c1, c2):
            surface -= 2

print(surface)
    
