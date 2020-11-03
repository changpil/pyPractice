def add(x,y):
    return x+y

l = [i for i in range(10)]

import functools
print(functools.reduce(add, [1,2,3], 0))
print(functools.reduce(add, [1]))
print(functools.reduce(add, [], 0))
print(functools.reduce(add, l, 0))