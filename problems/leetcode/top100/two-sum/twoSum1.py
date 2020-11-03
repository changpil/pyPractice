def twoSum(nums, target):
    for a_i in range(len(nums)):
        for b_i in range(a_i + 1, len(nums)):
            if target == nums[a_i] + nums[b_i]:
                return [a_i, b_i]

    return []

# computation O(n^2)
# Storage O(1)