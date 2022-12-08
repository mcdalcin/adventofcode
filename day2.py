import sys

file = open('day2_input.txt', 'r')
lines = file.readlines()

score = 0
for line in lines:
    x = line.split()
    if x[1] == 'X':

        score += 0

        if x[0] == 'A':
            score += 3
        if x[0] == 'B':
            score += 1
        if x[0] == 'C':
            score += 2

    if x[1] == 'Y':
        score += 3
        if x[0] == 'A':
            score += 1
        if x[0] == 'B':
            score += 2
        if x[0] == 'C':
            score += 3

    if x[1] == 'Z':
        score += 6
        if x[0] == 'A':
            score += 2
        if x[0] == 'B':
            score += 3
        if x[0] == 'C':
            score += 1

print(score)

