"""
//Given a method that takes in a positive non-zero number N, return from that method the total number of factors of N.
//Start with O(n) solution and make it faster if we have time
"""

def factor(n):
    factors = []
    for i in range(1, n+1):
        if n%i == 0:
            factors.append(i)

    return factors

print(factor(5))