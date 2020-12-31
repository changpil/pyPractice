# Every non-negative integer N has a binary representation, for example, 8 can be represented as “1000” in binary and 7 as “0111” in binary.
#
# The complement of a binary representation is the number in binary that we get when we change every 1 to a 0 and every 0 to a 1.
# For example, the binary complement of “1010” is “0101”.
# For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.

def calculate_bitwise_complement(n):
    expected = 1
    bdig = 0
    tmp = n
    while tmp:
        tmp = tmp >> 1
        bdig = bdig << 1
        bdig += 1
    # for i in range(1 , n):
    #     if (i ^ n) == bdig:
    #         return i
    return n ^ bdig

def main():
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

main()