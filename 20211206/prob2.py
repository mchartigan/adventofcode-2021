'''
--- Part Two ---

Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539 lanternfish!

How many lanternfish would there be after 256 days?
'''

'''
fish(days) = int((days-d0)/7)
'''
class Generation:
    def __init__(self, days):
        self.days = days
        self.members = 0

    def addMembers(self, num):
        self.members += num

    def countdown(self):
        self.days -= 1
        if self.days < 0:
            self.days = 6
            return self.members
        
        return 0

with open("input.txt") as file:
    nums = [int(x) for x in file.readline().split(',')]
    
    generations = [0,0,0,0,0,0,0,0,0]

    for num in nums:
        generations[num] += 1
    
    staticlength = len(generations)
    for _ in range(0,256):
        zeros = generations[0]
        for i in range(0,8):
            generations[i] = generations[i+1]
        generations[8] = zeros
        generations[6] += zeros

    print(sum(generations))