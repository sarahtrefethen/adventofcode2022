   
def score(oponnent: str, me: str):
    sum = 0
    if me == 'X': #loose
        if oponnent == 'A': #rock
            sum += 3 #scisors
        elif oponnent == 'B': #paper
            sum += 1 #rock
        elif oponnent == 'C': #scisors
            sum += 2 #pPWE
    elif me == 'Y': #draw
        sum += 3
        if oponnent == 'A': #rock
            sum += 1
        elif oponnent == 'B': #paper
            sum += 2
        elif oponnent == 'C': #scisors
            sum += 3
    elif me == 'Z': #win
        sum += 6
        if oponnent == 'A': #rock
            sum += 2
        elif oponnent == 'B': #paper 
            sum += 3
        elif oponnent == 'C': #scisors
            sum += 1
    return sum

with open("D2input.txt", 'r') as input:
    text = input.read()
    moves = [move.split(" ") for move in text.split('\n')]
    print(sum([score(move[0], move[1]) for move in moves]))
