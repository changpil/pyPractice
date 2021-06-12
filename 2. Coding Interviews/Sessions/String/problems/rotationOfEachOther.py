"""
Check the two stings are rotation of each other
"""

## No extra space
## Time O(NM)
def isRotaionOfEachOther(a, b):
    if len(a) != len(b):
        return False
    p = -1
    i = 0
    while i < len(a):
        if a[i] == b[0]:
            j = 0
            ii = i
            while ii < len(a) and j < len(b) and a[ii] == b[j]:
                    ii += 1
                    j += 1
            if ii == len(a):
                p = i
                break
        i += 1
    if p == -1:
        return False
    for j in range(p ):
        if a[j] != b[p+j]:
            return False
    return True

import collections
def isRotaionOfEachOther(a, b):
    if len(a) != len(b):
        return False
    if a == b:
        return True
    d = collections.defaultdict(set())
    for i, c in enumerate(a):
        d[c].add(i)
    for i, c in enumerate(b):
        pass



a, b = "abcd", "cdab"
print(isRotaionOfEachOther(a,b))

a, b = "abcd", "cabd"
print(isRotaionOfEachOther(a,b))

a, b = "    ", "    "
print(isRotaionOfEachOther(a,b))