def missingElement(nums, k):
    a = nums[0]

    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        missings = nums[mid] - (a + mid)
        if missings >= k:
            end = mid - 1
        else:
            start = mid + 1

    return nums[end] + (k - (nums[end] - (a + end)))

nums = [4,7,9,10]
k = 3

print(missingElement(nums, k))