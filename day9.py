def is_adjacent(row_1, col_1, row_2, col_2):
    # get distance between each
    return abs(row_1 - row_2) <= 1 and abs(col_1 - col_2) <= 1

def get_new_row_col(head_row, head_col, tail_row, tail_col):
    if is_adjacent(head_row, head_col, tail_row, tail_col):
        return tail_row, tail_col

    # move towards head by one step
    row_dist = head_row - tail_row
    col_dist = head_col - tail_col
    row_dist = max(-1, min(1, row_dist))
    col_dist = max(-1, min(1, col_dist))
    return tail_row + row_dist, tail_col + col_dist

file = open('day9_input.txt', 'r')
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]

head_row = 0
head_col = 0
tails_row_col = []
for i in range(9):
    tails_row_col.append([0, 0])

tail_locations = set()
tail_locations.add((0, 0))
for line in lines:
    movement = line.split(' ')

    for i in range(int(movement[1])):
        if movement[0] == 'U':
            head_row -= 1
        if movement[0] == 'D':
            head_row += 1
        if movement[0] == 'L':
            head_col -= 1
        if movement[0] == 'R':
            head_col += 1

        curr_row = head_row
        curr_col = head_col
        for j in range(len(tails_row_col)):
            new_row_col = get_new_row_col(curr_row, curr_col, tails_row_col[j][0], tails_row_col[j][1])
            tails_row_col[j][0] = new_row_col[0]
            tails_row_col[j][1] = new_row_col[1]
            curr_row = tails_row_col[j][0]
            curr_col = tails_row_col[j][1]

        tail_locations.add((tails_row_col[8][0], tails_row_col[8][1]))

print(len(tail_locations))


