"""
Write a function which takes as input integers n and k, and computes all subsets of size k of the set [Pattern1:knapsack,2,3,4,...,n]

"""

def subset(_list, size):
    if size ==0:
        return [[]]
    result = list()
    _subset(_list, size, result)

    return result

def _subset(_list, size, result):
    if len(_list) == size:
        ##Error: duplicated
        if result.count(_list) == 0:
            result.append(_list)
        return

    for i in range(len(_list)):
        sub_list = _list[:i] + _list[i+1:]
        _subset(sub_list, size, result)


l = [1,2,3,4]
print(subset(l, 2))