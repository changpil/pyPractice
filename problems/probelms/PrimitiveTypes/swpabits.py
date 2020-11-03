#How to swap two bits in a given integer?

"""
Input: n = 28, p1 = 0, p2 = 3
Output: 21
28 in binary is 11100.  If we swap 0'th and 3rd digits,
we get 10101 which is 21 in decimal.

Input: n = 20, p1 = 2, p2 = 3
Output: 24
"""

def swapbits(n, p1, p2):
    print("{} p1={} p2={}".format(bin(n)[2:], p1, p2))
    if n.bit_length() <= p1 or n.bit_length() <= p2:
        raise ValueError
    bit1 = (n >> p1) & 1
    bit2 = (n >> p2) & 1

    x = bit1 ^ bit2

    x = (x << p1) | (x << p2)
    print("mask x  {}".format(bin(x)[2:]))
    result = x^n
    print(bin(result)[2:])
    print(result)

#swapbits(28, 0, 3)



def makefullbits(n):
    print(bin(n)[2:])
    i = 1
    for _ in range(n.bit_length()-1):
        i = (i << 1) | 1
    print(bin(i)[2:])

    print("XOR {}".format(bin(n^i)[2:]))
makefullbits(10)