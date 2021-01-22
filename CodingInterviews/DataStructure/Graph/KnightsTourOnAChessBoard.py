# Complete the function below.
def get_neighbor(rows, cols, i, j):
    l = []

    # i = 2 j = 1
    if i+2 < rows and j+1 < cols:
        l.append((i+2, j+1))
    if i+2 < rows and j-1 >= 0:
        l.append((i+2, j-1))
    if i-2 >= 0 and j+1 < cols:
        l.append((i-2, j+1))
    if i-2 >= 0 and j-1 >= 0:
        l.append((i-2, j-1))

    # i = 1 j = 2
    if i+1 < rows and j+2 < cols:
        l.append((i+1, j+2))
    if i+1 < rows and j-2 >= 0:
        l.append((i+1, j-2))
    if i-1 >= 0 and j+2 < cols:
        l.append((i-1, j+2))
    if i-1 >= 0 and j-2 >= 0:
        l.append((i-1, j-2))

    return l

def build_graph(rows, cols):
    graph = dict()
    num = 0
    for i in range(rows):
        for j in range(cols):
            graph[(i,j)] = []
            for ii, jj in get_neighbor(rows, cols,i,j):
                graph[(i,j)].append((ii,jj))

from collections import deque
def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    graph = build_graph(rows, cols)
    queue = deque()
    queue.append((start_row, start_col))
    distance = {}
    distance[(start_row, start_col)] = 0
    visited = set()
    visited.add((start_row, start_col))
    while queue:
        node = queue.popleft()
        for i, j in get_neighbor(rows, cols, node[0], node[1]):
            if (i, j) not in visited:
                visited.add((i, j))
                distance[(i, j)] = distance[(node[0],node[1])] +1
                if i == end_row and j == end_col:
                    print(visited)
                    print(distance)
                    return distance[(i, j)]
                queue.append((i,j))
    return -1

print(find_minimum_number_of_moves(2,1,1,0,0,0))




