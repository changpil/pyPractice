def mergeSort(l):
    if len(l) == 1:
        return l
    mid = len(l)//2
    a = mergeSort(l[:mid])
    b = mergeSort(l[mid:])
    c = merge(a, b)
    return c



def merge(a, b):
    c = []
    i , j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(a[j])
        j += 1
    return c

l =[9,8,7,6,3]
z=mergeSort(l)
print(z)


def mergeSort_inplace(s, e, _list):
    if e-s == 1:
        return

    mid = (s+e)//2
    mergeSort_inplace(s, mid, _list)
    mergeSort_inplace(mid, e, _list)
    merge_inplace(s,mid, e, _list)

def merge_inplace(s, mid, e,_list):
    i = s
    j = mid

    while i < mid and j < e:
        if _list[i] > _list[j]:
            tmp = _list[j]
            del _list[j]
            _list.insert(i, tmp)
            j += 1
            i += 1
            mid += 1
        else:
            i += 1


l =[4,3,5,67,8,3,44,6]
mergeSort_inplace(0, len(l), l)
print(l)



