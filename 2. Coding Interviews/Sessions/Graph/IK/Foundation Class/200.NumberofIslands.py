"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

import collections
def numIslands(grid):
    visited = set()
    island = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] == '1':
                bfs(grid, visited, i, j)
                island += 1

    return island

def bfs(grid, visited, i, j):
    q = collections.deque()
    visited.add((i,j))
    q.append((i,j))

    while q:
        x, y = q.popleft()
        for nx, ny in getNeighbors(grid, x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))

def getNeighbors(grid, i, j):
    neigbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    for nx, ny in neigbors:
        if 0<= nx < len(grid) and 0<= ny< len(grid[0]) and grid[nx][ny] == '1':
            yield nx, ny

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))