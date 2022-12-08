from pandas import *

graph = dict()

# count paths to end node.
def count_paths(node, visited, has_visited_small_cave_twice):
    if node == 'end':
        return 1

    if node.islower() and node in visited and has_visited_small_cave_twice:
        return 0

    # start can only be visited once
    if node.islower() and node in visited and node == 'start':
       return 0

    # otherwise, check if we have already visited it,
    if node.islower() and node in visited:
        has_visited_small_cave_twice = True

    node_added = False
    if node.islower() and not (node in visited):
        node_added = True
        visited.add(node)
    num_paths = 0
    neighbors = graph[node]
    for neighbor in neighbors:
        num_paths += count_paths(neighbor, visited, has_visited_small_cave_twice)

    # when we come up from our function, backtrack visited set.
    if node_added:
        visited.remove(node)
    return num_paths


file = open('day12_input.txt', 'r')
file_lines = [x.strip() for x in file.readlines()]

# create graph of nodes...
# use a list of neighbors to define the graph
# dict -> list of neighbors.

for line in file_lines:
    nodes = line.split('-')
    if not nodes[0] in graph:
        graph[nodes[0]] = set()
    if not nodes[1] in graph:
        graph[nodes[1]] = set()

    graph[nodes[0]].add(nodes[1])
    graph[nodes[1]].add(nodes[0])

# once we have this.. starting at Start.. lets recursively go through and count the paths..
# note we can visit little nodes once and big caves as many times as we want..
visited_set = set()
count = count_paths('start', visited_set, False)

print(count)

