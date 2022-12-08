import sys
import string

class Node:
    def __init__(self, name, parent):
        self.parent = parent
        self.children = []
        self.size = 0

    def add_child(self, child):
        self.children.append(child)

    def get_total_size(self):
        total_size = self.size
        for child in self.children:
            total_size += child.get_total_size()
        return total_size

file = open('day7_input.txt', 'r')
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]

nodes = []

curr_node = None
for line in lines:
    if line[0] == '$':
        split = line.split(' ')
        if split[1][0] == 'c':
            # create a new curr_node
            if split[2][0] == '.':
                curr_node = curr_node.parent
            else:
                parent = curr_node
                curr_node = Node(split[2], parent)
                if parent is not None:
                    parent.add_child(curr_node)
                nodes.append(curr_node)

    if line[0].isnumeric():
        # add to curr_node size
        curr_node.size += int(line.split(' ')[0])

filesystem_size = 70000000
needed_space = 30000000
total_size = 0

curr_size = nodes[0].get_total_size()
needed_free_space = needed_space - (filesystem_size - curr_size)
smallest_dir = 10000000000
for node in nodes:
    if node.get_total_size() >= needed_free_space:
        if node.get_total_size() < smallest_dir:
            smallest_dir = node.get_total_size()


print(smallest_dir)