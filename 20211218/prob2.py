'''
--- Part Two ---

You notice a second question on the back of the homework assignment:

What is the largest magnitude you can get from adding only two of the snailfish numbers?

Note that snailfish addition is not commutative - that is, x + y and y + x can produce different results.

Again considering the last example homework assignment above:

[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]

The largest magnitude of the sum of any two snailfish numbers in this list is 3993. This is the magnitude of [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]] + [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]], which reduces to [[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]].

What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?
'''

from math import floor, ceil
from copy import deepcopy
# import numpy as np

class SFNum:
    def __init__(self, val, depth):
        self.val = val
        self.depth = depth

    def split(self):
        return [SFNum(floor(self.val/2), self.depth+1), SFNum(ceil(self.val/2), self.depth+1)]

def magnitude(result):
    list = result[:]
    while len(list) > 1:
        deepest = list[0].depth
        di = 0
        for i in range(0,len(list)):
            if list[i].depth > deepest:
                di = i
                deepest = list[i].depth
        
        list[di:di+2] = [SFNum(list[di].val*3 + list[di+1].val*2,list[di].depth-1)]

    return list[0].val

def addLists(x, y):
    x.extend(y)
    for num in x:
        num.depth += 1

def reduce(list):
    for i in range(0,len(list)):    # check for explodes first
        if list[i].depth > 4:
            if i > 0:
                list[i-1].val += list[i].val
            if i+2 < len(list):
                list[i+2].val += list[i+1].val
            list[i].val = 0
            list[i].depth -= 1
            del list[i+1]
            return True
    for i in range(0,len(list)):    # check for splits second
        if list[i].val > 9:
            list[i:i+1] = list[i].split()
            return True
    return False

with open("input.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    nums = []
    for line in lines:
        depth = 0
        num = []
        for char in line:
            if char == '[':
                depth += 1
            elif char == ']':
                depth -= 1
            elif char == ',':
                pass
            else:
                num.append(SFNum(int(char),depth))
        nums.append(num)

    totals = []
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if i != j:
                x = deepcopy(nums[i])
                y = deepcopy(nums[j])
                addLists(x, y)
                while reduce(x):
                    pass
                totals.append(magnitude(x))
    print(max(totals))