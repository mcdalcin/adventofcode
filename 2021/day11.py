from pandas import *


file = open('day11_input.txt', 'r')
file_lines = [x.strip() for x in file.readlines()]

# gains eneryg over time, flashes brightly when full.
# we have starting energies.
# each step, each octupus +1 energy
# any octupus with energy level > 9 flashes. increases all adjacent octopus energy by 1 (diagonally adjacent as well).
# those adjacent also flash if can ( an octopus can flash at most once per step )
# any octopus that flashed has it energy set to 0,

# simulate 100 steps, how many total flashes?

def increment_adjacents(row, col, energies, has_flashed):
    dirs = [-1, 0, 1]
    num_explosions = 0
    for rowAdd in dirs:
        for colAdd in dirs:
            # ignore 0, 0
            if rowAdd == 0 and colAdd == 0:
                continue

            adjacentRow = row + rowAdd
            adjacentCol = col + colAdd
            if in_bound(adjacentRow, adjacentCol, energies) and not has_flashed[adjacentRow][adjacentCol]:
                energies[adjacentRow][adjacentCol] += 1
                # potentially explode star.
                num_explosions += explode(adjacentRow, adjacentCol, energies, has_flashed)
    return num_explosions


def explode(row, col, energies, has_flashed):
    # explode a star > 9
    if energies[row][col] <= 9 or has_flashed[row][col]:
        return 0

    energies[row][col] = 0
    has_flashed[row][col] = True
    return increment_adjacents(row, col, energies, has_flashed) + 1


def in_bound(row, col, energies):
    return row >= 0 and row < len(energies) and col >= 0 and col < len(energies[0])


energy = []
for line in file_lines:
    energy.append([int(x) for x in line.strip()])

num_explosions = 0
# num_explosions -> need to be == 100
for i in range(1, 500):
    curr_explosions = 0
    has_flashed = []
    for j in range(len(energy)):
        has_flashed.append([False] * len(energy))

    energy = [[x+1 for x in y] for y in energy]

    for row in range(len(energy)):
        for col in range(len(energy[0])):
            curr_explosions += explode(row, col, energy, has_flashed)
    if curr_explosions == 100:
        print(i)
    num_explosions += curr_explosions

