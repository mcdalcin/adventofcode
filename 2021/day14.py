from collections import Counter
from line_profiler_pycharm import profile
from copy import copy, deepcopy
from pandas import DataFrame
import pandas


class Node:
    def __init__(self, letter, next):
        self.letter = letter
        self.next = next

    @profile
    def to_string(self):
        string = ''
        n = self
        while n is not None:
            string += n.letter
            n = n.next
        return string

@profile
def do_code(initial_node):
    for i in range(15):
        node = initial_node
        while node.next is not None:
            nextNode = node.next
            pair = node.letter + node.next.letter
            if pair in insertion_rules:
                node.next = Node(insertion_rules[pair], nextNode)
            node = nextNode

        print(i)
        # now get most common and least common elements..
        common_chars = Counter(init_node.to_string()).most_common()

        print(common_chars[0])
        print(common_chars[-1:])

def add_pair_to_count(pair, counts, num_times):
    if pair in counts:
        counts[pair] = counts[pair] + num_times
    else:
        counts[pair] = num_times

def remove_pair_from_count(pair, counts, num_times):
    counts[pair] = counts[pair] - num_times

file = open('day14_input.txt', 'r')
file_lines = [x.strip() for x in file.readlines()]

# ffirst line = polymer template
# next sections define pair insertion rules..
# AB -> C means when A and B are immediately adjacent, elemtn C should be inserted between them.
# simulataneously... NNCB NN NC CB

# get all pairs..
# do mappings on them
# combine the pairs.

# NN NC CB
# -> NCN NBC CHB
# -> to combine, its not as simple as adding them together..
# if 3 letters -> add first two letters
# if 2 letters -> add first letter
# if last pair, add all letters.

# need a dict of the mappings.
insertion_rules = dict()

polymer = file_lines[0]

for i in range(2, len(file_lines)):
    split_line = file_lines[i].split()
    insertion_rules[split_line[0]] = split_line[2]

pair_counts = dict()
for i in range(len(polymer) - 1):
    add_pair_to_count(polymer[i] + polymer[i+1], pair_counts, 1)

# now perform code on init_pairs..
# each pair creates two potentially
# pair[0] + letter and letter + pair[1], increment.
for i in range(40):
    pair_counts_new = dict()
    for key in pair_counts:
        if key in insertion_rules:
            letter = insertion_rules[key]
            num_times = pair_counts[key]
            add_pair_to_count(key[0] + letter, pair_counts_new, num_times)
            add_pair_to_count(letter + key[1], pair_counts_new, num_times)
        elif pair_counts[key] != 0:
            # add whatever is in there..unless the num is 0
            num_times = pair_counts[key]
            add_pair_to_count(key, pair_counts_new, num_times)
    pair_counts = pair_counts_new

# now go through and count all letters, put into map?
letter_counts = dict()
for key in pair_counts:
    # count first letter only, this will lead to of by one error for last letter in polymer.
    letter_counts[key[0]] = letter_counts.get(key[0], 0) + pair_counts[key]

# add last letter in
last_letter = polymer[-1:]
letter_counts[last_letter] = letter_counts.get(last_letter, 0) + 1

print(pair_counts)
print(letter_counts)
print(max(letter_counts.values()))
print(min(letter_counts.values()))
print(max(letter_counts.values()) - min(letter_counts.values()))


