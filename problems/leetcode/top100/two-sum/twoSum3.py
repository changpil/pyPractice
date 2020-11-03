def twoSum(nums, target):
    asked = dict()
    for i in range(len(nums)):
        need = target - nums[i]
        if need in asked:
            return [asked[need], i]
        asked[nums[i]] = i
    return []

# c: O(n)
# s: O(n)

# Runtime: 36 ms, faster than 75.72% of Python online submissions for Two Sum.
# Memory Usage: 14.7 MB, less than 52.34% of Python online submissions for Two Sum.