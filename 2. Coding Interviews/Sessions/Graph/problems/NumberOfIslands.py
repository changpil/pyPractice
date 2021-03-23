

def numOfIslands(grid):
    island = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                island += 1
                find_island(grid, i, j)
    return island
def find_island(grid, i, j):
    #if not (0<= i < len(grid)) or not (0 <= j < len(grid[0]) ):
    #    return

    grid[i][j] =0

    if i+1 < len(grid) and grid[i+1][j] == 1:
        find_island(grid, i+1, j)
    if i -1 >= 0 and grid[i-1][j] ==1:
        find_island(grid, i -1, j)
    if j +1 < len(grid[0]) and grid[i][j+1]:
        find_island(grid, i, j+1)
    if j-1 >=0 and grid[i][j-1] ==1:
        find_island(grid[i][j-1])


grid = [[1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0]]

print(numOfIslands(grid))

grid = [[0,1,1,1,0],
        [1,0,1,1,0],
        [1,1,0,0,1],
        [0,1,1,0,1]]

print(numOfIslands(grid))


