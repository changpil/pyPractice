import random

def quickSort(_list, l, r ):
    if l > r:
        return
    #m = partition_origin(_list, l, r)
    m = partition(_list,l, r)
    #print("l:{} r:{}  m:{} list:{!r}".format(l, r ,m,  _list))
    quickSort(_list, l, m - 1)
    quickSort(_list, m + 1, r)

# This does not find right index for pivot
def partition(a, l, r):
    i, j  = l, r-1
    #pivot, pivot_index = a[(r-l)//2], (r-l)//2
    #a[pivot_index], a[r] = a[r], a[pivot_index]
    pivot =a[r]
    while i <= j: # i <j is not working : In the case of [3,4]
        while i <= r-1 and a[i] < pivot :
            i += 1
        while j >= l and a[j] > pivot:
            j -= 1
        if i < j:
            a[i] , a[j] = a[j], a[i]
            i += 1
            j -= 1

    a[i], a[r] = a[r], a[i]
    return i


def partition_origin(arr, low, high):
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







a = [4, 2, 3, 1, 4]
print(a)
quickSort(a, 0, len(a)-1)
print(f"{a}")

a =[7, 6,5,4,3,2,1]
print(a)
quickSort(a, 0, len(a)-1)
print(f"{a}")

a =[4, 7, 6,5,4,3,2,1]
print(a)
quickSort(a, 0, len(a)-1)
print(a)

a =[-2, 1, -1]
print(a)
quickSort(a, 0, len(a)-1)
print(f"{a}")

a =[-1, 1]
print(a)
quickSort(a, 0, len(a)-1)
print(f"{a}")