file = open('day10_input.txt', 'r')
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]

cycle = 0
x_register = 1
signals = []
pixels = []
special_cycles = [20, 60, 100, 140, 180, 220]
for line in lines:
    if line == 'noop':
        if x_register - 1 <= (cycle % 40) <= x_register + 1:
            pixels.append('#')
        else:
            pixels.append('.')
        cycle += 1
        if (cycle + 1) in special_cycles:
            print(cycle)
            signals.append(x_register * (cycle + 1))
    else:
        add_value = int(line.split(' ')[1])
        for i in range(2):
            if x_register - 1 <= (cycle % 40) <= x_register + 1:
                pixels.append('#')
            else:
                pixels.append('.')
            cycle += 1
            if i == 1:
                x_register += add_value
            if (cycle + 1) in special_cycles:
                print(str(cycle) + ' ' + str(x_register))
                signals.append(x_register * (cycle + 1))

print(signals)
print([(i + 1) * 20 for i in range(len(signals))])
print(sum(signals))
print(pixels)
for i in range(0, len(pixels), 40):
    print(''.join(pixels[i:i + 40]))
