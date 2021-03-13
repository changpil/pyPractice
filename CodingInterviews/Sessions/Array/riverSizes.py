def riverSizes(matrix):
    result = []
    visited = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            n = traverse(matrix, i, j, visited)
            if n != 0:
                result.append(n)
    return result


def traverse(grid, i, j, visited):
    if (i, j) in visited:
        return 0
    if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])):
        return 0

    visited.add((i, j))
    if grid[i][j] == 0:
        return 0
    river = 1
    # if (i+1, j) not in visited:
    river += traverse(grid, i + 1, j, visited)
    # if (i-1, j) not in visited:
    river += traverse(grid, i - 1, j, visited)
    # if (i, j+1) not in visited:
    river += traverse(grid, i, j + 1, visited)
    # if (i, j-1) not in visited:
    river += traverse(grid, i, j - 1, visited)
    return river

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]

print(riverSizes(matrix))

matrix = [
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 1]
]
print(riverSizes(matrix))