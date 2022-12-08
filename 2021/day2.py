import sys

file = open('day2_input.txt', 'r')
lines = file.readlines()



curr_y = 0
curr_x = 0

for line in lines:
    splits = line.split()
    command = splits[0]
    distance = int(splits[1])

    if command == 'forward':
        curr_x += distance

    if command == 'down':
        curr_y += distance

    if command == 'up':
        curr_y -= distance

print("curr_y: " + str(curr_y) + " curr_x: " + str(curr_x) + "; multiplied: " + str(curr_y * curr_x))
