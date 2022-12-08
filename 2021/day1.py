import sys

file = open('day1_input.txt', 'r')
lines = file.readlines()

nums = [int(i) for i in lines]

increase_count = 0
prev_num = sys.maxsize

for num in nums:
    if num > prev_num:
        increase_count += 1
    prev_num = num

print("Increase count: " + str(increase_count))