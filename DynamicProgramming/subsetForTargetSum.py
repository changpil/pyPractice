# Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.

#Brute Force

def subsetForSum(nums, t):
    return _subsetForSum(nums, 0, t, 0 )

def _subsetForSum(nums, i, t, _sum):
    if i >= len(nums) and t == _sum:
        return True
    if i >= len(nums) and t != _sum:
        return False

    re = _subsetForSum(nums, i + 1, t, _sum + nums[i])
    if re:
        return re
    return _subsetForSum(nums, i + 1, t, _sum)

print(subsetForSum([1,2,3,7], 6))
print(subsetForSum([1,2,7,1,5], 10))
print(subsetForSum([1,3,4,8], 6))