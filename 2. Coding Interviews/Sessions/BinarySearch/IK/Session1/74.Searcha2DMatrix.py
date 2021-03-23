# Similar problem from Leetcode problem: 240

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""


# Time Complexity : O(logN*logM)
# def searchMatrix(matrix, target):
#     sr, er = 0, len(matrix) - 1
#     sc, ec = 0, len(matrix[0]) - 1
#     while sr <= er:
#         mr = (sr + er) // 2
#         if matrix[mr][sc] <= target <= matrix[mr][ec]:
#             return bsearch(matrix[mr], target, sc, ec)
#         elif mr - 1 >= 0 and matrix[mr - 1][ec] >= target:
#             er = mr - 1
#         else:
#             sr = mr + 1
#     return False
#
#
# def bsearch(nums, target, s, e):
#     while s <= e:
#         mid = (s + e) // 2
#         if target == nums[mid]:
#             return True
#         elif nums[mid] > target:
#             e = mid - 1
#         else:
#             s = mid + 1
#     return False

# matrix = [[2,4,7,9],[11, 15, 24,56]]
# target = 10
# print(searchMatrix(matrix, target))
# target = 9
# print(searchMatrix(matrix, target))
# matrix = [[2,4,7,9, 11, 15, 24,56]]
# target = 24
# print(searchMatrix(matrix, target))

#Time Complexity : O(logN+logM)
def search(martix , target):
    start, end = 0, len(matrix)*len(matrix[0]) - 1
    while start <= end:
        mid = (start + end)//2
        row = mid//len(matrix[0])
        col = mid%len(matrix[0])

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False
matrix = [[2,4,7,9],[11, 15, 24,56]]
target = 10
print(search(matrix, target))
target = 9
print(search(matrix, target))
matrix = [[2,4,7,9, 11, 15, 24,56]]
target = 24
print(search(matrix, target))