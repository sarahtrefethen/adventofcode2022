

ground = set([(x, 0) for x in range(0,7)])

class Rock:
    def move_right(self):
        self.coords = [(x+1, y) for (x, y) in self.coords] if all([x+1 < 7 and (x+1,y) not in ground for (x, y) in self.coords]) else self.coords
    def move_left(self):
        self.coords = [(x-1, y) for (x, y) in self.coords] if all([x-1 >= 0 and (x-1,y) not in ground for (x, y) in self.coords]) else self.coords
    def move_down(self):
        self.coords = [(x, y-1) for (x, y) in self.coords]
        

class Hbar(Rock):
    def  __init__(self, height):
        self.coords = [(2, height), (3, height), (4, height), (5, height)]
class Cross(Rock):
    def  __init__(self, height):
        self.coords = [(3, height), (2, height+1), (3, height+1), (4, height+1), (3, height+2)]
class Corner(Rock):
    def  __init__(self, height):
        self.coords = [(2, height),(3, height),(4, height),(4, height+1),(4, height+2)]
class Vbar(Rock):
    def  __init__(self, height):
        self.coords = [(2,height),(2,height+1),(2,height+2),(2,height+3)]
class Square(Rock):
    def  __init__(self, height):
        self.coords = [(2,height),(2,height+1),(3,height),(3,height+1)]


with open("D17input.txt") as file:
    wind = file.read().strip("\n")



shapes=[Hbar, Cross, Corner, Vbar, Square]

height = 0
wind_index = 0

for rock_count in range(2022):
    rock = shapes[rock_count % len(shapes)](height+4)

    time = 0
    hit = False
    while(not hit):
        if time % 2 == 0:
            dir = wind[wind_index % len(wind)]
            wind_index+=1
            if dir == "<":
                rock.move_left()
            else:
                rock.move_right()
        else:
            if any([(x, y-1) in ground for (x, y) in rock.coords]):
                [ground.add(coord) for coord in rock.coords]
                top_of_settled_rock = max([y for (x,y) in rock.coords])
                if top_of_settled_rock > height:
                    height = top_of_settled_rock
                hit=True
            else:
                print("v")
                rock.move_down()        


        time += 1
    
    print("part1:", height)    
