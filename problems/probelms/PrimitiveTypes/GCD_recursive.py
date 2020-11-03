def gcd(x, y):
    t1 = max(x,y)
    t2 = min(x,y)
    x =t1
    y =t2
    while y != 0:
        (x, y) = (y, x % y)
    return x

def get_gcd(x, y, factor= None):
    if factor == None:
        factor =[1]
    if x ==0 or y ==0:
        return factor

    _max = max(x,y)
    _min = min(x,y)
    for i in range(2, _min+1):
        if  _max%i ==0 and _min%i ==0:
            factor.append(i)
            return get_gcd(_max//i, _min//i, factor)

    return factor

import math
def isPrime(num):
    if num < 3:
        return True

    for i in range(2, int(math.sqrt(num)+1)):
        if num%i ==0:
            return False
    return True


def get_lcm(x, y, factor= None):
    if factor == None:
        factor =[1]
    if x ==0 or y ==0:
        return factor

    _max = max(x,y)
    _min = min(x,y)
    for i in range(2, _min+1):
        if  _max%i ==0 and _min%i ==0:
            factor.append(i)
            _max //= i
            _min //= i
            if isPrime(_max) or isPrime(_min):
                break
            else:
                return get_gcd(_max, _min, factor)

    factor.append(_max)
    factor.append(_min)
    return factor



x, y = 14, 80
print(gcd(x, y))
print(get_gcd(x, y))
print(get_lcm(x, y))