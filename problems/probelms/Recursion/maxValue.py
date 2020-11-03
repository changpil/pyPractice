#O(nlogn)
def maxValue(_list, left, right):
    if left > right and left < 0 and right > len(_list):
        raise ValueError

    mid = (left + right)//2

    if mid == left:
        return _list[mid]

    return max(maxValue(_list, left, mid-1), maxValue(_list, mid , right))

def maxValue_better(_list, left, right):
    if left == right:
        return _list[left]


    return max(_list[left], maxValue(_list, left+1 , right))

_l=[3,3,34,4,34,34,556,23,34,56,1,34,3]
print(maxValue(_l, 4, 9))
