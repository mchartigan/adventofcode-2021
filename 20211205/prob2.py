'''
--- Part Two ---

Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

    An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
    An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....

You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
'''

import re
import numpy

class Line:
    def __init__(self, line):
        points = re.split(r' -> |,', line)
        self.x1 = int(points[0])
        self.y1 = int(points[1])
        self.x2 = int(points[2])
        self.y2 = int(points[3])

        try:
            self.slope = (self.y2 - self.y1) / (self.x2 - self.x1)
        except:
            if (self.y2 - self.y1) > 0:
                self.slope = 10
            else:
                self.slope = -10
    
    def getPoints(self):
        points = []
        point = [self.x1, self.y1]
        points.append(point)
        end = [self.x2, self.y2]

        while point != end:
            if self.slope == 10:
                point = [point[0], point[1]+1]
            elif self.slope == -10:
                point = [point[0], point[1]-1]
            else:
                dir = 1 if self.x2 > self.x1 else -1
                point = [point[0]+dir, point[1]+(dir*self.slope)]
            points.append(point)

        return points


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = [Line(x.strip()) for x in file.readlines()]
        size = 1000
        
        map = numpy.zeros((size,size), dtype=int)
        for line in lines:
            points = line.getPoints()

            for point in points:
                map[int(point[1])][int(point[0])] += 1

        count = 0
        for i in range(0,size):
            for j in range(0,size):
                if map[i][j] >= 2:
                    count += 1

        print(count)