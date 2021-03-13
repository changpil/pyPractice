# Complete the function below.

import math


def check_if_sum_possible(arr, k):
    return helper(arr, k, 0, math.inf)


def helper(arr, k, i, _sum):
    if i == len(arr):
        if k == _sum:
            return True
        else:
            return False

    _in, _ex = False, False

    if _sum == math.inf:
        _in = helper(arr, k, i + 1, arr[i])
        _ex = helper(arr, k, i + 1, _sum)
    else:
        _in = helper(arr, k, i + 1, _sum + arr[i])
        _ex = helper(arr, k, i + 1, _sum)

    return _in or _ex