def solution(A):
    d = dict()
    for e in A:
        key = digitsSum(e)
        v= d.get(key,[])
        v.append(e)
        d[key] = v

    max_return = -1
    for vals in d.values():
        if len(vals) < 2:
            continue
        vals.sort()
        max_return = max(max_return, vals[-1] + vals[-2] )

    return max_return

def digitsSum(num):
    t = 0
    while True:
        d, m = divmod(num, 10)
        t+=d
        num = m
        if d == 0:
            t+= m
            break
    return t

print(solution([51,32,43]))