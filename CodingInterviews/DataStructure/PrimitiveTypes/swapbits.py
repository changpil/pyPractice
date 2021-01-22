"""
Date:Pattern1:knapsack/17/2018
"""
from PrimitiveTypes.paritybit import print2Bytes


def swapbits(bits, a, b):
    print2Bytes(bits)
    bit_list =[]
    #insert 1s and 0s in list in same order
    for i in range(16):
        bit = bits & 1
        bits = bits >> 1
        bit_list.insert(0,bit)

    print(bit_list)
    #swap the bits
    #no check for out of range
    # Error: numer is different
    tmp_i = bit_list[a]
    bit_list[a] = bit_list[b]
    bit_list[b] = tmp_i

    print(bit_list)
    # generate list to bytes
    rt_bits = 0
    for i in bit_list:
        rt_bits = rt_bits << 1
        rt_bits = rt_bits | i
    print2Bytes(rt_bits)
    return rt_bits

swapbits(23, 1, 6)

