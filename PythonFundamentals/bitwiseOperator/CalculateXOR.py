#Calculate XOR from knapsack to n.


def xor(n):
    re= 1
    for i in range(2, n+1):
        re = re ^ i
        print(i, re)
    return re

#xor(24)

#XOR counts of 0s and 1s in binary representation

def xxx(a,b):
    print(bin(a), " " , bin(b))
    rb= a ^b
    l = rb.bit_length()
    n_0=0
    n_1=0
    for _ in range(l):
        b = rb & 1
        if b:
            n_1 +=1
        else:
            n_0 +=1
        rb = rb >>1
    return n_0, n_1

print(xxx(3, 5))