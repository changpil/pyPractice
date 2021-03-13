# binary search is ordered list
# Recursion of Binary Search is not preferable (call stack)
# def binary_search(base, target,  start, end):
#     if start > end:
#         return -1
#     mid = (start + end)//2
#
#     if target == base[mid]:
#         return mid
#     elif base[mid] < target:
#         return binary_search(base, target,  mid+1, end)
#     else:
#         return binary_search(base, target,  start, mid-1)
#
#
# a=[-6, -3, -1, 0, 1,3,5,8,9,10,14,18,23,45]
# targets = [3, -1, -7,  -6,  4, 18, 99]
# print(a)
# for t in targets:
#     print(f"Target: {t} : {binary_search(a, t, 0, len(a) -1)}")
#
# a=[0,1]
# targets = [-1, 0, 1, 2]
# print(a)
# for t in targets:
#     print(f"Target: {t} : {binary_search(a, t, 0, len(a) -1)}")

## This is preferable due to call stack of O(logN)
def binarySearch(nums, target):
    start = 0;
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return -1

a=[-6, -3, -1, 0, 1,3,5,8,9,10,14,18,23,45]
targets = [3, -1, -7,  -6,  4, 18, 99]
print(a)
for t in targets:
    print(f"Target: {t} : {binarySearch(a, t)}")

a=[0,1]
targets = [-1, 0, 1, 2]
print(a)
for t in targets:
    print(f"Target: {t} : {binarySearch(a, t )}")