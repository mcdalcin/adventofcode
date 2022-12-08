import sys

file = open('day2_input.txt', 'r')
lines = file.readlines()


curr_x = 0
curr_y = 0
aim = 0

for line in lines:
    splits = line.split()
    command = splits[0]
    distance = int(splits[1])

    if command == 'forward':
        curr_x += distance
        curr_y += aim * distance

    if command == 'down':
        aim += distance

    if command == 'up':
        aim -= distance

print("curr_y: " + str(curr_y) + " curr_x: " + str(curr_x) + "; multiplied: " + str(curr_y * curr_x))
