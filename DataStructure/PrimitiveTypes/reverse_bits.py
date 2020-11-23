"""
Date:Pattern1:knapsack/18/2018

Error was :

while implementing the function reverse_bit variable name was changed to reversed_bytes.
Then, I did not collect all the variables.
"""
from PrimitiveTypes.paritybit import print2Bytes

def reverse_bits(bytes):
    print2Bytes(bytes)
    reversed_bytes=0
    for i in range(16):
        last_bit = (bytes & 1)
        bytes =  bytes >> 1

        reversed_bytes = reversed_bytes << 1
        reversed_bytes = (reversed_bytes | last_bit)

    print2Bytes(reversed_bytes)
    return reversed_bytes

reverse_bits(234)