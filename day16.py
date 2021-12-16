from utils import get_input
import numpy as np

def part1(data):
    binary_string = bin(int(data, 16))[2:].zfill(len(data)*4)

    i = 0
    sum_versions = 0
    while i < len(binary_string):

        if int(binary_string[i:]) == 0:
            break

        version, type_id, length, val = read_next_packet(binary_string[i:])

        i += length
        sum_versions += version

    return sum_versions

def read_next_packet(binary_data):

    version = int(binary_data[0:3],2)
    type_id = int(binary_data[3:6],2)

    i = 6
    if type_id == 4: # literal value
        number = '' 
        while binary_data[i]=='1':
            number += binary_data[i+1:i+5]
            i+=5
        number += binary_data[i+1:i+5]
        number = int(number,2)
        return version, type_id, i+5, number

    else: # operator
        if binary_data[i] == '0': #15-bit
            sub_length = int(binary_data[i+1:i+16],2)
            return version, type_id, i+16, ('L',sub_length)
        else: #11-bit
            sub_packets = int(binary_data[i+1:i+12],2)
            return version, type_id, i+12, ('N',sub_packets)

def part2(data):
    binary_string = bin(int(data, 16))[2:].zfill(len(data)*4)

    i = 0
    while i < len(binary_string):

        if int(binary_string[i:]) == 0:
            break

        version, type_id, length, val = read_next_packet(binary_string[i:])

        i += length

        if type_id != 4:
            if val[0]=='N':
                packets, length = read_n_packets(binary_string[i:], val[1])
            else:
                packets, length  = read_n_bits(binary_string[i:], val[1])

            val = perform_operation(type_id, packets)
            i += length

    return val

def read_n_packets(binary_data, n):
    i = 0
    packets = []
    for p in range(n):
        version, type_id, length, val = read_next_packet(binary_data[i:])
        i += length

        if type_id != 4:
            if val[0]=='N':
                sub_packets, length = read_n_packets(binary_data[i:], val[1])
            else:
                sub_packets, length = read_n_bits(binary_data[i:], val[1])

            val = perform_operation(type_id, sub_packets)
            i += length

        packets.append(val)

    return packets, i

def read_n_bits(binary_data, n_bits):
    i = 0
    packets = []
    while i < n_bits:
        version, type_id, length, val = read_next_packet(binary_data[i:])
        i += length

        if type_id != 4:
            if val[0]=='N':
                sub_packets, length = read_n_packets(binary_data[i:], val[1])
            else:
                sub_packets, length = read_n_bits(binary_data[i:], val[1])

            val = perform_operation(type_id, sub_packets)
            i += length

        packets.append(val)

    return packets, i

def perform_operation(op, packets):
    packets = [int(x) for x in packets]
    if op == 0:
        return sum(packets)
    if op == 1:
        return np.prod(packets)
    if op == 2:
        return np.min(packets)
    if op == 3:
        return np.max(packets)
    if op == 5:
        return int(packets[0]>packets[1])
    if op == 6:
        return int(packets[0]<packets[1])
    if op == 7:
        return int(packets[0]==packets[1])

if __name__ == "__main__":
    day = 16
    data = get_input(day, splitlines=False)
    print(part1(data))
    print(part2(data))

