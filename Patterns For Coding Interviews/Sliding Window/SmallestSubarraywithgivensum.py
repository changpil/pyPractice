# Smallest Subarray with a given sum
# Given an array of positive numbers and a positive number ‘S,’
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
# Return 0 if no such subarray exists.

def smallestContinuousSubarray(nums, s):
    l,r =0,0
    _sum =0
    while r < len(nums) and _sum < s:
        _sum += nums[r]
        r += 1

    if _sum < s:
        return 0

    noe = r

    while r < len(nums):
        if _sum >= s:
            noe = min(noe, r -l)
            _sum -= nums[l]
            l+=1
        else:
            _sum += nums[r]
            r +=1

    while l < len(nums):
        if _sum >= s:
            noe = min(noe, r -l)
            _sum -= nums[l]
        l+=1
    return noe

print(smallestContinuousSubarray([2, 1, 5, 2, 3, 2], 7))
print(smallestContinuousSubarray([2, 1, 5, 2, 8], 7))
print(smallestContinuousSubarray([3, 4, 1, 1, 6], 8))

print(smallestContinuousSubarray([1, 1, 1, 1, 11], 8))