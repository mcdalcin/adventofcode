import sys

def is_open(c):
    return c == '[' or c == '{' or c == '(' or c == '<'

def get_open_counterpart(c):
    if c == ']':
        return '['
    if c == '}':
        return '{'
    if c == ')':
        return '('
    if c == '>':
        return '<'

    return None

file = open('day10_input.txt', 'r')
file_lines = [x.strip() for x in file.readlines()]

#corrupted line - closes with the wrong character
# we can do push pop...
# push -> open char, pop -> closing char.
# on pop, closing char must match open char pair.

incomplete_chars_list = []
for line in file_lines:
    queue = []
    is_corrupted = False
    for c in line:
        if is_open(c):
            queue.append(c)
        else:
            pop_char = queue.pop()
            if get_open_counterpart(c) != pop_char:
                is_corrupted = True
                break
    if len(queue) > 0 and not is_corrupted:
        # incomplete, in order to complete it, pop all.
        incomplete_chars = []
        while len(queue) > 0:
            incomplete_chars.append(queue.pop())
        incomplete_chars_list.append(incomplete_chars)


sums = []
for incomplete_chars in incomplete_chars_list:
    incomplete_chars_sum = 0
    for c in incomplete_chars:
        val = 0
        if c == '(':
            val = 1
        elif c == '[':
            val = 2
        elif c == '{':
            val = 3
        elif c == '<':
            val = 4
        else:
            print('wtf')

        incomplete_chars_sum = incomplete_chars_sum * 5 + val
    sums.append(incomplete_chars_sum)

sorted_sums = sorted(sums)
print(sorted_sums)
print(sorted_sums[int(len(sorted_sums)/2)])