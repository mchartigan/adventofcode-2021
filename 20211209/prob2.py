'''
--- Part Two ---

Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678

The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678

The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
'''

def findBasinSize(x, y, map, traversed):

    sum = 1
    traversed.append((x,y))
    if x != 0 and map[y][x-1] != 9 and ((x-1,y) not in traversed):
        sum += findBasinSize(x-1,y,map,traversed)
    if y != 0 and map[y-1][x] != 9 and ((x,y-1) not in traversed):
        sum += findBasinSize(x,y-1,map,traversed)
    if x != len(map[0])-1 and map[y][x+1] != 9 and ((x+1,y) not in traversed):
        sum += findBasinSize(x+1,y,map,traversed)
    if y != len(map)-1 and map[y+1][x] != 9 and ((x,y+1) not in traversed):
        sum += findBasinSize(x,y+1,map,traversed)

    return sum


with open("input.txt") as file:
    map = [[int(char) for char in line.strip()] for line in file.readlines()]
    
    lows = []
    for x in range(0,len(map[0])):
        for y in range(0,len(map)):
            if not (x != 0 and map[y][x-1] <= map[y][x]):
                if not (y != 0 and map[y-1][x] <= map[y][x]):
                    if not (x != len(map[0])-1 and map[y][x+1] <= map[y][x]):
                        if not (y != len(map)-1 and map[y+1][x] <= map[y][x]):
                            lows.append((x,y))

    sizes = []
    for points in lows:
        sizes.append(findBasinSize(points[0], points[1], map, []))
    
    sizes = sorted(sizes, reverse=True)
    print(sizes[0]*sizes[1]*sizes[2])