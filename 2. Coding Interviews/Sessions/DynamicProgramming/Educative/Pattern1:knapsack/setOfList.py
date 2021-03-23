def create_set(n):
    s, l = list(), list()
    _create(n, 0, s, l)
    return s

def _create(n, i, s, l):
    if len(n) == 1:
        return n

    if i >= len(n):
        # I had an error with "s.append(l)"
        # The output was "[[], [], [], [], [], [], [], []]"
        s.append(l.copy())
        return

    _create(n, i + 1, s, l)
    l.append(n[i])
    _create(n, i + 1, s, l)
    l.pop()


print(create_set(["a", "b", "c"]))