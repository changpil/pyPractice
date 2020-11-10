"""
Multiply two integers without using multiplication, division and bitwise operators, and no loops
"""

def multiply(a, b):
    if a == 0 or b == 0:
        return 0

    if b > 0:
        a = a + multiply(a, b - 1)
    else:
        a = -multiply(a, -b)

    return a

#print(multiply(-3, -5))

def multiply1(a, b):
    if a == 0 or b == 0:
        return 0

    if b > 0:
        return a + multiply(a, b - 1)
    else:
        return -multiply(a, -b)

print(multiply(3, -5))