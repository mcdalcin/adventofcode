import math
import copy
import heapq as heap
import numpy as np


def is_neighbor(nodes, pos_1, pos_2):
    # make sure pos_2 is in bounds.
    if pos_2[0] < 0 or pos_2[0] >= len(nodes) or pos_2[1] < 0 or pos_2[1] >= len(nodes[0]):
        return False
    char_pos_1 = nodes[pos_1[0]][pos_1[1]]
    char_pos_2 = nodes[pos_2[0]][pos_2[1]]

    if char_pos_1 == 'S':
        char_pos_1 = 'a'
    if char_pos_2 == 'E':
        char_pos_2 = 'z'

    return ord(char_pos_2) - ord(char_pos_1) <= 1

def dijkstra(nodes, starting_pos):
    visited = set()
    # parentsMap = {}
    pq = []
    node_costs = dict()
    node_costs[starting_pos] = 0
    heap.heappush(pq, (0, starting_pos))

    while pq:
        _, node_pos = heap.heappop(pq)
        visited.add(node_pos)

        # go up, left, down, right. they are neighbors if they are not more than 1 greater.
        potential_neighbors = [tuple(np.add(node_pos, add)) for add in [(-1, 0), (0, -1), (1, 0), (0, 1)]]
        for potential_neighbor in potential_neighbors:
            if is_neighbor(nodes, node_pos, potential_neighbor) and potential_neighbor not in visited:
                if potential_neighbor not in node_costs or node_costs[potential_neighbor] > node_costs[node_pos] + 1:
                    node_costs[potential_neighbor] = node_costs[node_pos] + 1
                    heap.heappush(pq, (node_costs[potential_neighbor], potential_neighbor))

    return node_costs

file = open('day12_input.txt', 'r')
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]

chars = []
for line in lines:
    chars.append(list(line))

# find the start row and column in chars
start_positions = []
end_row = 0
end_col = 0
for row in range(len(chars)):
    for col in range(len(chars[row])):
        if chars[row][col] == 'S':
            start_positions.append((row, col))
            chars[row][col] = 'a'
        if chars[row][col] == 'E':
            end_row = row
            end_col = col
            chars[row][col] = 'z'
        if chars[row][col] == 'a':
            start_positions.append((row, col))

node_costs = []
print(len(start_positions))
for start_position in start_positions:
    node_costs.append(dijkstra(chars, start_position))

print(min([node_costs[(end_row, end_col)] if (end_row, end_col) in node_costs else 1000000000000000000 for node_costs in node_costs]))
