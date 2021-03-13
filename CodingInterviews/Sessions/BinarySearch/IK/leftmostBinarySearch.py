# [1, 2,2,2,3,5,8] k = 2
# [2,2,2,2 3,6,8,99] k =2

#Recursive Binary Search is not preferable
# def binary_search_leftmost(arr, target, s, e):
#     if s > e:
#         return -1
#     mid = (s+e) // 2
#     if target == arr[mid]:
#         re = binary_search_leftmost(arr, target, s, mid -1)
#         if re == -1:
#             return mid
#         else:
#             return re
#
#     if target > arr[mid]:
#         return binary_search_leftmost(arr, target, mid + 1, e)
#     if target < arr[mid]:
#         return binary_search_leftmost(arr, target, s, mid -1)
# k = 2
# arr = [1,2,2,2,3,5,8]
# print(binary_search_leftmost(arr, 2, 0, len(arr)-1))
#
# k = 2
# arr = [2,2,2, 2, 3,5,8]
# print(binary_search_leftmost(arr, 2, 0, len(arr)-1))
#
#
# k = 2
# arr = [2,2,2, 2, 2,2,2 ]
# print(binary_search_leftmost(arr, 2, 0, len(arr)-1))

def binary_search_leftmost(nums, target):
    start, end = 0, len(nums)-1
    while start <= end:
        mid = (start + end)//2
        if target <= nums[mid]:
            end = mid - 1
        else:
            start = mid + 1

    #if start == len(nums) or end == -1 or nums[start] != target:
    # end == -1 ===> -1 when arr = [2,2,2, 2,3,5,8]
    if start == len(nums) or nums[start] != target:
        return -1

    return start

k = 2
arr = [1,2,2,2,3,5,8]
print(binary_search_leftmost(arr, 2))

# When target is all the way to left
arr = [2,2,2, 2,3,5,8]
print(binary_search_leftmost(arr, 2))

arr = [3,5,8, 10]
print(binary_search_leftmost(arr, 2))

# When there is no target
arr = [-2, 0, 1,3,5,8]
print(binary_search_leftmost(arr, 2))

arr = [3,4,5,6,7 ]
print(binary_search_leftmost(arr, 2))


arr = [-6, -4, -3, -1, 0 ]
print(binary_search_leftmost(arr, 2))