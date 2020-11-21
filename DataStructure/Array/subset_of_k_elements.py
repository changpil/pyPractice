"""
Implement algorithm taht takes A and integer k and returns a subset of k elements of A.
"""
import random

def subset(_list, k):
    if k > len(_list):
        return None

    if k == len(_list):
        return _list

    picked_indexies=[]
    results=[]
    for k_i in range(k):
        while True:
            index = random.randint(0, len(_list)-1)
            if (picked_indexies.count(index) == 0):
                picked_indexies.append(index)
                results.append(_list[index])
                break
    return results

a =[1,-1,2,5,7,9,32,45,32,11,67,-44,5,6]
print(a)
print(subset(a, 5))

"""
Use O(knapsack) additioal storage
use as few calls to trh random
"""
def subset_upgraded(_list, k):
    if k > len(_list):
        return None

    if k == len(_list):
        return _list

    i_p =0
    for k_i in range(k):
        random_i = random.randint(0, len(_list)-1)
        temp = _list[i_p]
        _list[i_p] = _list[random_i]
        _list[random_i] = temp
        i_p += 1

    return _list[:k]

print(subset_upgraded(a, 5))
