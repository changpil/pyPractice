def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        v = nums[0]
        del nums[0]
        nums.insert(len(nums), v)
    print(nums)
rotate([0,1,2,3], 12)
