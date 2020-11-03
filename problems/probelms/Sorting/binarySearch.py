
#BinarySearch is only for sortedOrder O(logn)
def binarySearch(l, t):
    return _binarySearch(0, len(l)-1, l, t)


def _binarySearch(s, e, l, t):
    if s > e:
        return -1

    p = (s+e)//2
    if l[p] > t:
        return _binarySearch(s, p-1, l, t)
    elif l[p] < t:
        return _binarySearch(p+1, e, l, t)

    else:
        return p

def binarySearch_recursive(l, t):
    i = 0
    j = len(l) -1

    while i <= j:
        p = (i + j) // 2
        if l[p] == t:
            return p
        elif l[p] > t:
            j = p - 1
        elif l[p] < t:
            i = p + 1
    return -1

l=[1,3,6,8,12,35,67,78,89]

print(binarySearch_recursive(l,1))

