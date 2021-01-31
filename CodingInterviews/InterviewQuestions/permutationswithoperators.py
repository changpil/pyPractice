'''

Output formula permutations with operators, all input integers are positive and no duplicate

input: [1,2]
output: ['1+2','2+1','1-2','2-1','1*2','2*1','1/2','2/1']

input: [1,2,3]
output: ['1+2+3', '1-2-3', '1*2/3', '1/2*3', '2+1+3', '2-1*3', '2*1/3', '2/1+3'.......];


NOTE:

operators can duplicate within a formula string
operators are + - * / only
no time complexity requirement or concerns

'''

'''
             all permutation: [1, 2]  [2, 1]
             each permutaion I can run operations. 

             '1'

        '1+2'  '1-2' '1* 2'  '1/2'
        O(4^n)

        O(n^n)

        O(n^n*4^n)
'''


# DFS
def getPermutation(l, i, s, tmp, store):
    if i >= len(l):
        store.append(tmp.copy())
        return

    for n in range(len(l)):
        if n not in s:
            s.add(n)
            tmp.append(l[n])
            getPermutation(l, i + 1, s, tmp, store)
            tmp.pop()
            s.discard(n)
#BFS
def perm(input, i):
    if i >= len(input):
        return [[]]

    pre = perm(input, i+1)
    result = []
    for l in pre:
        for j in range(len(l)+1):
            tmp = l[:j] + [input[i]] + l[j:]
            result.append(tmp)
    return result


# ["1", "2"]
# Formal way
def operation(l, i, tmp, store):
    if i >= len(l):
        store.append("".join(tmp))
        return

    if i == 0:
        tmp.append(l[i])
        operation(l, i + 1, tmp, store)
        tmp.pop()
    else:
        for op in "+-*/":
            tmp.append(op + l[i])
            operation(l, i + 1, tmp, store)
            tmp.pop()


def foo(input):
    rel = []
    s = set()
    ll = []
    tmp = []

    #getPermutation(input, 0, s, tmp, ll)
    ll = perm(input, 0)
    for l in ll:
        strl = list(map(lambda x: str(x), l))
        tmps = []
        store = []
        operation(strl, 0, tmps, store)
        rel.extend(store)
        store.clear()

    return rel


input = [1, 2]

# tmp = []
# s = set()
# store = []
# getPermutation(input, 0, s, tmp, store)
# print(store)
# print(foo(input))


input = [1, 2, 3]
print(foo(input))