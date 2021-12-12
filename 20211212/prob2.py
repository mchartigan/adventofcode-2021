'''
--- Part Two ---

After reviewing the available paths, you realize you might have time to visit a single small cave twice. Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. However, the caves named start and end can only be visited exactly once each: once you leave the start cave, you may not return to it, and once you reach the end cave, the path must end immediately.

Now, the 36 possible paths through the first example above are:

start,A,b,A,b,A,c,A,end
start,A,b,A,b,A,end
start,A,b,A,b,end
start,A,b,A,c,A,b,A,end
start,A,b,A,c,A,b,end
start,A,b,A,c,A,c,A,end
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,d,b,A,c,A,end
start,A,b,d,b,A,end
start,A,b,d,b,end
start,A,b,end
start,A,c,A,b,A,b,A,end
start,A,c,A,b,A,b,end
start,A,c,A,b,A,c,A,end
start,A,c,A,b,A,end
start,A,c,A,b,d,b,A,end
start,A,c,A,b,d,b,end
start,A,c,A,b,end
start,A,c,A,c,A,b,A,end
start,A,c,A,c,A,b,end
start,A,c,A,c,A,end
start,A,c,A,end
start,A,end
start,b,A,b,A,c,A,end
start,b,A,b,A,end
start,b,A,b,end
start,b,A,c,A,b,A,end
start,b,A,c,A,b,end
start,b,A,c,A,c,A,end
start,b,A,c,A,end
start,b,A,end
start,b,d,b,A,c,A,end
start,b,d,b,A,end
start,b,d,b,end
start,b,end

The slightly larger example above now has 103 paths through it, and the even larger example now has 3509 paths through it.

Given these new rules, how many paths through this cave system are there?
'''

class Cave:
    def __init__(self, name):
        self.name = name
        self.connections = {}

    def add(self, cave):
        if cave.name not in self.connections.keys():
            self.connections[cave.name] = cave

def explore(start, currentPath, dblTraversed):
    found = 0
    currentPath.append(start.name)
    if start.name == "end":
        return 1
    
    for pt in start.connections.values():
        if pt.name != "start":
            if pt.name == "end" or pt.name.isupper() or pt.name not in currentPath:
                found += explore(pt, currentPath[:], dblTraversed)
            elif not dblTraversed:
                found += explore(pt, currentPath[:], True)

    return found



with open("input.txt") as file:
    pairs = [x.strip().split('-') for x in file.readlines()]

    caves = {}
    for x,y in pairs:
        if x not in caves.keys():
            caves[x] = Cave(x)
        if y not in caves.keys():
            caves[y] = Cave(y)
        caves[x].add(caves[y])
        caves[y].add(caves[x])
    
    print(explore(caves["start"], [], False))
        