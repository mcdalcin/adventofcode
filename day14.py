import math
import copy
import heapq as heap
from functools import cmp_to_key

import numpy as np
import ast
from prettytable import PrettyTable

# returns false if starts falling into abyss. modifies grid with the stand piece resting.
def add_sand(grid):
    x = 500
    y = 0

    if grid[y][x] == 'o' or grid[y] == '#':
        return False

    # while in bounds of grid
    while y < len(grid) and x < len(grid[0]) and x >= 0:
        # keep going down, down-left, down-right until we can't anymore.
        if y+1 >= len(grid) or x < 0 or x >= len(grid[0]):
            print('should not get here')
            return False
        if grid[y+1][x] == '.':
            y += 1
        elif grid[y+1][x-1] == '.':
            y += 1
            x -= 1
        elif grid[y+1][x+1] == '.':
            y += 1
            x += 1
        else:
            # can't go down anymore. mark current spot.
            grid[y][x] = 'o'
            return True
    # out of bounds. return false.
    print('should not get here')
    return False

file = open('day14_input.txt', 'r')
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]

# go through each line, split by ' -> '

paths = []
max_x = 0
max_y = 0
for line in lines:
    path = []
    for pos in line.split(' -> '):
        position = pos.split(',')
        path.append((int(position[0]), int(position[1])))
        max_x = max(max_x, int(position[0]))
        max_y = max(max_y, int(position[1]))

    paths.append(path)

max_x = 1000
max_y = max_y + 2
# make array of max_x and max_y
# fill with '.'

grid = [['.' for x in range(max_x + 1)] for y in range(max_y + 1)]

# go through each path and fill grid with '#' for the path.

# set last row equal to row full of '#'
for x in range(max_x + 1):
    grid[max_y][x] = '#'

for path in paths:
    # from pos to the next position
    start_position = path[0]
    for end_position in path[1:]:
        # if y is the same, go through every x in between.
        add_x = 0
        add_y = 0
        if end_position[1] == start_position[1]:
            add_x = 1 if end_position[0] > start_position[0] else -1
            add_y = 0
        elif end_position[0] == start_position[0]:
            add_x = 0
            add_y = 1 if end_position[1] > start_position[1] else -1
        else:
            print('somethings wrong.')

        current_position = start_position
        while end_position[1] != current_position[1] or end_position[0] != current_position[0]:
            grid[current_position[1]][current_position[0]] = '#'
            current_position = (current_position[0] + add_x, current_position[1] + add_y)

        # mark current position.
        grid[current_position[1]][current_position[0]] = '#'

        start_position = end_position

p = PrettyTable()
for row in grid:
    p.add_row(row)

print(p.get_string(header=False, border=False))


count = 0
while add_sand(grid):
    count += 1

print(count)

