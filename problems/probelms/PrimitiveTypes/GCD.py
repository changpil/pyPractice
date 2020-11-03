import math
def get_divisors(num):
    rv =[]
    for i in range(1,int(math.sqrt(num)+1)):
        if num%i == 0:
            if rv.count(i) ==0:
                rv.append(i)
            if rv.count(num//i) ==0:  #in case of 4*4
                rv.append(num//i)
    return rv

def isDivisible(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num%i == 0 :
            return True
    return False

#(logn)
def isPrime(num):
    if num < 1:
        return False

    for i in range(2, int(math.sqrt(num)+1)):
        if num %i == 0:
            return False
    return True

#O((logn)^n)
def get_factors(num, _list = None):
    if _list == None:
        _list = []

    if isPrime(num):
        _list.append(num)
        return _list   # missed _list for _get_factor(11)

    for i in range(2, num+1):
        if num%i == 0:
            get_factors(i, _list)
            get_factors(num//i, _list)
            break
    return _list

#O((logn)^n)
# Intersection
def get_GCD(num1, num2):
    factors1 = get_factors(num1)
    factors2 = get_factors(num2)
    factors1.sort()
    factors2.sort()
    _list = []
    print(factors1)
    print(factors2)
    j_position =0
    for i, c1  in enumerate(factors1):
        for j in range(j_position, len(factors2)):
            if c1 == factors2[j]:
                _list.append(c1)
                j_position += 1
                break
            elif c1 < factors2[j]:
                break
            else:
                j_position += 1

    return _list

# Union
def get_LCM(num1, num2):
    factors1 = get_factors(num1)
    factors2 = get_factors(num2)
    factors1.sort()
    factors2.sort()
    _list = []
    print(factors1)
    print(factors2)
    i_position = 0
    j_position = 0

    for i in range(i_position, len(factors1)):
        for j in range(j_position, len(factors2)):
            c1, c2 = factors1[i], factors2[j]
            if c1== c2:
                _list.append(c1)
                j_position +=1
                i_position +=1
                break
            elif c1 < c2 :
                _list.append(c1)
                i_position += 1
                break
            else:
                _list.append(c2)
                j_position +=1
    while i_position < len(factors1):
        _list.append(factors1[i_position])
        i_position += 1      # Error : forgot thois line
    while j_position < len(factors2):
        _list.append(factors2[j_position])
        j_position += i      # Error: forgot this line
    return _list

#print(get_GCD(18, 48))
#print(get_LCM(18, 48))