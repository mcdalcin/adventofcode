from collections import Counter
from line_profiler_pycharm import profile
from copy import copy, deepcopy
from pandas import DataFrame
import pandas
import sys
import time
from heapq import *
import numpy as np

def calculate_packet_value(id, sub_packet_values):
    # ids
    # 0 -> sum packets, value = sum of values.
    # 1 -> product packets
    # 2 -> min packets
    # 3 -> max packets
    # 5 greater than packets -> 1 if value of first is greater than value of 2nd, otherwise 0.
    # 6 less than packets
    # 7 equal to packets
    if id == 0:
        return sum(sub_packet_values)
    if id == 1:
        product = sub_packet_values[0]
        for v in sub_packet_values[1:]:
            product *= v
        return product
    if id == 2:
        return min(sub_packet_values)
    if id == 3:
        return max(sub_packet_values)
    if id == 5:
        return 1 if sub_packet_values[0] > sub_packet_values[1] else 0
    if id == 6:
        return 1 if sub_packet_values[0] < sub_packet_values[1] else 0
    if id == 7:
        return 1 if sub_packet_values[0] == sub_packet_values[1] else 0


def parse_packet(packet_binary_str, versions):
    value = None
    i = 0
    # get version and id, then increment +6
    version_bin = packet_binary_str[i:i + 3]
    id_bin = packet_binary_str[i + 3:i + 6]
    curr_version = int(version_bin, 2)
    curr_id = int(id_bin, 2)
    versions.append(curr_version)
    i += 6

    if curr_id == 4:
        # continue on in groups of 5 bits, looking for last group (first bit = 0)
        literal_bin_str = ''
        while True:
            curr_group = packet_binary_str[i:i+5]
            literal_bin_str += curr_group[1:]
            i += 5
            if curr_group[0] == '0':
                break
        # i is now at the start of the extra 0s. we can just ignore.
        value = int(literal_bin_str, 2)
    else:
        # operator packet
        length_type_id = packet_binary_str[i]
        i += 1
        sub_packet_values = []
        if length_type_id == '0':
            # next 15 bits are a number that represent the total length in bits of the sub-packets contained in this packet.
            total_length = int(packet_binary_str[i:i+15], 2)
            i += 15
            bits_remaining = total_length

            while bits_remaining > 0:
                packet_length, packet_value = parse_packet(packet_binary_str[i:i+bits_remaining], versions)
                i += packet_length
                bits_remaining -= packet_length
                sub_packet_values.append(packet_value)
        if length_type_id == '1':
            # next 11 bits represent how many packets are contained.
            total_sub_packets = int(packet_binary_str[i:i+11], 2)
            i += 11
            sub_packets_remaining = total_sub_packets

            while sub_packets_remaining > 0:
                packet_length, packet_value = parse_packet(packet_binary_str[i:], versions)
                i += packet_length
                sub_packets_remaining -= 1
                sub_packet_values.append(packet_value)

        value = calculate_packet_value(curr_id, sub_packet_values)

    return i, value # i ends up being the total size of the parsed packet, value = value of packet

file = open('day16_input.txt', 'r')
file_lines = [x.strip() for x in file.readlines()]

# saved in hexadecimal
# convert hex -> binary

# 0 = 0000
# 1 = 0001
# 2 = 0010
# 3 = 0011
# 4 = 0100
# 5 = 0101
# 6 = 0110
# 7 = 0111
# 8 = 1000
# 9 = 1001
# A = 1010
# B = 1011
# C = 1100
# D = 1101
# E = 1110
# F = 1111

# contains a single packet as its outermost layer, which contains many other packets?? hex might encode a few extra 0 bits at the end; ignore.
# 3 bits, 3 bits,
# packet version, packet type ID
# packets with type id 4 represent literal value. they encode a single binary number. binary number is padded with leading zeroes until its length is a multiple of four bits.
# thten broken into groups of four bits.

#every other type of packet represent an operator that performs some calculation.
# bit immediately after the packet header.. if 0, next 15 bits are a number that represents the total length in bits of sub packets contained.
# if 1, the next 11 bits are a number that ...

#then the sub packets appear.


versions = []

h = file_lines[0]

# zfill pads with 0's in beginning, python automatically strips them.
total_size = len(h) * 4

# [2:] gets rid of 0b that python adds on.
binary_str = bin(int(h, 16))[2:].zfill(total_size)

# maintain a state-machine approach.

# 1. parse_packet_header (get both version and id)
# 2. if operator
# 2a. parse next bit, 0 -> next 15 bits, 1 -> next 11 bits.
# 3. if id = 4, literal value
# 3a. traverse 5 bits at a time, looking for last group (1st bit of group will be 0).
# note: total size is a multiple of 4. there may be extra 0's at the end of a packet. ignore those.
length, value = parse_packet(binary_str, versions)

print(versions)
print(sum(versions))
print('length: ' + str(length) + ' value: ' + str(value))