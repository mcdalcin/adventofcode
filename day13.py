import math
import copy
import heapq as heap
from functools import cmp_to_key

import numpy as np
import ast


def compare_ints(left, right):
    return right - left


def compare_list(left, right):
    for index in range(len(left)):
        if index >= len(right):
            # -1 means out of order entirely.
            return -1
        left_element = left[index]
        right_element = right[index]
        ret = compare(left_element, right_element)
        if ret != 0:
            return ret
    if len(left) < len(right):
        return 1
    return 0


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return compare_ints(left, right)
    elif isinstance(left, list) and isinstance(right, list):
        return compare_list(left, right)

    if isinstance(left, int) and isinstance(right, list):
        # convert left to a list and try again.
        left = [left]
        return compare(left, right)
    elif isinstance(left, list) and isinstance(right, int):
        # convert right to a list and try again.
        right = [right]
        return compare(left, right)

    # invalid
    print("Should never get here.")
    return -1


file = open('day13_input.txt', 'r')
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]

pairs = []
all_lists = []
i = 0
while i < len(lines):
    if lines[i] == "":
        i += 1
        continue

    all_lists.append(ast.literal_eval(lines[i]))
    all_lists.append(ast.literal_eval(lines[i + 1]))
    pairs.append((ast.literal_eval(lines[i]), ast.literal_eval(lines[i + 1])))
    i += 2

sum_indices = 0
for i in range(len(pairs)):
    if compare(pairs[i][0], pairs[i][1]) >= 0:
        sum_indices += (i + 1)
        print(i + 1)

print(sum_indices)

sorted_list = sorted(all_lists, key=cmp_to_key(compare), reverse=True)
for i in range(len(sorted_list)):
    if sorted_list[i] == [[2]] or sorted_list[i] == [[6]]:
        print(str(i + 1) + " index")

#print(*sorted(all_lists, key=cmp_to_key(compare), reverse=True), sep='\n')