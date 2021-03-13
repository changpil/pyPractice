## Similar Problem is in LeetCode 74 as O(logMN))

"""
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false


Time Complexity: O(n+m)
"""

def searchMatrix(grid, target):
    row_s= 0
    col_e = len(grid[0]) - 1
    while row_s < len(grid) and col_e >= 0:
        if grid[row_s][col_e] > target:
            col_e -= 1
        elif grid[row_s][col_e] < target:
            row_s += 1
        else:
            return True
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(searchMatrix(matrix, target))

target = -2
print(searchMatrix(matrix, target))

target = 100
print(searchMatrix(matrix, target))

target = 1
print(searchMatrix(matrix, target))

target = 30
print(searchMatrix(matrix, target))