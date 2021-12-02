with open("input1.txt") as file:
    lines = file.readlines()
    window = []

    for i in range(0, len(lines) - 2):
        window.append(int(lines[i]) + int(lines[i+1]) + int(lines[i+2]))

    count = 0
    last = None
    for val in window:
        if last is not None:
            if val > last:
                count = count + 1
        
        last = val

    print(count)
