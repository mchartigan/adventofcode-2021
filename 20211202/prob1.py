fwd = 0
depth = 0

with open("input.txt") as file:
    lines = file.readlines()

    for line in lines:
        list = line.split(' ')
        if list[0] == "forward":
            fwd = fwd + int(list[1])
        elif list[0] == "down":
            depth = depth + int(list[1])
        elif list[0] == "up":
            depth = depth - int(list[1])

    print(depth*fwd)