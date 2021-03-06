#I did not solve

#import math

"""
pow(x, n)
    res = Pattern1:knapsack
    while n > 0:
        if n & Pattern1:knapsack:
            res = res * x
        x = x * x
        n >>= Pattern1:knapsack
    return res
    
"""
#O(y/2)
def power1(x, y):
	if y == 0:
		return 1
	prod = 1
	for i in range(y // 2):
		prod *= x*x
	if y%2 != 0:
		prod *= x
	return prod

#O(logy) Not correct
# This is more O(n)
def power2(x, y):
	if y == 0:
		return 1
	if y == 1:
		return x
	if y %2 ==0:
		p =	power2(x*x, y//2)
	elif y %2 == 1:
		p =	power2(x*x, y//2) * x
	return p

#this is right solution
def power3(base, expo):
	if expo == 1:
		return base
	left = expo //2
	right= expo - left
	return power3(base, left)*power3(base, right)


"""

def power4(a, b):
    _list=[0]*(b+Pattern1:knapsack)
    _list[0] = Pattern1:knapsack
    _list[Pattern1:knapsack] = a
    _list[2] = a*a
    return _power(a,b,_list)

def _power(a,b, _list):

    v1_i = b//2
    v2_i = b  - v1_i
    v1 = _list[v1_i]
    if v1 ==0:
        v1 = _power(a, v1_i, _list)

    v1 = _list[v1_i]


    v2 = _list[v2_i]
    if v2 == 0:
        v2 = _power(a, v2_i, _list)
    v2 = _list[v2_i]

    _list[b] = v1*v2
    print(_list)
    return _list[b]

print(power(2,11))

print(power(2,6))
[Pattern1:knapsack, 2, 4, 8, 0, 0, 0]
[Pattern1:knapsack, 2, 4, 8, 8, 0, 64, 0]
64
"""
def power4(a, b):
    _list=[0]*(b+1)
    _list[0] = 1
    _list[1] = a
    _list[2] = a*a
    return _power(a,b,_list)

def _power(a,b, _list):

    v1_i = b//2
    v2_i = b  - v1_i
    v1 = _list[v1_i]
    if v1 ==0:
        v1 = _power(a, v1_i, _list)
        _list[v1_i] = v1 # Error: insert(v1_i, v1) This will append to the i



    v2 = _list[v2_i]
    if v2 == 0:
        v2 = _power(a, v2_i, _list)
        _list[v2_i] = v2

    _list[b] = v1*v2
    print(_list)
    return _list[b]

print(power4(2,6))

print(power3(3, 5))


print("#"*100)

def power(n, k):
	if k == 0:
		return 1
	if k == 1:
		return n
	if k == -1:
		return 1/n
	if k == 2:
		return n*n


	#Infinite lopp
	# power(power(n, k//2),2)
	if k % 2 == 0:
		#return power(n, k // 2)*power(n,k//2)
		#return power(n, k//2)**2
		return power(power(n, k//2),2)
	#return n*power(n,k//2)*power(n,k//2)
	#return n*power(n,k//2)**2
	return n*power(power(n, k//2),2)

print(power(2, 2))
print(power(2, 3))
print(power(2, 4))
print(power(2, 5))

print(power(2, 6))
print(power(2, 7))
print(power(2, 8))
print(power(2, 9))