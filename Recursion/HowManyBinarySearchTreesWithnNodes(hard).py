# def how_many_BSTs(n):
#     arr = [i for i in range(n)]
#     n = helper(arr)
#     return n
#
# def helper(arr):
#     if len(arr) == 1:
#         return 1
#     total= 0
#     for i in range(len(arr)):
#         left, right = 0, 0
#         if not (0 < i < len(arr)):
#             left = helper(arr[:i])
#             right = helper(arr[i + 1:])
#         else:
#             if len(arr[:i]) == len(arr[i + 1:]):
#                 left = helper(arr[:i])
#             #elif len(arr[:i]) < len(arr[i + 1:]):
#             #    right = helper(arr[i + 1:])
#             else:
#                 left = max(helper(arr[:i]), helper(arr[i + 1:]))
#         total += left + right
#     return total

def how_many_BSTs(n):
    arr = [i for i in range(n)]
    return helper(arr, 0, len(arr) - 1)

def helper(arr, i, j):
    if i >= j:
        return 0
    total = 0
    for mid in range(i , j +1):
        l = helper (arr,i, mid -1 )
        r = helper(arr, mid +1, j)
        total += l + r + 1
    return total


# print(how_many_BSTs(1))
# print(how_many_BSTs(2))
print(how_many_BSTs(3))
# print(how_many_BSTs(4))
# print(how_many_BSTs(5))