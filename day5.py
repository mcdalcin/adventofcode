import sys
import string

def get_crate_list(line):
    crates = line.split(" ")

    crate_list = []

    count = 0
    for crate in crates:
        if crate == '':
            count += 1

            if count == 4:
                crate_list.append('')
                count = 0
        else:
            crate_list.append(crate)

    return crate_list

file = open('day5_input.txt', 'r')
lines = file.readlines()

stacks = []
moves = []

done_with_crates = False
start_moving = False


lines = [line.replace('\n', '') for line in lines]

# get number of crate
num_crates = len(get_crate_list(lines[0]))
for i in range(num_crates):
    stacks.append([])

for line in lines:
    if len(line) > 0 and line[1] == '1':
        done_with_crates = True

    if len(line) > 0 and line[0] == 'm':
        start_moving = True

    if not done_with_crates:
        crates = get_crate_list(line)
        for i in range(len(crates)):
            crate = crates[i]
            if crate != '':
                stacks[i].append(crate)

    if start_moving:
        move = line.split(' ')
        moves.append((int(move[1]), int(move[3]), int(move[5])))

for move in moves:
    from_index = move[1] - 1
    to_index = move[2] - 1

    crates_to_move = []
    for i in range(move[0]):
        crates_to_move.insert(0, stacks[from_index].pop(0))

    for crate in crates_to_move:
        stacks[to_index].insert(0, crate)


top_crates = [crates[0] for crates in stacks]

print(top_crates)