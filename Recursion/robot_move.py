"""
Robot sit on upper-lest corner in NXN grid.
The robot can move in two direction : right and down.
How many possible paths are there for the robot
"""
import pprint

def move(grid, row, col,):
    max_col = len(grid[0])-1
    max_row = len(grid) -1

    if row == max_row  and col == max_col:
        return 1
    elif row == max_row and col != max_col :
        #grid[row][col] = grid[row][col+Pattern1:knapsack]
        return move(grid, row , col+1)
    elif row != max_row and col == max_col:
        #grid[row][col] = grid[row+Pattern1:knapsack][col]
        return move(grid, row+1, col)
    else:
        #grid[row][col] = grid[row+Pattern1:knapsack][col] +grid[row][col+Pattern1:knapsack]
        return move(grid, row+1, col) + move(grid, row, col+1)

def move_wrong(grid, i, j):
    if i == len(grid) -1 or j ==len(grid[0]) -1:
        return 0
    if i < len(grid):
        down = 1 + move_wrong(grid, i+1, j)
    if j < len(grid[0]):
        right = 1+ move_wrong(grid, i, j+1)
    return down+right

#grid=[[0]]
#grid = [[0,0],[0,0]]
grid=[[0,-1,0],[-1,-1,-1],[0,0,0]]
#grid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#grid=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
pprint.pprint(grid)

print(move(grid, 0, 0))
pprint.pprint(grid)

print("#"*30)

#print(move_wrong(grid, 0, 0))

"""
Design a algorith to find a path for the robot from the top left to bottom right.
There are "off limit" that a robot cannot pass through 
"""

def findpath(i, j, grid, path):
    if i == len(grid) -1 and j == len(grid[0]) -1:
        return path
    if j+1 < len(grid[0]) and grid[i][j+1] != -1:
        path.append("R")
        return findpath(i, j+1, grid, path)
    elif i + 1 < len(grid) and grid[i+1][j] != -1:
        path.append("D")
        return findpath(i + 1, j, grid, path)
    else:
        return False
print(findpath(0,0,grid,list()))

