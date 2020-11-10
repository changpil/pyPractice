"""

def power(a, b):
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
[1, 2, 4, 8, 0, 0, 0]
[1, 2, 4, 8, 8, 0, 64, 0]
64
"""
def power(a, b):
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

print(power(2,6))

