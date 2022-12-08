import sys
import string

def get_scenic_score(trees, row, col):
    # go up, left, down, up.
    # if any of these are not visible, return false.
    # if all are visible, return true.

    return get_scenic_score_helper(trees, row - 1, col, -1, 0, trees[row][col]) * \
        get_scenic_score_helper(trees, row, col - 1, 0, -1, trees[row][col]) * \
        get_scenic_score_helper(trees, row + 1, col, 1, 0, trees[row][col]) * \
        get_scenic_score_helper(trees, row, col + 1, 0, 1, trees[row][col])

def get_scenic_score_helper(trees, row, col, row_dir, col_dir, height):
    if row < 0 or col < 0 or row >= len(trees) or col >= len(trees[0]):
        return 0

    if height <= trees[row][col]:
        return 1

    return 1 + get_scenic_score_helper(trees, row + row_dir, col + col_dir, row_dir, col_dir, height)

file = open('day8_input.txt', 'r')
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]

trees = []

tree = []
for line in lines:
    tree_list = []
    for tree in line:
        tree_list.append(int(tree))
    trees.append(tree_list)

score = 0
for row in range(len(trees)):
    for col in range(len(trees[0])):
        score = max(score, get_scenic_score(trees, row, col))
print(score)