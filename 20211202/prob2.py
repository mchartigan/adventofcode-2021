fwd = 0
depth = 0
aim = 0

with open("input.txt") as file:
    lines = file.readlines()

    for line in lines:
        list = line.split(' ')
        if list[0] == "forward":
            fwd = fwd + int(list[1])
            depth = depth + aim * int(list[1])
        elif list[0] == "down":
            aim = aim + int(list[1])
        elif list[0] == "up":
            aim = aim - int(list[1])

    print(depth*fwd)