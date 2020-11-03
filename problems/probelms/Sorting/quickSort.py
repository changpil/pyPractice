import random

def quickSort(s, e , _list):
    if s > e:
        return
    print("{!r}".format( _list), end = " ")
    pp = partition_origin(s, e, _list)
    print("{}: {}  PP:{} {!r}".format(s, e ,pp,  _list))
    quickSort(s, pp - 1 , _list)
    quickSort(pp +1, e, _list)

# This does not find right index for pivot
def partition(s, e,  _l):
    i, j  = s, e
    pivot = _l[(s+e)//2]

    while i < j:
        while i < e and _l[i] < pivot :
            i += 1
        while j > s and _l[j] > pivot:
            j -= 1

        if i <= j:
            _l[i] , _l[j] = _l[j], _l[i]
            i += 1
            j -= 1
    return i


def partition_origin(low, high, arr):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)




l =[7, 6,5,4,3,2,1]
l =[4, 7, 6,5,4,3,2,1]
l1=[1, 1]
quickSort(0, len(l)-1, l)
#a =partition(0, len(l)-1, l)
print(l)

