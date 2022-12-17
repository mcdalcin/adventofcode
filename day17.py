import re

file = open('day17_input.txt', 'r')
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]

rocks = [
    [['#', '#', '#', '#']],
    [['.', '#', '.'],
     ['#', '#', '#'],
     ['.', '#', '.']],
    [['.', '.', '#'],
     ['.', '.', '#'],
     ['#', '#', '#']],
    [['#'],
     ['#'],
     ['#'],
     ['#']],
    [['#', '#'],
     ['#', '#']]]


# vertical chamber is exactly seven units wide
# each rock starts so its left edge is two units away from the left wall
# bottom edge is three units above the highest rock in the room (or floor if none)

# push by jet, then move down
# if rock cannot move down, rock stops where it is
# next rock goes up

def get_new_rock_positions(max_y_inner, rock):
    new_rock_positions = set()
    top_left_pos = (2, max_y_inner + 4 + len(rock) - 1)
    for y in range(len(rock)):
        for x_idx in range(len(rock[y])):
            if rock[y][x_idx] == '#':
                new_rock_positions.add((top_left_pos[0] + x_idx, top_left_pos[1] - y))
    return new_rock_positions


def push_rock_positions(x_add, rock_positions_2, all_rock_positions):
    # check if we can push the rock.
    # if we can, then move it, otherwise, don't move it.
    new_rock_positions = set()
    for rock_pos_2 in rock_positions_2:
        new_pos = (rock_pos_2[0] + x_add, rock_pos_2[1])
        if new_pos in all_rock_positions or new_pos[0] < 0 or new_pos[0] > max_x:
            return rock_positions_2
        new_rock_positions.add((rock_pos_2[0] + x_add, rock_pos_2[1]))
    return new_rock_positions


def can_move_down(rock_positions, all_rock_positions):
    new_rock_positions = set()
    for rock_pos_2 in rock_positions:
        new_pos = (rock_pos_2[0], rock_pos_2[1] - 1)
        if new_pos in all_rock_positions or new_pos[1] < 0:
            return False, rock_positions
        new_rock_positions.add(new_pos)
    return True, new_rock_positions


max_y = -1  # highest rock
max_x = 6

current_rock_index = 0
current_rock_positions = get_new_rock_positions(max_y, rocks[current_rock_index])

rock_positions = set()
num_rocks_stopped = 0
current_char_index = 0
prev_max_y = -1
diffs = []
count_rocks = 0
while num_rocks_stopped < 10000:
    c = lines[0][current_char_index]
    # store location for each part of rock.
    # push rock by jet
    current_rock_positions = push_rock_positions(1 if c == '>' else -1, current_rock_positions, rock_positions)

    # move rock down
    can_move, pos = can_move_down(current_rock_positions, rock_positions)
    current_char_index = (current_char_index + 1) % len(lines[0])

    if can_move:
        current_rock_positions = pos

    else:
        # add rock to all rock positions
        for rock_pos in current_rock_positions:
            rock_positions.add(rock_pos)
        # get new rock
        current_rock_index = (current_rock_index + 1) % len(rocks)
        # get max y in current_rock_positions
        max_y = max(max_y, max([pos[1] for pos in current_rock_positions]))
        current_rock_positions = get_new_rock_positions(max_y, rocks[current_rock_index])
        num_rocks_stopped += 1

        count_rocks += 1
        if num_rocks_stopped % 1 == 0:
            diff = max_y - prev_max_y
            prev_max_y = max_y
            diffs.append(diff)

        # if num_rocks_stopped % 100000 == 0:
        #     diff = max_y - prev_max_y
        #     prev_max_y = max_y
        #     print(diff)
        all_max_y = True
        for x in range(max_x + 1):
            if (x, max_y) not in rock_positions:
                all_max_y = False
                break
        if all_max_y:
            print('tes2t')

cycle = []
cycle_start_idx = 0

# try to find a cycle
for i in range(len(diffs) // 2):
    end_idx = len(diffs) - 1
    start_idx = end_idx - i
    size = end_idx - start_idx + 1
    if size < 100:
        continue
    if diffs[start_idx:] == diffs[start_idx - size:start_idx]:
        print('found cycle! size: ' + str(size) + ' sum: ' + str(sum(diffs[start_idx:])) + ' start_idx: ' + str(start_idx))

        print(diffs[start_idx:])
        print(diffs[start_idx - size:start_idx])
        cycle = diffs[start_idx:]
        cycle_start_idx = start_idx
        break

# once we have cycle,
rocks_remaining = 1000000000000 - cycle_start_idx

num_cycles_in_rocks_remaining = rocks_remaining // len(cycle)
total_height = sum(diffs[0:cycle_start_idx]) + num_cycles_in_rocks_remaining * sum(cycle)
rocks_remaining = rocks_remaining % len(cycle)

# go through remaining rocks one at a time.
i = 0
while rocks_remaining != 0:
    total_height += cycle[i]
    i = (i + 1) % len(cycle)
    rocks_remaining -= 1

print(total_height)
