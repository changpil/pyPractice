# Complete the function below.
# First Implementation
# def get_neighbor(rows, cols, i, j):
#     l = []
#
#     # i = 2 j = 1
#     if i+2 < rows and j+1 < cols:
#         l.append((i+2, j+1))
#     if i+2 < rows and j-1 >= 0:
#         l.append((i+2, j-1))
#     if i-2 >= 0 and j+1 < cols:
#         l.append((i-2, j+1))
#     if i-2 >= 0 and j-1 >= 0:
#         l.append((i-2, j-1))
#
#     # i = 1 j = 2
#     if i+1 < rows and j+2 < cols:
#         l.append((i+1, j+2))
#     if i+1 < rows and j-2 >= 0:
#         l.append((i+1, j-2))
#     if i-1 >= 0 and j+2 < cols:
#         l.append((i-1, j+2))
#     if i-1 >= 0 and j-2 >= 0:
#         l.append((i-1, j-2))
#
#     return l
#
# def build_graph(rows, cols):
#     graph = dict()
#     num = 0
#     for i in range(rows):
#         for j in range(cols):
#             graph[(i,j)] = []
#             for ii, jj in get_neighbor(rows, cols,i,j):
#                 graph[(i,j)].append((ii,jj))
#
# from collections import deque
# def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
#     graph = build_graph(rows, cols)
#     queue = deque()
#     queue.append((start_row, start_col))
#     distance = {}
#     distance[(start_row, start_col)] = 0
#     visited = set()
#     visited.add((start_row, start_col))
#     while queue:
#         node = queue.popleft()
#         for i, j in get_neighbor(rows, cols, node[0], node[1]):
#             if (i, j) not in visited:
#                 visited.add((i, j))
#                 distance[(i, j)] = distance[(node[0],node[1])] +1
#                 if i == end_row and j == end_col:
#                     print(visited)
#                     print(distance)
#                     return distance[(i, j)]
#                 queue.append((i,j))
#     return -1

from collections import deque
def nightMoves(rows, cols, i, j):
    moves = [(i + 1, j + 2), (i + 2, j + 1), (i - 1, j + 2), (i - 2, j + 1),
             (i + 1, j - 2), (i + 2, j - 1), (i - 1, j - 2), (i - 2, j - 1)]
    for next_i, next_j in moves:
        if 0 <= next_i < rows and 0 <= next_j < cols:
            yield (next_i, next_j)

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    # Write your code here.
    if not (0 <= start_row < rows) or not (0 <= start_col < cols):
        return -1

    queue, visited = deque(), set()
    queue.append((start_row, start_col, 0))
    visited.add((start_row, start_col))

    while queue:
        tmp = queue.popleft()
        i, j, level = tmp[0], tmp[1], tmp[2]

        if i == end_row and j == end_col:
            return level

        for next_i, next_j in nightMoves(rows, cols, i, j):
            print(f"{i}  {j} {next_i} {next_j}")
            if (next_i, next_j) not in visited:
                visited.add((next_i, next_j))
                queue.append((next_i, next_j, level + 1))
        print("####")
    return -1

print(find_minimum_number_of_moves(2,7,0,5,1,1))




