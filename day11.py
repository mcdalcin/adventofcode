import math
import copy


file = open('day11_input.txt', 'r')
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]

#items = [[79, 98], [54, 65, 75, 74], [79,60,97], [74]]

items = [[89,74], [75, 69, 87, 57, 84, 90, 66, 50], [55], [69, 82, 69, 56, 68],
         [72, 97, 50], [90, 84, 56, 92, 91, 91],[63, 93, 55, 53],[50, 61, 52, 58, 86, 68, 97]]
test_nums = [17, 7, 13, 2, 19, 3, 5, 11]
#test_nums = [23, 19, 13, 17]

items_modulus = []

for i in range(len(items)):
    # each monkey cares about all the items..
    items_modulus.append(copy.deepcopy(items))

for i in range(len(items_modulus)):
    i_list = items_modulus[i]
    for j in i_list:
        for k in range(len(j)):
            j[k] = j[k] % test_nums[i]


operations = [lambda old : old * 5, lambda old : old + 3, lambda old : old + 7, lambda old : old + 5, lambda old : old + 2, lambda old : old * 19, lambda old : old * old, lambda old : old + 4]

#operations = [lambda old: old * 19, lambda old: old + 6, lambda old: old * old, lambda old: old + 3]

tests = [lambda worry : 4 if worry % 17 == 0 else 7, lambda worry : 3 if worry % 7 == 0 else 2, lambda worry : 0 if worry % 13 == 0 else 7, lambda worry : 0 if worry % 2 == 0 else 2, lambda worry : 6 if worry % 19 == 0 else 5, lambda worry : 6 if worry % 3 == 0 else 1, lambda worry : 3 if worry % 5 == 0 else 1, lambda worry : 5 if worry % 11 == 0 else 4]
#tests = [lambda worry: 2 if worry % 23 == 0 else 3, lambda worry: 2 if worry % 19 == 0else 0, lambda worry: 1 if worry % 13 == 0 else 3, lambda worry: 0 if worry % 17 == 0 else 1]


round = 0

monkeys_inspect_count = []
for i in range(len(items)):
    monkeys_inspect_count.append(0)

for round in range(10000):
    for i in range(len(items)):
        for j in range(len(items[i])):
            # i is the current monkey we're on.
            # j is the current item we're on.
            item_worry = items_modulus[i][i][j]
            new_item_worry = operations[i](item_worry)
            new_monkey = tests[i](new_item_worry)

            # put into num into new_monkey list for each items_modulus.
            for k in range(len(items_modulus)):
                monkey_item_worry = items_modulus[k][i][j]
                new_monkey_item_worry = operations[i](monkey_item_worry)
                items_modulus[k][new_monkey].append(new_monkey_item_worry % test_nums[k])

            # put also into items so we can easily see what's going on. we don't we have to use the new item worry, since its only being used to track.
            items[new_monkey].append(items[i][j])
            monkeys_inspect_count[i] += 1
        items[i] = []
        for k in range(len(items_modulus)):
            items_modulus[k][i] = []
    if round % 100 == 0:
        print(round)

print(items)
print(monkeys_inspect_count)
monkeys_inspect_count.sort()
print(monkeys_inspect_count)
print(items)
