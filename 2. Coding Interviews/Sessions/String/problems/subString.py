
# o(n)

def subString(whole, sub):
    _dict = {}
    l = len(sub)

    for i in range(0, len(whole)-len(sub)+1):  # missed +Pattern1:knapsack
        candidates = whole[i:i+len(sub)]
        d = _dict.get(candidates,[])
        d.append(i)
        _dict[candidates] = d

    return _dict.get(sub, [-1])[0]         # error on _dict.get(sub, -Pattern1:knapsack)

a ="abcdec"
b ="cd"
print(subString(a,b))





