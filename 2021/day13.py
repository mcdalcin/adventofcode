from copy import copy, deepcopy
from pandas import DataFrame
import pandas



file = open('day13_input.txt', 'r')
file_lines = [x.strip() for x in file.readlines()]

# first read in x and y's..

init_coordinates = []
folds = []

is_separator = False
for line in file_lines:
    if line == '':
        is_separator = True
        continue

    if is_separator:
        # we are on fold lines..
        fold = (line.split()[2]).split('=')
        folds.append([fold[0], int(fold[1])])

    if not is_separator:
        # we are on coordinates
        coordinate = line.split(',')
        init_coordinates.append([int(coordinate[0]), int(coordinate[1])])

# get max x and y
max_x = init_coordinates[0][0]
max_y = init_coordinates[0][1]
for i in range(1, len(init_coordinates)):
    max_x = max(max_x, init_coordinates[i][0])
    max_y = max(max_y, init_coordinates[i][1])

# max x = column length,
# max y = row length
dots = []
for i in range(max_y + 1):
    dots.append([False] * (max_x + 1))


# now add dots.. as per coordinates
for coordinate in init_coordinates:
    dots[coordinate[1]][coordinate[0]] = True

# now do the folds.. for horizontal folds ('y') fold paper up.

num_fold = 0
for fold in folds:
    if fold[0] == 'y':
        # horizontal fold.
        # dots along coordinate disappear.
        pos = fold[1]
        dots_copy = deepcopy(dots)
        # remove all after pos including pos.
        dots_copy = dots_copy[:pos]
        # then dots after pos are mirrored upwards.
        for i in range(1, len(dots) - pos):
            # dots_copy[pos-i] = bitwise or of dots[pos-i] and dots[pos+i]
            for j in range(len(dots[0])):
                dots_copy[pos - i][j] = dots[pos - i][j] or dots[pos + i][j]
        dots = dots_copy

    if fold[0] == 'x':
        # vertical fold.
        # dots along coordinate disappear..
        pos = fold[1]
        dots_copy = deepcopy(dots)
        # remove all after pos including pos.
        for i in range(len(dots_copy)):
            dots_copy[i] = dots_copy[i][:pos]
        for i in range(1, len(dots[0]) - pos):
            for j in range(len(dots)):
                dots_copy[j][pos - i] = dots[j][pos - i] or dots[j][pos + i]

        dots = dots_copy

    # count visible dots..
    num_fold += 1
    num_dots = 0
    for dot in dots:
        num_dots += sum(dot)

    print('iteration: ' + str(num_fold) + ' num_dots: ' + str(num_dots))

# need to pretty print it..
dots_pretty = []
for dot in dots:
    dots_pretty.append(['#' if x else '.' for x in dot])

pandas.set_option("display.max_rows", None, "display.max_columns", None)


print(DataFrame(dots_pretty))