'''
--- Part Two ---

Sometimes, it's a good idea to appreciate just how big the ocean is. Using the Manhattan distance, how far apart do the scanners get?

In the above example, scanners 2 (1105,-1205,1229) and 3 (-92,-2380,-20) are the largest Manhattan distance apart. In total, they are 1197 + 1175 + 1249 = 3621 units apart.

What is the largest Manhattan distance between any two scanners?
'''


import numpy as np
from copy import deepcopy
from math import sin, cos, pi

rotations = [0, pi/2, pi, 3*pi/2]
matrices = []
overlap = 11
bottom = np.array([0,0,0,1])    # bottom of rotation matrix (don't wanna redefine)


class Scanner:
    def __init__(self, name):
        self.name = name
        self.points = []
        self._rotated = []
        self._backup = []
        self._rotate = np.eye(3)
        self._translate = np.array([[0],[0],[0]])
        self.relatives = []
        self.matched = None

    @staticmethod
    def rotz(z):
        return np.array([[round(cos(z)),round(-sin(z)),0],[round(sin(z)),round(cos(z)),0],[0,0,1]])

    @staticmethod
    def roty(y):
        return np.array([[round(cos(y)),0,round(sin(y))],[0,1,0],[round(-sin(y)),0,round(cos(y))]])

    @staticmethod
    def rotx(x):
        return np.array([[1,0,0],[0,round(cos(x)),round(-sin(x))],[0,round(sin(x)),round(cos(x))]])

    def add(self, point):
        self.points.append(point)
        self._rotated.append(point)
        self._backup.append(point)
        self.relatives.append([])

    def rotate(self, mat):
        self._rotate = mat
        
        for i in range(0,len(self._backup)):
            self._rotated[i] = np.dot(self._rotate, self._backup[i])

    def translate(self, dr):
        self._translate = dr
        
        for i in range(0,len(self._backup)):
            self.points[i] = self._rotated[i] + self._translate

    def __eq__(self, other):
        ct = 0
        for i in range(0,len(self.points)):
            for j in range(0,len(other.points)):
                if np.array_equal(self.points[i], other.points[j]):
                    ct += 1
                    if ct >= overlap:
                        return True
        return False

    def updateRelatives(self, choice=None):
        if choice is None:
            for i in range(0, len(self.relatives)):
                for j in range(0, len(self.relatives)):
                    dx = abs(self._backup[i][0,0] - self._backup[j][0,0])
                    dy = abs(self._backup[i][1,0] - self._backup[j][1,0])
                    dz = abs(self._backup[i][2,0] - self._backup[j][2,0])
                    mag = dx**2 + dy**2 + dz**2
                    self.relatives[i].append((mag, max(dx,dy,dz), min(dx,dy,dz)))
        elif choice == 'all':
            self.relatives = [[None for x in self.points] for y in self.points]
            for i in range(0, len(self.relatives)):
                for j in range(0, len(self.relatives)):
                    dx = abs(self._backup[i][0,0] - self._backup[j][0,0])
                    dy = abs(self._backup[i][1,0] - self._backup[j][1,0])
                    dz = abs(self._backup[i][2,0] - self._backup[j][2,0])
                    mag = dx**2 + dy**2 + dz**2
                    self.relatives[i][j] = (mag, max(dx,dy,dz), min(dx,dy,dz))
        else:
            i = choice
            for j in range(0, len(self.relatives)):
                dx = abs(self._backup[i][0,0] - self._backup[j][0,0])
                dy = abs(self._backup[i][1,0] - self._backup[j][1,0])
                dz = abs(self._backup[i][2,0] - self._backup[j][2,0])
                mag = dx**2 + dy**2 + dz**2
                self.relatives[i][j] = (mag, max(dx,dy,dz), min(dx,dy,dz))

    def relEqual(self, other, otherI, selfI):
        ct = 0
        for i in range(0,len(self.relatives[selfI])):
            for j in range(0,len(other.relatives[otherI])):
                if self.relatives[selfI][i] == other.relatives[otherI][j]:
                    ct += 1
                    if ct >= overlap + 1:
                        return True
        return False


def defineRotations():
    for yaw in rotations:
        for pitch in rotations:
            for roll in rotations:
                Rz = Scanner.rotz(yaw)
                Ry = Scanner.roty(pitch)
                Rx = Scanner.rotx(roll)
                mat = np.dot(np.dot(Rz, Ry), Rx)
                exists = False
                for x in matrices:
                    if np.array_equal(mat, x):
                        exists = True
                if not exists:
                    matrices.append(mat)

def searchForRotation(scn, soln, a, b):
    # a in soln.points, b in scn._rotated
    for mat in matrices:
        scn.rotate(mat)
        scn.translate(soln._backup[a] - scn._rotated[b])

        if scn == soln:
            scn.matched = soln
            for pt in scn.points:
                match = False

                for u in soln.points:
                    if np.array_equal(pt, u):
                        match = True
                        break
                
                if not match:
                    soln.add(pt)
            soln.updateRelatives(choice='all')
            return True
    return False

def search(scanners, i, j):
    for b in range(0,len(scanners[i].relatives)):
        for a in range(0,len(scanners[j].relatives)):
            scanners[i].translate(scanners[j]._backup[a] - scanners[i]._backup[b])
            scanners[i].updateRelatives(choice=b)
            if scanners[i].relEqual(scanners[j], a, b):
                    return searchForRotation(scanners[i], scanners[j], a, b)

    return False

with open("input.txt") as file:
    lines = [x.strip() for x in file.readlines() if x.strip() != '']

scanners = []
for line in lines:
    if line[0:2] == '--':
        scanners.append(Scanner(line.replace('---', '').strip()))
    else:
        x,y,z = line.split(',')
        scanners[-1].add(np.array([[int(x)],[int(y)],[int(z)]]))

[scn.updateRelatives() for scn in scanners]
defineRotations()

finished = False
ind = 0
while not finished:
    finished = True
    print("loop " + str(ind))
    ind += 1
    for i in range(1,len(scanners)):
        if scanners[i].matched is None:
            search(scanners, i, 0)
        if scanners[i].matched is None:
            finished = False
        else:
            print("solved " + str(i))

print(len(scanners[0].points))   # 295 too low, 315 too high?

maxMhtn = 0
for i in range(0,len(scanners)):
    for j in range(0,len(scanners)):
        mhtn = np.linalg.norm(scanners[i]._translate - scanners[j]._translate, ord=1)
        if mhtn > maxMhtn:
            maxMhtn = mhtn

print(maxMhtn)