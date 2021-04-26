"""
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates.
You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.
Example
Perform the following steps:
i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
It took  swaps to sort the array.
Function Description
Complete the function minimumSwaps in the editor below.
minimumSwaps has the following parameter(s):
int arr[n]: an unordered array of integers
Returns
int: the minimum number of swaps to sort the array

Sample Input 0

4
4 3 1 2
Sample Output 0

3

Explanation 0

Given array
After swapping  we get
After swapping  we get
After swapping  we get
So, we need a minimum of  swaps to sort the array in ascending order.

Sample Input 1
5
2 3 4 1 5
Sample Output 1
3
Explanation 1

Given array
After swapping  we get
After swapping  we get
After swapping  we get
So, we need a minimum of  swaps to sort the array in ascending order.

Sample Input 2
7
1 3 5 2 4 6 7
Sample Output 2

3
Explanation 2
Given array
After swapping  we get
After swapping  we get
After swapping  we get
So, we need a minimum of  swaps to sort the array in ascending order.
"""

# Timeout
# import math
# def minimumSwaps(arr):
#     steps = [math.inf]
#     _minimumSwaps(arr, 0, 0, steps)
#     return min(steps)
#
# def  _minimumSwaps(arr, index, step, steps):
#     if step == len(arr):
#         return
#     if step >= steps[0]:
#         return
#     arranged = True
#     for i in range(len(arr)):
#         if arr[i] != i + 1:
#             arranged = False
#     if arranged:
#         steps.pop()
#         steps.append(step)
#         return
#     for i in range(index, len(arr)):
#         if arr[i] != i + 1:
#             for swapindex in range(i+1, len(arr)):
#                 arr[i], arr[swapindex] = arr[swapindex], arr[i]
#                 _minimumSwaps(arr, i + 1, step +1, steps)
#                 arr[i], arr[swapindex] = arr[swapindex], arr[i]

# Solution
def minimumSwaps(arr):
    valueIndexMap = {}
    for pos, val in enumerate(arr):
        valueIndexMap[val] = pos
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            targetIndex = valueIndexMap[i+1]
            arr[i], arr[targetIndex] = arr[targetIndex], arr[i]
            valueIndexMap[arr[targetIndex]] = targetIndex
            swaps += 1
    return swaps

arr = [4, 3, 1, 2]
print(minimumSwaps(arr)) # 3

arr = [2, 3, 4, 1, 5]
print(minimumSwaps(arr)) # 3


arr = [3, 7, 6, 9, 1, 8, 10, 4, 2, 5]
print(minimumSwaps(arr)) # 9

# Timeout
arr = [2, 31, 1, 38, 29, 5, 44, 6, 12, 18, 39, 9, 48, 49, 13, 11, 7, 27, 14, 33, 50, 21, 46, 23, 15, 26, 8, 47, 40,
       3, 32, 22, 34, 42, 16, 41, 24, 10, 4, 28, 36, 30, 37, 35, 20, 17, 45, 43, 25, 19]
print(minimumSwaps(arr)) # 46