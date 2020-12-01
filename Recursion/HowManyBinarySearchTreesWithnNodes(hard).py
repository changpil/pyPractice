def how_many_BSTs(n):
    arr = [i for i in range(n)]
    n = helper(arr)
    return n

def helper(arr):
    if len(arr) == 1:
        return 1
    total= 0
    for i in range(len(arr)):
        left, right = 0, 0
        if not (0 < i < len(arr)):
            left = helper(arr[:i])
            right = helper(arr[i + 1:])
        else:
            if len(arr[:i]) == len(arr[i + 1:]):
                left = helper(arr[:i])
            #elif len(arr[:i]) < len(arr[i + 1:]):
            #    right = helper(arr[i + 1:])
            else:
                left = max(helper(arr[:i]), helper(arr[i + 1:]))
        total += left + right
    return total

print(how_many_BSTs(5))