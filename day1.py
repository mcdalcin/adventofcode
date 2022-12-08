import sys

file = open('day1_input.txt', 'r')
lines = file.readlines()

total_calories = []

curr_calories = 0
for line in lines:
    if line == '\n':
        total_calories.append(curr_calories)
        curr_calories = 0
    else:
        curr_calories += int(line)

total_calories.sort(reverse=True)

print(sum(total_calories[0:3]))