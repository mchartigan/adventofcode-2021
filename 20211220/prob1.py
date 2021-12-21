'''
--- Day 20: Trench Map ---

With the scanners fully deployed, you turn their attention to mapping the floor of the ocean trench.

When you get back the image from the scanners, it seems to just be random noise. Perhaps you can combine an image enhancement algorithm and the input image (your puzzle input) to clean it up a little.

For example:

..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###

The first section is the image enhancement algorithm. It is normally given on a single line, but it has been wrapped to multiple lines in this example for legibility. The second section is the input image, a two-dimensional grid of light pixels (#) and dark pixels (.).

The image enhancement algorithm describes how to enhance an image by simultaneously converting all pixels in the input image into an output image. Each pixel of the output image is determined by looking at a 3x3 square of pixels centered on the corresponding input image pixel. So, to determine the value of the pixel at (5,10) in the output image, nine pixels from the input image need to be considered: (4,9), (4,10), (4,11), (5,9), (5,10), (5,11), (6,9), (6,10), and (6,11). These nine input pixels are combined into a single binary number that is used as an index in the image enhancement algorithm string.

For example, to determine the output pixel that corresponds to the very middle pixel of the input image, the nine pixels marked by [...] would need to be considered:

# . . # .
#[. . .].
#[# . .]#
.[. # .].
. . # # #

Starting from the top-left and reading across each row, these pixels are ..., then #.., then .#.; combining these forms ...#...#.. By turning dark pixels (.) into 0 and light pixels (#) into 1, the binary number 000100010 can be formed, which is 34 in decimal.

The image enhancement algorithm string is exactly 512 characters long, enough to match every possible 9-bit binary number. The first few characters of the string (numbered starting from zero) are as follows:

0         10        20        30  34    40        50        60        70
|         |         |         |   |     |         |         |         |
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##

In the middle of this first group of characters, the character at index 34 can be found: #. So, the output pixel in the center of the output image should be #, a light pixel.

This process can then be repeated to calculate every pixel of the output image.

Through advances in imaging technology, the images being operated on here are infinite in size. Every pixel of the infinite output image needs to be calculated exactly based on the relevant pixels of the input image. The small input image you have is only a small region of the actual infinite input image; the rest of the input image consists of dark pixels (.). For the purposes of the example, to save on space, only a portion of the infinite-sized input and output images will be shown.

The starting input image, therefore, looks something like this, with more dark pixels (.) extending forever in every direction not shown here:

...............
...............
...............
...............
...............
.....#..#......
.....#.........
.....##..#.....
.......#.......
.......###.....
...............
...............
...............
...............
...............

By applying the image enhancement algorithm to every pixel simultaneously, the following output image can be obtained:

...............
...............
...............
...............
.....##.##.....
....#..#.#.....
....##.#..#....
....####..#....
.....#..##.....
......##..#....
.......#.#.....
...............
...............
...............
...............

Through further advances in imaging technology, the above output image can also be used as an input image! This allows it to be enhanced a second time:

...............
...............
...............
..........#....
....#..#.#.....
...#.#...###...
...#...##.#....
...#.....#.#...
....#.#####....
.....#.#####...
......##.##....
.......###.....
...............
...............
...............

Truly incredible - now the small details are really starting to come through. After enhancing the original input image twice, 35 pixels are lit.

Start with the original input image and apply the image enhancement algorithm twice, being careful to account for the infinite size of the images. How many pixels are lit in the resulting image?
'''

# I did kinda hardcode what a convolution sum results in
# - for the sample, 0 -> 0 so I didn't have to do anything special with the null space
# - for the input, 0 -> 1 so that made it harder, but I basically said on lines 130, 151, and 154
#   to alternate replacing white space with zeros and ones so that I didn't have to make a crazy
#   big matrix

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

for i in range(0, 2):
    img = resize(img, i)
    # printImg(img)
    enhance(img, i)

# printImg(img)
ttl = int(np.sum(img))
print(ttl)