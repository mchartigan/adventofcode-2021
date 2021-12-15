'''
--- Part Two ---

The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
'''

rules = {}
maps = {}

def polymerize(string, depth):
    depth += 1
    counts = {}
    if depth > 40:
        return counts
    for i in range(0,len(string)-1):
        newstr = rules[string[i:i+2]]
        counts[newstr[1]] = 1 if newstr[1] not in counts else counts[newstr[1]] + 1

        if newstr in maps and depth in maps[newstr]:
            for k,v in maps[newstr][depth].items():
                counts[k] = v if k not in counts else counts[k] + v
        else:
            ret = polymerize(newstr, depth)
            if newstr not in maps:
                maps[newstr] = {depth: ret}
            else:
                maps[newstr][depth] = ret
            for k,v in ret.items():
                counts[k] = v if k not in counts else counts[k] + v
    
    return counts


with open("input.txt") as file:
    polymer = file.readline().strip()
    file.readline()
    temp = [x.strip().split(' -> ') for x in file.readlines()]
    for k,v in temp:
        rules[k] = k[0] + v + k[1]

    counts = {}
    for char in polymer:
        counts[char] = 1 if char not in counts else counts[char] + 1

    ret = polymerize(polymer, 0)
    for k,v in ret.items():
        counts[k] = v if k not in counts else counts[k] + v
    vals = counts.values()
    print(max(vals)-min(vals))