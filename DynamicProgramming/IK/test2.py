# Number Of Paths In A Matrix

# Consider a maze mapped to a matrix with an upper left corner at coordinates (row, column) = (0, 0).
# You can only move either towards right or down from a cell.
# You must determine the number of distinct paths through the maze.
# You will always start at a position (0, 0), the top left, and end up at (n-1, m-1), the bottom right.
# As an example, consider the following diagram where '1' indicates an open cell and '0' indicates blocked.
# You can only travel through open cells, so no path can go through the cell at (0, 2). There are two distinct paths to the goal.


def numberOfPaths(m):
    if m[0][0] ==0:
        return 0
    if m[-1][-1] == 0:
        return 0

    table = [[0]*(len(m[0])) for _ in range(len(m))]
    for i in range(len(m)):
        if m[i][0] == 1:
            table[i][0] = 1
        else:
            break
    for i in range(len(m[0])):
        if m[0][i] == 1:
            table[0][i] = 1
        else:
            break
    for i in range(1, len(m)):
        for j in range(1, len(m[0])):
            if m[i][j] != 0:
                table[i][j] = table[i-1][j] + table[i][j-1]
    return table[-1][-1]

# ANswer: 10
m = [[1]*4 for _ in range(3)]
print(numberOfPaths(m))

# ANswer: 10
m = [[1]*8 for _ in range(4)]
print(numberOfPaths(m))



