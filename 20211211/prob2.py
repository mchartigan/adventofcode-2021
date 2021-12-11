'''
--- Part Two ---

It seems like the individual flashes aren't bright enough to navigate. However, you might have a better option: the flashes seem to be synchronizing!

In the example above, the first time all octopuses flash simultaneously is step 195:

After step 193:
5877777777
8877777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777

After step 194:
6988888888
9988888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888

After step 195:
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000

If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to navigate through the cavern. What is the first step during which all octopuses flash?
'''

width = 10
height = 10

def flash(octos):
    flashes = 0
    dirs = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

    for i in range(0, height):
        for j in range(0, width):
            if octos[i][j] > 9:
                flashes += 1
                for x,y in dirs:
                    try:
                        if octos[i+x][j+y] != 0 and i+x >= 0 and j+y >= 0:
                            octos[i+x][j+y] += 1
                    except:
                        pass
                
                octos[i][j] = 0
                flashes += flash(octos)

    return flashes

def wrapper(octos):
    if flash(octos) >= 100:
        return True
    return False


with open("input.txt") as file:
    octos = [[int(char) for char in line.strip()] for line in file.readlines()]

    total = 0
    k = 0
    while True:
        k += 1
        for i in range(0, height):
            for j in range(0, width):
                octos[i][j] += 1

        if wrapper(octos):
            print(k)
            break
