"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

"""

import collections
def floodFill(image, sr, sc, newColor):
    visited = set()
    bfs(image, visited, sr, sc, image[sr][sc], newColor)
    return image


import collections
def bfs(grid, visited, i, j, oc, nc):
    q = collections.deque()
    visited.add((i, j))
    q.append((i, j))
    while q:
        x, y = q.popleft()
        grid[x][y] = nc
        for nx, ny in getNeighbors(grid, x, y, oc):
            if (nx, ny) not in visited:
                grid[nx][ny] = nc
                visited.add((nx, ny))
                q.append((nx, ny))


def getNeighbors(grid, i, j, oc):
    neigbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    for nx, ny in neigbors:
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == oc:
            yield nx, ny

image = [[1,1,1],[1,1,0],[1,0,1]]
print(floodFill(image, 1, 1, 2))

