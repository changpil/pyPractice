# binary search is ordered list

def binary_search(base, target,  left, right):
    mid = (left+right)//2
    if target == base[mid]:
        return mid

    if left >= right:
        return -1

    if  base[mid] < target:
        return binary_search(base, target,  mid+1, right)
    else:
        return binary_search(base, target,  left, mid-1)

a=[1,3,5,8,9,10,14,18,23,45]
a=[0,1]
print(binary_search(a,1,0,len(a)-1))