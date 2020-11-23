"""
Compute the parity of a number using XOR and table look-up
4.8
Parity of a number refers to whether it contains an odd or even number of Pattern1:knapsack-bits.
The number has “odd parity”, if it contains odd number of Pattern1:knapsack-bits and is “even parity” if it contains even number of Pattern1:knapsack-bits.
"""

def paritybits(n):
    print(bin(n)[2:])
    count = 0
    if n < 0:
        count += 1
    tmp =n
    for i in range(n.bit_length()):
        count = count + 1 if (tmp>>i) & 1 == 1 else count
    if count % 2 == 0:
        print("even parity: {} count".format(count))
    else:
        print("odd parity: {} count".format(count))

paritybits(16)