from collections import Counter
from line_profiler_pycharm import profile
from copy import copy, deepcopy
from pandas import DataFrame
import pandas
import sys
import time
from heapq import *
import numpy as np


def mod_risk(val):
    if val >= 10:
        val = (val % 10) + 1
    return val


def in_bounds(g, x, y):
    return 0 <= x < len(g[0]) and 0 <= y < len(g)

def shortest_path(g, node):
    distances = dict()
    distances[node] = 0

    min_heap = [(0, node)]

    visited = set()

    while min_heap:
        distance, min_node = heappop(min_heap)

        while min_node in visited:
            distance, min_node = heappop(min_heap)

        visited.add(min_node)

        # can go up, down, left, or right.
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for dir in dirs:
            new_node = (min_node[0] + dir[0], min_node[1] + dir[1])
            if new_node in visited or not in_bounds(g, new_node[0], new_node[1]):
                continue

            new_dist = distance + g[new_node[1]][new_node[0]]
            if new_node not in distances or new_dist < distances[new_node]:
                distances[new_node] = new_dist
                heappush(min_heap, (new_dist, new_node))

    return distances


file = open('day15_input.txt', 'r')
file_lines = [x.strip() for x in file.readlines()]

#start top  left
# destination is bottom right
# each number is risk level..
# add up each position you enter (dont count unless you enter, leaving does not count it)
# find path with lowest total risk..
# dijkstrah algorithm...

# read in graph, 2d array is fine for the graph..

# build graph..

graph = []
for line in file_lines:
    graph.append([int(x) for x in line])

new_graph = np.array(graph)

mod_func = np.vectorize(mod_risk)

# make 25 tiles then concatenate them all.
tiles = []
for i in range(5):
    tiles_row = []
    for j in range(5):
        # add i + j to new_graph and append.
        tile = new_graph + (i + j)
        tile = mod_func(tile)
        tiles_row.append(tile)
    tiles.append(tiles_row)

# now combine tiles in tiles_row
tiles_combined = []
for tiles_row in tiles:
    tiles_combined.append(np.concatenate(tiles_row, axis = 0))

# now combine tiles_combined
entire_graph = np.concatenate(tiles_combined, axis = 1)

# initial graph of
# 1, 1
# 1, 1
# would go to
# 1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
# 1, 1, 2, 2, 3, 3, 4, 4, 5, 5
# 2d, 2, 3, 3, 4, 4, 5, 5, 6, 6
# ...
# 5, 5, 6, 6, 7, 7, 8, 8, 9, 9
# 5, 5, 6, 6, 7, 7, 8, 8, 9, 9

start_time = time.time()
d = shortest_path(entire_graph, (0, 0))
elapsed_time = time.time() - start_time

print("elapsed time: " + str(elapsed_time))
