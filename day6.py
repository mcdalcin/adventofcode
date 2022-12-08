import sys
import string

file = open('day6_input.txt', 'r')
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]

line = lines[0]

for i in range(len(lines[0])):
    # i -> i + 4
    if i + 14 > len(lines[0]):
        break
    four = line[i:i+14]
    unique = True
    for j in range(len(four) - 1):
        if four[j] in four[j+1:]:
            unique = False
            break

    if unique:
        print(four)
        print(i)
        break