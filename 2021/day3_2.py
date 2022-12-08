import sys

gamma_rate = ''
epsilon_rate = ''

def calculate_gamma_and_epsilon(gamma_list, epsilon_list):
    global gamma_rate
    global epsilon_rate
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(len(gamma_list[0])):
        num_zeros = 0
        num_ones = 0

        for line in gamma_list:
            if line[i] == '0':
                num_zeros += 1
            else: 
                num_ones += 1

        if num_zeros > num_ones:
            gamma_rate += '0'
        else:
            gamma_rate += '1'
    for i in range(len(epsilon_list[0])):
        num_zeros = 0
        num_ones = 0

        for line in epsilon_list:
            if line[i] == '0':
                num_zeros += 1
            else: 
                num_ones += 1

        if num_zeros > num_ones:
            epsilon_rate += '1'
        else:
            epsilon_rate += '0'


file = open('day3_input.txt', 'r')
lines = file.readlines()
lines_stripped = [i.strip() for i in lines]

oxygen_lines = lines_stripped.copy()
co2_lines = lines_stripped.copy()

# use gamma rate for oxygen, epsilon rate for co2


calculate_gamma_and_epsilon(oxygen_lines, co2_lines)
print(gamma_rate)
print(epsilon_rate)
for i in range(len(gamma_rate)):
    if (len(oxygen_lines) == 1 and len(co2_lines) == 1):
        break

    calculate_gamma_and_epsilon(oxygen_lines, co2_lines)

    gamma_bit = gamma_rate[i]
    epsilon_bit = epsilon_rate[i]
    
    if (len(oxygen_lines) != 1):
        oxygen_lines = [x for x in oxygen_lines if x[i] == gamma_bit]
    
    if (len(co2_lines) != 1):
        co2_lines = [x for x in co2_lines if x[i] == epsilon_bit]


print(oxygen_lines)
print(co2_lines)
