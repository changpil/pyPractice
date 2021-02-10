

def foo(w):
    tmp, store = [], []
    helper(w, 0, tmp, store)
    return store

def helper(a, i, tmp, store ):
    if i == len(a):
        store.append(tmp.copy())
        return
    tmp.append(a[i])
    helper(a, i+1, tmp, store)
    tmp.pop()
    helper(a, i+1, tmp, store)

def foo1(w):
    tmp, store, s = [], [], set()
    helper1(w, 0, s, tmp, store)
    return store

def helper1(a, i, s, tmp, store):
    if i == len(a):
        store.append(tmp.copy())
        return

    for num in a:
        if num not in s:
            tmp.append(num)
            s.add(num)
            helper1(a, i+1, s, tmp, store)
            s.discard(num)
            tmp.pop()