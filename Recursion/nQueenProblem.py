def find_all_arrangements(n):
    c, partial = list(), list()
    s = set()
    helper(n, 0, s, c, partial)
    transformed_c = []
    for l in c:
        t = change(l)
        transformed_c.append(t)
    return transformed_c

def helper(n, level, s,  c, partial):
    if n == level:
        c.append(partial.copy())
        return
    for i in range(n):
        if i not in s:
            if validate(partial, level, i):
                s.add(i)
                partial.append(i)
                helper(n, level +1, s, c, partial)
                partial.pop()
                s.remove(i)


def validate(tmp, x, y):
    for i in range(len(tmp)):
        x_d = abs(x -i)
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

print(find_all_arrangements(11))
