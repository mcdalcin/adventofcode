import sys

file = open('day6_input.txt', 'r')
fileLines = file.readlines()

nums = [int(x) for x in fileLines[0].split(',')]

print(nums)

fish = [0] * 9
for num in nums:
    fish[num] += 1

for i in range(256):
    # fish[0] -> fish[8] += fish[0] and fish[6] += fish[0] + fish[7]
    # fish[1] -> fish[0]
    # fish[2] -> fish[1]
    # ...
    # fish[6] -> fish[5]
    # special ones are fish[7] and fish[0]

    fishCopy = fish.copy()

    for num in range(8):
        fish[num] = fishCopy[num + 1]

    fish[8] = fishCopy[0]
    fish[6] = fishCopy[0] + fishCopy[7]

    print(i)

print(sum(fish))
