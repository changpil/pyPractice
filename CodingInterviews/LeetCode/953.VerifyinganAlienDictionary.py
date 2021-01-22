
def compare(d, a, b):
    for i in range(min(len(a), len(b))):
        if d[a[i]] > d[b[i]]:
            return -1
        elif d[a[i]] < d[b[i]]:
            return 1

    if len(a) == len(b):
        return 0

    if len(a) > len(b):
        return -1
    return 1

def isAlienSorted(words, order):
    order_dict = {}
    for index, ch in enumerate(order):
        order_dict[ch] = index

    for i in range(len(words) - 1):
        if compare(order_dict, words[i], words[i + 1]) < 0:
            return False
    return True

print(isAlienSorted(["word","world","row"],"worldabcefghijkmnpqstuvxyz" ))