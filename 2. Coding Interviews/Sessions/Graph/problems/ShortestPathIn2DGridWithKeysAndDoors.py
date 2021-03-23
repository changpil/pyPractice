# Shortest Path In 2D Grid With Keys And Doors
# Given a two-dimensional maze represented by a character grid, find the shortest path from start to goal cell.
# You can move vertically or horizontally—but not diagonally—one step at a time.
# There are six types of cells:
# There’s exactly one start and one goal cell. Other cells may appear any number of times.
# Water can never be visited. A door cell can only be visited after visiting a matching key, e.g. key ‘a’ for door ‘A’.
# Other cells can be visited unconditionally. It is allowed to visit a cell more than once.
#

from collections import deque
def getStarAndEndPoints(grid):
    start, end = None, None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "+":
                end = (i,j)
            if grid[i][j] == "@":
                start = (i, j)
    return start, end

def nextMoves(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    moves = [(x+1,y), (x-1,y), (x,y+1),(x,y-1)]
    for i, j in moves:
        if not( 0<= i < rows and 0<= j <cols):
            continue
        if grid[i][j] == "#":
            continue
        if grid[i][j] == "@":
            continue
        yield (i,j)
# BFS does not work for finding key and open the door. Because shortest path can not to grep the key.
# There is no backtracking
def find_shortest_path(grid):
    visited, queue, parent = set(), deque(), dict()
    start, end = getStarAndEndPoints(grid)
    if start == None or end == None:
        return -1

    queue.append((start[0], start[1], 0))
    visited.add((start[0], start[1], 0))
    parent[(start[0], start[1], 0)] = None
    newKey = None
    while queue:
        i, j, key = queue.popleft()
        newKey = None
        if (i,j) == end:
            newKey = key
            break
        if grid[i][j].islower():
            newKey = key | 1 << ord(grid[i][j]) - ord('a')
        if grid[i][j].isupper():
            mask = 1 << ord(grid[i][j]) - ord("A")
            if (key >> ord(grid[i][j]) - ord("A")) & 1:
                newKey = key & ~mask
            else:
                continue
        if newKey == None:
            newKey = key

        for x, y in nextMoves(grid, i, j):
            if (x,y,newKey) not in visited:
                queue.append((x,y,newKey))
                visited.add((x,y,newKey))
                parent[(x,y,newKey)] = (i,j,key)

    if (end[0], end[1], newKey) not in parent:
        return -1
    trace = (end[0], end[1], newKey)
    traceList = deque()
    while trace:
        traceList.appendleft((trace[0], trace[1]))
        trace = parent[trace]
    return list(traceList)


grid = ["...B",".b#.","@#+."]
print(find_shortest_path(grid))
# grid = ["+B..." ,"####." ,"##b#." ,"a...A" , "##@##"]
# print(find_shortest_path(grid))

# import math
#
# def nextMoves_DFS(grid, x, y):
#     rows, cols = len(grid), len(grid[0])
#     moves = [(x+1,y), (x-1,y), (x,y+1),(x,y-1)]
#     for i, j in moves:
#         if not(0<= i < rows and 0<= j <cols):
#             continue
#         if grid[i][j] == "#":
#             continue
#         if grid[i][j] == "@":
#             continue
#         yield (i,j)
#
# def find_shortest_path_DFS(grid):
#     visited, tmp, store, level, = set(), [], {}, 0
#     start, end = getStarAndEndPoints(grid)
#     if start == None or end == None:
#         return -1
#     minNumPath = helper_DFS(grid, (start[0], start[1], 0) , end , level, visited, tmp, store )
#     if minNumPath == math.inf:
#         return -1
#     return store[minNumPath]
#
#
# def helper_DFS(grid, cur ,end, level, visited, tmp, store):
#     i, j, key = cur[0], cur[1], cur[2]
#     if (i, j) == end:
#         tmp.append((i,j))
#         store[level] = tmp.copy()
#         tmp.pop()
#         return level
#
#     # Lower ch: Add Keys["A"] in {(1,2), (4,3)}
#     if grid[i][j].islower():
#         key = key | (1 << ord(grid[i][j]) - ord("a"))
#     # Upper Ch: remove the Key if a key exists and Continue
#     #         : no proceed if it has no key
#     if grid[i][j].isupper():
#         mask = 1 << ord(grid[i][j]) - ord("A")
#         if (key >> ord(grid[i][j]) - ord("A")) & 1:
#             key = key & ~mask
#         else:
#             return math.inf
#
#     visited.add((i,j,key))
#     tmp.append((i,j))
#
#     minLevel = math.inf
#     for x, y in nextMoves_DFS(grid, cur[0], cur[1]):
#         # Move to next point if the move was not visited.
#         # Or visited but keys has been changed
#         if (x,y, key) not in visited:
#             rLevel = helper_DFS(grid, (x,y,key), end, level+1, visited, tmp, store)
#             minLevel = min(minLevel, rLevel)
#
#     visited.discard((i,j,key))
#     tmp.pop()
#     return minLevel
#
# grid = ["...B",".b#.","@#+."]
# print(find_shortest_path_DFS(grid))
# grid = ["+B..." ,"####." ,"##b#." ,"a...A" , "##@##"]
# print(find_shortest_path_DFS(grid))