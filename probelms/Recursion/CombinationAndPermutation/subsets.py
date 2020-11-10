
def subset(l):

    subsets = set()
    word = "".join(l)
    _subset(word, subsets, len(word) )
    return subsets

def _subset(word, subsets, level):
    if level == 0:
        return subsets.add("")

    subsets.add(word)
    for i in range(0, len(word)):
        disect_w = word[:i] + word[i+1:]
        _subset(disect_w, subsets, level -1)


s=["a", "b", "c"]
print(subset(s))