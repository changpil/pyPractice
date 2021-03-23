"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:

NumMatrix(int[][] matrix) initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) returns the sum of the elements of the matrix array inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2)
"""


class NumMatrix:

    def __init__(self, matrix):
        self.runningSum = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            runningSum = 0
            for j in range(len(matrix[0])):
                runningSum += matrix[i][j]
                if i == 0:
                    self.runningSum[i][j] = runningSum
                else:
                    self.runningSum[i][j] = self.runningSum[i-1][j] + runningSum

    def sumRegion(self, row1, col1, row2, col2):
        result = 0
        if col1 -1 >= 0 and row1 -1 >= 0:
            result = self.runningSum[row2][col2] - self.runningSum[row2][col1 -1] - self.runningSum[row1 -1][col2] + self.runningSum[row1-1][col1-1]
        elif  col1 -1 >= 0 and row1 - 1 < 0:
            result = self.runningSum[row2][col2] - self.runningSum[row2][col1 - 1]
        elif  col1 -1 < 0 and row1 - 1 >= 0:
            result = self.runningSum[row2][col2] - self.runningSum[row1 -1][col2]
        else:
            result = self.runningSum[row2][col2]
        return result

matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
numM = NumMatrix(matrix)
print(numM.sumRegion(2,1,4,3))
print(numM.sumRegion(1,1,2,2))
print(numM.sumRegion(1,2,2,4))



