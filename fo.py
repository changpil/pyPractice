def getDirections(n, i, j):
    directions = [(i - 1, j + 2), (i + 1, j + 2), (i + 2, j + 1), (i + 2, j - 1), (i - 1, j - 2), (i + 1, j - 2), (i - 2, j - 1), (i - 2, j + 1)]
    #d = set()
    for x, y in directions:
        if 0 <= x < n and 0 <= y < n :
            yield (x, y)
            #d.add((x, y))
    #return d

def validMove(visited, x, y):
    if (x,y) in visited:
        return False

    for i, j in visited:
        if i == x :
            return False
        if j == y:
            return False
        if abs(i-x) / abs(j-y) == 1.0:
            return False
    return True

def find_all_arrangements(n):
    tmp, store = [], set()
    visited = set()
    returnGrid = []

    for i in range(1, 2):
        foo(n, 0, i, 0, tmp, visited, store)
        visited.clear()
        tmp.clear()
        print(len(store))
    for da in store:
        returnGrid.append(stringGrid(n, da))

    return returnGrid


def foo(n, i, j, queen, tmp, visited, store):
    visited.add((i, j))
    tmp.append((i, j))
    queen += 1
    if queen == 4:
        print(tmp)
    if queen == n:
        tmp
        cp = tmp.copy()
        cp.sort()
        store.add(tuple(cp))
        visited.remove((i, j))
        tmp.pop()
        return
    # visited.add((i, j))
    # tmp.append((i, j))
    # queen += 1
    for x, y in getDirections(n, i, j):
        if validMove(visited, x, y):
            foo(n, x, y, queen, tmp, visited, store)

    visited.remove((i, j))
    tmp.pop()

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

#print(find_all_arrangements(4))
for a in find_all_arrangements(5):
    print(a)