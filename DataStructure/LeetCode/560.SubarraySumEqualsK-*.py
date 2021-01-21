
# Example
# 1:
#
# Input: nums = [1, 1, 1], k = 2
# Output: 2
# Example
# 2:
#
# Input: nums = [1, 2, 3], k = 3
# Output: 2

# Time Limit Exceeded
# O(n^3)
# def subarraySum(nums, k):
#     totalNum = 0
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)+1):
#             if sum(nums[i:j]) == k:
#                 totalNum += 1
#
#     return totalNum

#print(subarraySum([1,2,1,2,1], 3))

# Time Limit Exceeded
# O(n^2)
# def subarraySum(nums, k):
#
#     #subsums = [0]*len(nums)
#     #s = 0
#     #for i in range(len(nums)):
#     #    s+= nums[i]
#     #    subsums[i] = s
#     val = 0
#     for i in range(len(nums)):
#         s = 0
#         for j in range(i, len(nums)):
#             s+= nums[j]
#             if s == k:
#                 val += 1
#     return val

def subarraySum(nums, k):
    sumuntili = {}
    sumuntili[0] = 1
    s = 0
    targetHit = 0
    for i in range(len(nums)):
        s += nums[i]
        targetval = s - k
        if targetval in sumuntili:
            # We need count the same value
            # No targetHit += 1
            targetHit += sumuntili[targetval]

        sumuntili[s] = sumuntili.get(s, 0) + 1
    return targetHit

print(subarraySum([1,2,3], 3))

print(subarraySum([1,2,1,2,1], 3))

print(subarraySum([1, -1, 0], 0))