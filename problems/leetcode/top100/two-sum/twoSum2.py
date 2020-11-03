# Wrong Answer
# def twoSum(nums, target):
#     d = {}
#     for i, v in enumerate(nums):
#         if v not in d:
#             d[v] = i
#
#     print(d)
#     for i, v in enumerate(nums):
#         t = target - v
#         if t in d:
#             return [i, d[t]]
#
#     return []
#
# # NOt working condition The solution is not [0,0]
# print(twoSum([3,2,4], 6))


def twoSum(nums, target):
    d = {}
    # A value can be duplicated in positions
    for i, v in enumerate(nums):
        # d[v] = d.get(v, []).append(i) stores only None
        d[v] = d.get(v, [])
        d[v].append(i)

    print(d)
    for i, v in enumerate(nums):
        t = target - v
        if t in d:
            l = d[t]
            for another_index in l:
                if another_index != i:
                    return [i, another_index]

    return []

# NOt working condition The solution is not [0,0]
print(twoSum([3,2,4], 6))

# computation O(n^1)
# Storage O(n)

# Runtime: 56 ms, faster than 48.26% of Python online submissions for Two Sum.
# Memory Usage: 15.9 MB, less than 52.34% of Python online submissions for Two Sum.