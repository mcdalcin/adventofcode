import sys

file = open('day7_input.txt', 'r')
fileLines = file.readlines()

nums = [int(x) for x in fileLines[0].split(',')]

# brute force -- get min and max pos.
minPos = nums[0]
maxPos = nums[0]
for num in nums:
    minPos = min(minPos, num)
    maxPos = max(maxPos, num)


minFuel = sys.maxsize
# calculate total fuel cost for each dist
fuelCost = [0] * (maxPos + 1)
fuelCost[0] = 0
for i in range(1, maxPos + 1):
    fuelCost[i] = fuelCost[i - 1] + i
for pos in range(minPos, maxPos):
    # calc total fuel for each crab.
    fuelSum = 0
    for num in nums:
        dist = abs(num - pos)
        fuelSum += fuelCost[dist]
        if fuelCost[dist] == 0:
            print("what?")
    minFuel = min(minFuel, fuelSum)

    print(pos)

print(minFuel)
