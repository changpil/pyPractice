# 4/26/2021 8:23 - 8:38

def mergeSort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    a1 = mergeSort(a[:mid])
    a2 = mergeSort(a[mid:])
    a3 = merge(a1,a2)
    return a3


def merge(a1, a2):
    a = []
    i, j = 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a.append(a1[i])
            i += 1
        else:
            a.append(a2[j])
            j += 1
    while i < len(a1):
        a.append(a1[i])
        i += 1
    while j < len(a2):
        a.append(a2[j])
        j += 1
    return a



a = [5,3,7,9,2,1]
print(mergeSort(a))

a = [-1, 0, 5,3,0, 3 ,9,2,1]
print(mergeSort(a))

a = []
print(mergeSort(a))

a = [-1]
print(mergeSort(a))

a = [-1, -1]
print(mergeSort(a))


