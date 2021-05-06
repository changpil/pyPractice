# Complete the function below.
def find_all_arrangements(n):
    tmp, store = [], []
    visited = set()
    returnGrid = []

    for col in range(n):
        foo(n, 0 , col, 0, tmp, visited, store)
        for da in store:
            returnGrid.append(stringGrid(n, da))
        visited.clear()
        tmp.clear()
        store.clear()

    return returnGrid


def foo(n, row, col, queen, tmp, visited, store):
    visited.add((row, col))
    tmp.append((row, col))
    queen += 1
    if queen == n:
        store.append(tmp.copy())
        visited.remove((row, col))
        tmp.pop()
        return

    for x, y in getNextRowDirections(n, visited, row):
        foo(n, x, y, queen, tmp, visited, store)

    visited.remove((row, col))
    tmp.pop()


def getNextRowDirections(n, visited, row):
    for x in range(n):
        if validMove(visited, row + 1, x):
            yield (row + 1, x)


def validMove(visited, row, col):
    for x, y in visited:
        if x == row:
            return False
        if y == col:
            return False
        if abs(x - row) / abs(y - col) == 1.0:
            return False
    return True


def stringGrid(n, points):
    sg = []
    for i in range(n):
        line = []
        for j in range(n):
            if (i, j) not in points:
                line.append("-")
            else:
                line.append("q")
        sg.append("".join(line))
    return sg

#TIme Speed !!!!
#TIme Speed !!!!
# n = 11  1.9 sec
# n = 12  11 sec
# n = 13  68 sec
import time
start = time.time()
all = find_all_arrangements(5)
end = time.time()
print(end - start)

all =find_all_arrangements(5)
for line in all:
    print(line)