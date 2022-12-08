from collections import Counter
from line_profiler_pycharm import profile
from copy import copy, deepcopy
from pandas import DataFrame
import pandas
import sys
import time
from heapq import *
import numpy as np
import math
from itertools import permutations

file = open('day19_input.txt', 'r')
file_lines = [x.strip() for x in file.readlines()]

#determine pos of beacons and scanners yourself

# find pair of scanners that have overlapping w/ at least 12 beacons that both scanners detect.
# by establishing 12 common beacons, you can precisly determine where the scanners are relative to each other.

#0,2
#4,1
#3,3

#-1,-1
#-5,0
#-2,1

# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -

# 24 orientations?
# 90 degrees times an integer on x, y, z
# does it have to be the same integer value?
# assume not..
# can be 4 diff directions on x y and z...
# no
# x y and z can all be swapped..
# 3 * 2 * 1 = 6 and then each can be positive or negative values..
# no..
# going around x axis makes y or z change sign.
# going around y axis makes x or z change sign..
# so... positive or negative x y or z, and considering any of the 3 directions "up".
# 8 * 3... -> 24.. wtf problem is wrong says 4.

# --- scanner 0 ---
# 404,-588,-901
# 528,-643,409
# -838,591,734
# 390,-675,-793
# -537,-823,-458
# -485,-357,347
# -345,-311,381
# -661,-816,-575
# -876,649,763
# -618,-824,-621
# 553,345,-567
# 474,580,667
# -447,-329,318
# -584,868,-557
# 544,-627,-890
# 564,392,-477
# 455,729,728
# -892,524,684
# -689,845,-530
# 423,-701,434
# 7,-33,-71
# 630,319,-379
# 443,580,662
# -789,900,-551
# 459,-707,401
#
# --- scanner 1 ---
# 686,422,578
# 605,423,415
# 515,917,-361
# -336,658,858
# 95,138,22
# -476,619,847
# -340,-569,-846
# 567,-361,727
# -460,603,-452
# 669,-402,600
# 729,430,532
# -500,-761,534
# -322,571,750
# -466,-666,-811
# -429,-592,574
# -355,545,-477
# 703,-491,-529
# -328,-685,520
# 413,935,-424
# -391,539,-444
# 586,-435,557
# -364,-763,-893
# 807,-499,-711
# 755,-354,-619
# 553,889,-390

# if in same direction, then
# difference of two beacons from the scanner should be the same?
# a.B1 = a.B1(absolute) - a.s0(absolute)
# a.B2 = a.b2(absolute) - a.s0(absolute)
# a.b1 - a.b2 = a.b1 - a.b2 + 0
# so.. to find all unique beacons.. try
# first find out the orientation of the scanner..
# use two beacons, and look for another beacon pair in b2.
# try this first

# read in scanners, put them in lists

def diff(coordA, coordB):
    return coordA - coordB

def isSame(coordA, coordB):
    return np.array_equiv(coordA, coordB)

def isSame2(coordA, coordB):
    mag1 = np.linalg.norm(coordA)
    mag2 = np.linalg.norm(coordB)
    return mag1 == mag2


def changeOrientation(coordA, perm, sign):
    return coordA[perm] * sign

# use rot90...

scanners = []
i = -1
for line in file_lines:
    if len(line) == 0:
        continue
    if line[1] == '-':
        i += 1
        scanners.append([])
        continue
    line.split(',')
    scanners[i].append(np.array([int(x) for x in line.split(',')]))

perms = [list(x) for x in permutations([0,1,2])]
signs = []
for i in [-1,1]:
    for j in [-1,1]:
        for k in [-1,1]:
            signs.append([i, j, k])


# 8 * 6 = 48, but half are not valid from rotations..
# let's try anyway.
for i in range(len(scanners[0])):
    for j in range(i+1, len(scanners[0])):
        s0b0 = scanners[0][i]
        s0b1 = scanners[0][j]
        s0_diff = diff(s0b1, s0b0)
        for i_0 in range(len(scanners[1])):
            for j_0 in range(i_0 + 1, len(scanners[1])):
                b1 = scanners[1][i_0]
                b2 = scanners[1][j_0]
                # go through each orientation
                for p in perms:
                    for s in signs:
                        # assume same orientation since same scanner..
                        b1_o = changeOrientation(b1, p, s)
                        b2_o = changeOrientation(b2, p, s)
                        s1_diff = diff(b2_o, b1_o)
                        if isSame2(s0_diff, s1_diff):
                            print("Nice!")
    print(str(i) + ' out of ' + str(len(scanners[0])))






