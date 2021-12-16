'''
--- Day 15: Chiton ---

You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.

The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581

You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581

The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).

What is the lowest total risk of any path from the top left to the bottom right?
'''

from math import inf

nodes = []

class Node:
    def __init__(self, val, x, y):
        self.weight = val
        self.x = x
        self.y = y
        self.adj = []

    def addNeighbors(self):
        neighbors = [[-1,0],[0,-1],[0,1],[1,0]]
        for i,j in neighbors:
            row = self.x+i
            col = self.y+j
            if 0 <= row < len(nodes) and 0 <= col < len(nodes):
                self.adj.append(nodes[row][col])

    @property
    def pos(self):
        return self.x, self.y

with open("input.txt") as file:
    nodes = [[int(x) for x in y.strip()] for y in file.readlines()]
    
    start = [0, 0]
    end = [len(nodes)-1, len(nodes)-1]

    for i in range(0,len(nodes)):
        for j in range(0,len(nodes)):
            weight = nodes[i][j]
            nodes[i][j] = Node(weight, i, j)

    queue = {}
    dist = [[inf for x in range(0,len(nodes))] for y in range(0,len(nodes))]
    dist[0][0] = 0
    prev = [[None for x in range(0,len(nodes))] for y in range(0,len(nodes))]
    for i in range(0,len(nodes)):
        for j in range(0,len(nodes)):
            nodes[i][j].addNeighbors()
            queue[nodes[i][j]] = dist[i][j]

    while queue:
        temp = inf
        u = None
        for key in queue:
            if queue[key] < temp:
                u = key
                temp = queue[key]
        queue.pop(u)

        for k,v in queue.items():
            if k in u.adj:
                alt = temp + k.weight
                if alt < v:
                    dist[k.x][k.y] = alt
                    prev[k.x][k.y] = u
                    queue[k] = alt
         
    print(dist[len(nodes)-1][len(nodes)-1])