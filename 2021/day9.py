import sys


def is_low_pt(row, col):
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for dir in dirs:
        if is_in_bounds(row + dir[0], col + dir[1]):
            if heights[row][col] >= heights[row + dir[0]][col + dir[1]]:
                return False
    return True


def is_in_bounds(row, col):
    return row >= 0 and row < len(heights) and col >= 0 and col < len(heights[0])


def count_basins(row, col):
    # assumed to be called from a low pt.
    return count_basin_helper(row, col, -1, set())


def count_basin_helper(row, col, prev_num, visited):
    if not is_in_bounds(row, col) or heights[row][col] == 9:
        return 0
    if is_visited(row, col, visited):
        return 0
    if heights[row][col] < prev_num:
        return 0

    # Otherwise, visit and try up down left right.
    visit(row, col, visited)
    prev_num = heights[row][col]
    return count_basin_helper(row + 1, col, prev_num, visited) + count_basin_helper(row - 1, col, prev_num, visited) + \
        count_basin_helper(row, col - 1, prev_num, visited) + count_basin_helper(row, col + 1, prev_num, visited) + 1


def visit(row, col, visited):
    visited.add(str(row) + ',' + str(col))


def is_visited(row, col, visited):
    key = str(row) + ',' + str(col)
    return key in visited


file = open('day9_input.txt', 'r')
file_lines = file.readlines()

# adjacent = up down left and right
# edge or corners adjacent -> three or two adjacent

# risk level of low pt = 1 + height of low point

# put into 2d list

heights = []
low_pts = []

for line in file_lines:
    heights.append([int(x) for x in line.strip()])
    low_pts.append([False] * len(line.strip()))

# go through and determine lowpt map
basinSizes = []
for row in range(len(heights)):
    for col in range(len(heights[row])):
        if is_low_pt(row, col):
            basinSizes.append(count_basins(row, col))

basinSizes = sorted(basinSizes)

print(basinSizes)
