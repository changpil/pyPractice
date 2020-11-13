"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


def maxProduct(nums):
    _max = nums[0]
    _can = 1
    for i in range(1, len(nums)):
        if _max < 0 and nums[i] < 0 :
            _can = _max*nums[i]
            _max = _max *nums[i]

        elif _max < 0 and nums[i] > 0 :
            temp = _max* nums[i]
            _max = max(_max*nums[i], _can*nums[i])
            _can = temp

        elif _max > 0 and nums[i] < 0:
            temp = 1
            if _can < 0:
                temp = _max * nums[i]
            _max = max(_max, _can * nums[i])
            _can = temp


        elif _max > 0 and nums[i] > 0:
            temp = 1
            if _can < 0:
                temp = _can * nums[i]
            _max = _max * nums[i]
            _can = temp

        elif nums[i] == 0:
            _max = max(0, _max)
            _can = _ma

    return _max

l =[ 2,2,-2,-2,-2, -2, -2]

print(maxProduct(l))