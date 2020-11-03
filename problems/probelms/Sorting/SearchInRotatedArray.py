"""
Sorted array was rotated an unknown number of times.
[55, 56, 57,89, 102, 3, 4,7,12, 33,45]
"""

def binarySearch(l, t):
    return _binarySearch(0, len(l)-1, l, t)

def _binarySearch(left, right, l, t):
    if left > right:
        return -1

    p = (left+right)//2
    if t < l[p]:
        while l[left] > l[p]:
            left += 1
        res = _binarySearch(left, p-1, l, t)
        if res != -1:
            return res
        while p < right and l[p] > l[right]:
            p += 1
        return _binarySearch(p, right, l, t)

    elif t > l[p]:
        while l[right] < l[p]:
            right -= 1
        res = _binarySearch(p +1, right, l, t)
        if res != -1:
            return res
        while left <= p and l[p] < l[left]:
            p -= 1
        return _binarySearch(left, p , l, t )
    else:
        return p

l = [55, 56, 57,89, 102, 3, 4,7,12, 33,45]
l=[1,2,3,34]
print(binarySearch(l, 0))
