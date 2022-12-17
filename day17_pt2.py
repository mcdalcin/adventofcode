import re

y_diff = 1060007
cycle = [
    151427,
    151427,
    151427,
    151432,
    151432,
    151428,
    151429,
    151430
]
more_to_stop = 999999300000
rocks_per_unit = 100000

print(cycle[0:1])

i = 0
while more_to_stop != 0:
    y_diff += cycle[i]
    more_to_stop -= rocks_per_unit
    i = (i + 1) % len(cycle)

print(y_diff)