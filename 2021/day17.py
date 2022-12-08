from collections import Counter
from line_profiler_pycharm import profile
from copy import copy, deepcopy
from pandas import DataFrame
import pandas
import sys
import time
from heapq import *
import numpy as np

file = open('day17_input.txt', 'r')
file_lines = [x.strip() for x in file.readlines()]


# each step:
# x position increases by its x velocity
# y pos increases by its y velocity
# due to drag, x vel cahnges by 1 towards 0
# probes y velocity decreases by 1

# target area: x=20..30, y=-10..-5 (within ANY step)

# find initial x,y vel values s.t. after any step, probe's x position is at least 20 and at most 30 and the probes y pos is at least -10 and at most -5
# how high can you make the probe go while still reaching the target area?

# whats the formula? this seems like a binary search problem.
# do brute force first
bounds_x = (240, 292)
bounds_y = (-90, -57)

max_x = None
max_y = 0
in_range = []
for x in range(293):
    for y in range(-91, 100):
        # go until either x > max_x or y > max_y
        x_vel = x
        y_vel = y
        x_pos = 0
        y_pos = 0
        while True:
            if x_pos > bounds_x[1] or y_pos < bounds_y[0]:
                break

            if bounds_x[0] <= x_pos <= bounds_x[1] and bounds_y[0] <= y_pos <= bounds_y[1]:
                in_range.append((x, y))
                break

            # otherwise, perform a step
            x_pos += x_vel
            y_pos += y_vel
            x_vel = max(x_vel - 1, 0)
            y_vel -= 1
    print(x)

print(len(in_range))

