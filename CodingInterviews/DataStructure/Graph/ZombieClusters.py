# def build_grid(input):
#     grid=[]
#     for line in input:
#         grid.append(list(line))
#     return grid
#
# def zombieCluster(zombies):
#     grid = build_grid(zombies)
#     num_cluster = 0
#     print(grid)
#
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == '0':
#                 if (0 <= i-1 < i+1 < len(grid) and grid[i-1][j] == '1' and grid[i+1][j] == '1') or (
#                         0 <= j - 1 < j + 1 < len(grid[0]) and grid[i][j - 1] == '1' and grid[i][j + 1] == '1'):
#                     zombify(grid, i, j)
#     print(grid)
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == '1':
#                 num_cluster += 1
#                 cluster(grid, i, j)
#
#     return num_cluster
#
# def zombify(grid, i, j):
#     grid[i][j] = '1'
#     if i+1 < len(grid) and grid[i+1][j] == '0':
#         if i+2 < len(grid) and grid[i+2][j] == '1':
#             zombify(grid, i+1, j )
#     if i-1 >= 0 and grid[i-1][j] == '0':
#         if i - 2 >= 0 and grid[i - 2][j] == '1':
#             zombify(grid, i - 1, j)
#     if j+1 < len(grid[0]) and grid[i][j+1] == '0':
#         if j +2 < len(grid[0]) and grid[i][j+2] == '1':
#             zombify(grid, i , j +1)
#     if j-1 >= 0 and grid[i][j-1] == '0':
#         if j -2 >= 0 and grid[i][j-2] == '1':
#             zombify(grid, i , j - 1)
#
#
# def cluster(grid, i, j):
#     grid[i][j] = '0'
#     if i+1 < len(grid) and grid[i+1][j] == '1':
#         cluster(grid, i+1, j )
#     if i-1 >= 0 and grid[i-1][j] == '1':
#         cluster(grid, i-1, j )
#     if j+1 < len(grid[0]) and grid[i][j+1] == '1':
#         cluster(grid, i, j + 1 )
#     if j-1 >= 0 and grid[i][j-1] == '1':
#         cluster(grid, i, j - 1 )
def getMoves(grid, i, j):
    moves = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    for x, y in moves:
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            continue
        if grid[x][y] == "0":
            continue
        yield x, y


from collections import deque


def zombieCluster(grid):
    visited = set()
    cc = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] == "1":
                bfs(grid, i, j, visited)
                cc += 1
    return cc


def bfs(grid, i, j, visited):
    queue = deque()
    queue.append((i, j))

    while queue:
        mi, mj = queue.popleft()
        for x, y in getMoves(grid, mi, mj):
            if (x, y) not in visited:
                visited.add((x, y))
                queue.append((x, y))

zombies = ["1100",
           "1110",
           "0110",
           "0001"]
print(zombieCluster(zombies))

zombies = ["1000",
           "0001",
           "1100",
           "0101"]
print(zombieCluster(zombies))