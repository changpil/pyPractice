# [1, 2,2,2,3,5,8] k = 2
# [2,2,2,2 3,6,8,99] k =2


def binary_search_leftmost(arr, target, s, e):
    if s > e:
        return -1
    mid = (s+e) // 2
    if target == arr[mid]:
        re = binary_search_leftmost(arr, target, s, mid -1)
        if re == -1:
            return mid
        else:
            return re

    if target > arr[mid]:
        return binary_search_leftmost(arr, target, mid + 1, e)
    if target < arr[mid]:
        return binary_search_leftmost(arr, target, s, mid -1)

k = 2
arr = [1,2,2,2,3,5,8]
print(binary_search_leftmost(arr, 2, 0, len(arr)-1))

k = 2
arr = [2,2,2, 2, 3,5,8]
print(binary_search_leftmost(arr, 2, 0, len(arr)-1))


k = 2
arr = [2,2,2, 2, 2,2,2 ]
print(binary_search_leftmost(arr, 2, 0, len(arr)-1))