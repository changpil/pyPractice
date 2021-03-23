# Lomodos Partitioning
# Get the first non Negative integer

def partitionNegativeToNonNegative(nums):
    p = -1
    for cur in range(len(nums)):
        if nums[cur] < 0:
            p += 1
            nums[cur], nums[p] = nums[p], nums[cur]


nums = [-1, 0, 2, 5, -3,-4]
partitionNegativeToNonNegative(nums)
print(nums)


