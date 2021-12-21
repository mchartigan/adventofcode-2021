'''
--- Part Two ---

You still can't quite make out the details in the image. Maybe you just didn't enhance it enough.

If you enhance the starting input image in the above example a total of 50 times, 3351 pixels are lit in the final output image.

Start again with the original input image and apply the image enhancement algorithm 50 times. How many pixels are lit in the resulting image?
'''

import numpy as np
from copy import deepcopy

# Globals
near = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]
rows = 0
cols = 0
alg = {}

def sumNear(img, r, c, i):
    ttl = ''
    for y,x in near:
        try:
            ttl += str(int(img[r+y,c+x]))
        except:
            ttl += '0' if i % 2 == 0 else '1'
    return int(ttl, base=2)

def enhance(img, i):
    old = deepcopy(img)
    for r in range(0, rows):
        for c in range(0, cols):
            img[r,c] = alg[sumNear(old, r, c, i)]

def printImg(img):
    print()
    for r in range(0, rows):
        for c in range(0, cols):
            if img[r,c] == 1:
                print('#', end='')
            else:
                print('.', end='')
        print()

def resize(img, i):
    global rows, cols
    hor = np.zeros((1, cols)) if i % 2 == 0 else np.ones((1, cols))
    img = np.vstack((hor, img, hor))
    rows, cols = img.shape
    vert = np.zeros((rows, 1)) if i % 2 == 0 else np.ones((rows, 1))
    img = np.hstack((vert, img, vert))
    rows, cols = img.shape
    return img

with open("input.txt") as file:
    algstr = file.readline().strip()
    rest = [x.strip() for x in file.readlines() if x.strip() != '']

for i in range(0, len(algstr)):             # map algorithm
    alg[i] = 0 if algstr[i] == '.' else 1

rows = len(rest)
cols = len(rest[0])
img = np.zeros((rows, cols))

for r in range(0, rows):               # process input image
    for c in range(0, cols):
        img[r,c] = 0 if rest[r][c] == '.' else 1

for i in range(0, 50):
    img = resize(img, i)
    # printImg(img)
    enhance(img, i)

# printImg(img)
ttl = int(np.sum(img))
print(ttl)