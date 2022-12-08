import sys

file = open('day1_input.txt', 'r')
lines = file.readlines()

nums = [int(i) for i in lines]

increase_count = 0
prev_num = sys.maxsize

prev_sum = nums[0] + nums[1] + nums[2];
for i in range(3, len(nums)):
    curr_sum = prev_sum - nums[i-3] + nums[i]
    if curr_sum > prev_sum:
        increase_count += 1
    prev_sum = curr_sum

print("Increase count: " + str(increase_count))