count = 0

with open("input1.txt") as file:
    lines = file.readlines()
    last = None
    for line in lines:
        current = int(line)
        if last is not None:
            if current > last:
                count = count + 1
        
        last = current

    print(count)