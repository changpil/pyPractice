# This is O(N^N) in terms of (()))
# This needs to be improved later

def removeInvalidParentheses(s):
    store = {}
    tmp = []
    minskippedN = helper(s, 0, 0, 0, 0, tmp, store)
    return list(store[minskippedN])

import math
def helper(s, i, opened, closed, skipped, tmp, store):
    if opened < closed:
        return math.inf
    if i == len(s):
        if opened == closed:
            f = store.get(skipped, set())
            f.add("".join(tmp))
            store[skipped] = f
            return skipped
        else:
            return math.infqw

    if s[i] == "(":
        tmp.append("(")
        mr1 = helper(s, i + 1, opened + 1, closed, skipped, tmp, store)
        tmp.pop()
        mr2 = helper(s, i + 1, opened, closed, skipped + 1, tmp, store)
        return min(mr1, mr2)
    elif s[i] == ")":
        mr1 = helper(s, i + 1, opened, closed, skipped + 1, tmp, store)
        tmp.append(")")
        mr2 = helper(s, i + 1, opened, closed + 1, skipped, tmp, store)
        tmp.pop()
        return min(mr1, mr2)
    else:
        tmp.append(s[i])
        mr =  helper(s, i + 1, opened, closed, skipped, tmp, store)
        tmp.pop()
        return mr

print(removeInvalidParentheses("(a)())()"))