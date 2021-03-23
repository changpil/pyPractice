"""
An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:
-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

 -63, -34, -9, 12,
-10,   0, 28, 23,
-27, -11, -2, 10,
  9,  17, 25, 18

Output = 28
0 4 3
  1
8 6 6
"""
import math
def hourglassSum(grid):
    m = -math.inf
    for i in range(0, len(grid)-3+1):
        for j in range(0, len(grid[0])-3+1):
            local_m = 0
            for row in range(i, i+3):
                for col in range(j , j+3):
                    if col != j + 1  and row == i+1:
                        continue
                    else:
                        local_m += grid[row][col]
            m = max(m, local_m)
    return m

grid = [[-9,-9,-9,1,1,1],
        [0,-9,0,4,3,2],
        [9,-9,-9,1,2,3],
        [0,0,8,6,6,0],
        [0,0,0,-2,0,0],
        [0,0,1,2,4,0]]

print(hourglassSum(grid))

grid = [[1,1,1,0,0,0],
        [0,1,0,0,0,0],
        [1,1,1,0,0,0],
        [0,0,2,4,4,0],
        [0,0,0,2,0,0],
        [0,0,1,2,4,0]]

print(hourglassSum(grid))