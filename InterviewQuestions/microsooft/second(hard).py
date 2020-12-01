def solution(A, K):
    # if len(A) < K:
    #     return -1
    # if K %2 == 0:
    #     A.sort(reverse=True)
    #     t = 0
    #     for i in range(K):
    #         t += A[i]
    #     return t
    return helper(A, K, 0, 0)

def helper(arr, k, start, max_even):
    #if start > len(arr):
    #    return -1
    if k == 0:
        if max_even%2 == 0:
            return max_even
        else:
            return -1
    _max = -1
    for i in range(start, len(arr)):
        m = helper(arr,k -1, i+1, max_even+arr[start])
        _max = max(_max, m)
    return _max

print(solution([4, 9, 8, 2, 6], 3))
print(solution([5, 6, 3, 4, 2], 3))
print(solution([7,7,7,7], 1))




def maxEvenSum(arr, k):
    arr.sort()
    even, odd = list(), list()
    for e in arr:
        if e%2 == 0:
            even.append(e)
        else:
            odd.append(e)

    maxeven = 0
    maxodd = 0
    print(f"0 {maxeven} {maxodd}")
    for i in range (k):
        e = even.pop() if len(even) != 0 else 0
        o = odd.pop() if len(odd) != 0 else 0
        print(f"even {e} odd {o}")
        tmp = max(maxeven + e, maxodd + o)
        maxodd = max(maxeven + o, maxodd + e)
        maxeven = tmp
        print(f"{i} {maxeven} {maxodd}")
    return maxeven

print(maxEvenSum([4, 9, 8, 2, 6], 3))
#print(maxEvenSum([5, 6, 3, 4, 2], 3))
# print(maxEvenSum([7,7,7,7], 1))