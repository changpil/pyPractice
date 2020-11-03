def largestSumOfSunarray(l):
    _max = l[0]
    candidate = l[0]

    for i in range(1, len(l)):
        if _max < 0 and l[i] <= 0:
            _max = max(l[i], _max)
        elif _max > 0 and l[i] <= 0:
            candidate = candidate + l[i]
        elif i > 0 and l[i-1] < 0:
            _max = max(_max , _max + candidate, l[i])
        else:
            _max = max(_max + l[i], _max + candidate, l[i])
    return _max

l =[-1,-2,-3,-4,-5]
print(largestSumOfSunarray(l))