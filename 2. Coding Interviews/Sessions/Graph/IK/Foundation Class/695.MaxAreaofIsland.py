"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""

import math
def maxAreaOfIsland(grid):
    visited = set()
    prev_island = 0
    max_island = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] == 1:
                bfs(grid, visited, i, j)
                max_island = max(max_island, len(visited) - prev_island)
                prev_island = len(visited)

    return max_island

import collections
def bfs(grid, visited, i, j):
    q = collections.deque()
    visited.add((i, j))
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for nx, ny in getNeighbors(grid, x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))


def getNeighbors(grid, i, j):
    neigbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    for nx, ny in neigbors:
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
            yield nx, ny
#
# grid = [[0,0,0,0,0,0,0,0]]
# print(maxAreaOfIsland(grid))

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(grid))
