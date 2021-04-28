# 4/26/2021
def quickSort(a):
    if len (a) <= 1:
        return
    _quickSort(a, 0, len(a)-1)

def _quickSort(a, start, end):
    if start >= end:
        return
    pivot_index = partition(a, start, end)
    _quickSort(a, start, pivot_index - 1)
    _quickSort(a, pivot_index + 1, end)
    
def partition(a, start, end):
    pivot = a[start]
    i = start
    j = start + 1
    while j <= end:
        if a[j] >= pivot:
            j += 1
        else:
            i += 1
            a[j], a[i] = a[i], a[j]
            j+= 1
    a[i], a[start] = a[start], a[i]
    return i


a = [5,3,7,9,2,1]
quickSort(a)
print(a)

a = [-1, 0, 5,3,0, 3 ,9,2,1]
quickSort(a)
print(a)

a = []
quickSort(a)
print(a)

a = [-1]
quickSort(a)
print(a)

a = [-1, -1]
quickSort(a)
print(a)

            
    

