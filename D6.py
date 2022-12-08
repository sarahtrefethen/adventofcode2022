

with open("D6input.txt", 'r') as input:
    signal = input.read()

    for index in range(len(signal)):
        if index > 13:
            a_set = set(signal[index-13:index+1])
            if len(a_set) == 14:
                print(index+1)
                break
                