import sys
import string

def calculatePriority(letter):
    return string.ascii_letters.index(letter) + 1

def findPriority(first_sack, second_sack, third_sack):
    for i in range(0, len(first_sack)):
        for j in range(0, len(second_sack)):
            if first_sack[i] == second_sack[j]:
                for z in range(0, len(third_sack)):
                    if first_sack[i] == third_sack[z]:
                        return calculatePriority(first_sack[i])
    return 0


file = open('day3_input.txt', 'r')
lines = file.readlines()

sum_priorities = 0
i = 0
while i < len(lines):
    line1 = lines[i][:-1]
    line2 = lines[i + 1][:-1]
    line3 = lines[i + 2][:-1]

    sum_priorities += findPriority(line1, line2, line3)

    i+=3

print(sum_priorities)