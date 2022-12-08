import sys
import string
file = open('day4_input.txt', 'r')
lines = file.readlines()

count = 0
for line in lines:
    assignments = line.split(',')
    range1 = assignments[0].split('-')
    range2 = assignments[1].split('-')

    start_1 = int(range1[0])
    start_2 = int(range2[0])
    end_1 = int(range1[1])
    end_2 = int(range2[1])

    if (start_1 >= start_2 and start_1 <= end_2) or (end_1 >= start_2 and end_1 <= end_2) or (start_2 >= start_1 and start_2 <= end_1) or (end_2 >= start_1 and end_2 <= end_1):
        count += 1

print(count)


