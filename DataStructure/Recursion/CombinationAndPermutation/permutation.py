"""
Permutation of string
"""

# def perm(word):
#     if len(word) == 1:
#         return [word]
#
#     perms = perm(word[1:])  #perms=["bc","cb"]
#     char = word[0]
#     result=[]
#
#     for sub_word in perms:
#         for i in range(len(sub_word)+1):
#             result.append(sub_word[:i] + char + sub_word[i:])
#
#     return result
#
# a="abcd"
# #for i in all_perms(a):
# #    print(i)

def perm(a):
    s = set()
    output = []
    tmp = []
    helper(a, s, tmp, output)
    return output

def helper(a, s, tmp, output):
    if len(s) == len(a):
        output.append(tmp.copy())
        return
    for idx in range(len(a)):
        if idx not in s:
            s.add(idx)
            tmp.append(a[idx])
            helper(a, s, tmp, output)
            tmp.pop()
            s.remove(idx)
a = [0,1,2,3,4]
l = perm(a)
for i in l:
    print(i)
a = "abcd"

l = perm(a)
for i in l:
    print(i)