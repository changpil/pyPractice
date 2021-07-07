"""

8  9 10 11
7  6  5  4
0  1  2  3
"""

def boardGrid(n, m):
    grid = [[None]*m for _ in range(n)]
    count = 0
    forward = True
    for i in range(len(grid)-1, -1, -1):
        if forward:
            for j in range(len(grid[0])):
                grid[i][j] = count
                count += 1
        else:
            for j in range(len(grid[0])-1, -1, -1):
                grid[i][j] = count
                count += 1
        forward = not forward
    return grid

# for l in boardGrid(3, 3):
#     print(l)
#
# for l in boardGrid(4, 2):
#     print(l)
#
#
# for l in boardGrid(10, 10):
#     print(l)

"""
Provided number , find the matching i, j
"""

def getIndex(n,m, num):
    for line in boardGrid(n, m):
        print(line)

    row = (n-1) - num//m
    if row%2 == 0:
        col = num%m
    else:
        col = (m-1) - num%m
    return (row, col)


print(getIndex(12, 4,43))