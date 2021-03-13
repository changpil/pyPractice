def find_all_arrangements(n):
    tmp, store = list(), list()
    visited = set()
    helper(n, 0, visited, tmp, store)
    transformed_c = []
    for l in store:
        t = change(l)
        transformed_c.append(t)
    return transformed_c

def helper(n, x, visited,  tmp, store):
    if n == x:
        store.append(tmp.copy())
        return
    for y in range(n):
        if y not in visited:
            if validate(tmp, x, y):
                visited.add(y)
                tmp.append(y)
                helper(n, x + 1, visited, tmp, store)
                tmp.pop()
                visited.remove(y)


def validate(tmp, x, y):
    for i in range(len(tmp)):
        x_d = abs(x - i)
        y_d = abs(y - tmp[i])
        if x_d == y_d:
            return False
    return True

def change(l):
    arr = []
    for i in range(len(l)):
        s = "-"*len(l)
        s = s[:l[i]] + "q" + s[l[i]+1:]
        arr.append(s)
    return arr

#TIme Speed !!!!
# n = 11  0.9 sec
# n = 12  4.6 sec
# n = 13  24.12
import time
start = time.time()
all = find_all_arrangements(11)
end = time.time()
print(end - start)
