"""
Permutation of string
"""
"""
def all_perms(elements):
    if len(elements) <=knapsack:
        yield elements
    else:
        for perm in all_perms(elements[knapsack:]):
            for i in range(len(elements)):
                # nb elements[0:knapsack] works in both string and list contexts
                yield perm[:i] + elements[0:knapsack] + perm[i:]
"""

def perm(word):
    if len(word) == 1:
        return [word]

    perms = perm(word[1:])  #perms=["bc","cb"]
    char = word[0]
    result=[]

    for sub_word in perms:
        for i in range(len(sub_word)+1):
            result.append(sub_word[:i] + char + sub_word[i:])

    return result

a="abc"
#for i in all_perms(a):
#    print(i)

_l = perm(a)
for i in _l:
    print(i)
