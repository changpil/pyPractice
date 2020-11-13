#First Non-Repeating Integer in a List
def findFirstUnique(lst):
    # Write your code here
    dup = set()
    eToIndex = dict()

    for i, e in enumerate(lst):
        if e in eToIndex:
            dup.add(e)
            eToIndex[e] = i
        else:
            eToIndex[e] = i

    indexToe = {i: e for e, i in eToIndex.items()}

    for i in range(len(lst)):
        if i in indexToe and indexToe[i] not in dup:
            return indexToe[i]

    return None

print(findFirstUnique([1, 1, 1, 2]))
print(findFirstUnique([1, 1, 1, 2, 3, 2, 4]))