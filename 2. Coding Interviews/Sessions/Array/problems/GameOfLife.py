# Game of Life

def tran(grid):
    visited = set()
    copygrid = [l[:] for l in grid]

    move(grid, copygrid, 0, 0, visited)
    return copygrid


def move(grid, cpgrid, i, j, visited):
    # if (i, j) in visited:
    #     return

    numOfLiveNeb = getNumOfLiveNeb(grid, i, j)

    if grid[i][j]:
        if numOfLiveNeb < 2:
            cpgrid[i][j] = False
        elif numOfLiveNeb > 3:
            cpgrid[i][j] = False
    else:
        if numOfLiveNeb == 3:
            cpgrid[i][j] = True

    visited.add((i, j))

    for ii, jj in getNebs(grid, i, j):
        if (ii, jj) not in visited:
            move(grid, cpgrid, ii, jj, visited)


def getNumOfLiveNeb(grid, i, j):
    nebs = [(i - 1, j), (i, j - 1), (i - 1, j - 1), (i + 1, j), (i, j + 1), (i + 1, j + 1), (i - 1, j + 1),
            (i + 1, j - 1)]

    liveN = 0
    for ii, jj in nebs:
        if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]):
            if grid[ii][jj]:
                liveN += 1
    return liveN


def getNebs(grid, i, j):
    nebs = [(i - 1, j), (i, j - 1), (i - 1, j - 1), (i + 1, j), (i, j + 1), (i + 1, j + 1), (i - 1, j + 1),
            (i + 1, j - 1)]
    for ii, jj in nebs:
        if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]):
            yield (ii, jj)


print("#" * 30)
n, m = 3, 3
grid = [[False] * m for i in range(n)]
grid[1][1] = True

for l in grid:
    print(l)
ns = tran(grid)
print()
for l in ns:
    print(l)

print("#" * 30)
n, m = 3, 3
grid = [[False] * m for i in range(n)]
grid[1][0] = True
grid[0][1] = True
grid[2][0] = True

for l in grid:
    print(l)
ns = tran(grid)
print()
for l in ns:
    print(l)

print("#" * 30)
n, m = 4, 5
grid = [[False] * m for i in range(n)]
grid[0][0] = True
grid[2][1] = True
grid[2][4] = True
grid[1][4] = True
grid[2][2] = True
grid[0][4] = True
grid[3][3] = True
grid[3][2] = True

for l in grid:
    print(l)
ns = tran(grid)
print()
for l in ns:
    print(l)