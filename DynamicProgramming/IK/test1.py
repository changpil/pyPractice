# Cut The Rope﻿﻿﻿﻿
# Given a rope, cut it into parts maximizing the product of their lengths.
#
# Example
# Input: 4
# Output: 4
#
# Length of the rope is 4.
# All ways it can be cut into parts: 1+3, 1+1+2, 1+1+1+1, 2+2, 2+1+1.
# Among these, 2+2 cut makes for the greatest product: 2*2=4.


def max_product_from_cut_pieces(n):
    table = [1]*(n+1)
    table[0] = 1
    if n == 2 :
        return 1
    if n == 3:
        return 2

    for n in range(2, n + 1):
        maxR = 0
        for k in range(1, n + 1):
            maxR = max(maxR, table[n-k]*k)
        table[n] = maxR
    return table[n]
#Answer: 1
print(max_product_from_cut_pieces(1))
#Answer: 2
print(max_product_from_cut_pieces(3))
# Answer: 81
print(max_product_from_cut_pieces(12))