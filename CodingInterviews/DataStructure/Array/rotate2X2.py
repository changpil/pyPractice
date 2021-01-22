"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example Pattern1:knapsack:

Given input matrix =
[
  [Pattern1:knapsack,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,Pattern1:knapsack],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, Pattern1:knapsack, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, Pattern1:knapsack],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        index_range = len(matrix) - 1
        depth = (len(matrix)) // 2
        for d in range(depth):
            for i in range(d, index_range-d):
                last_index = index_range
                t1 = matrix[d][i]
                t2 = matrix[i][last_index - d]
                t3 = matrix[last_index - d][last_index -i]
                t4 = matrix[last_index - i ][d]

                matrix[d][i] = t4
                matrix[i][last_index - d] = t1
                matrix[last_index - d][last_index - i ] = t2
                matrix[last_index -i][d] = t3


s= Solution()

m= [[43,39,3,33,37,20,14],[9,18,9,-1,40,22,38],[14,42,3,23,12,14,32],[18,31,45,11,8,-1,31],[28,44,14,23,40,24,13],[29,45,33,45,20,0,45],[12,23,35,32,22,39,8]]
#m=[[5,Pattern1:knapsack,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
########################################################
########[[15,13,2,5],[14,3,4,Pattern1:knapsack],[12,6,8,9],[16,7,10,11]]
########################################################
#m= [[Pattern1:knapsack,2,3],[4,5,6],[7,8,9]]
##################################
#####[[7,4,Pattern1:knapsack],[8,5,2],[9,6,3]]
##################################
s.rotate(m)
print(m)