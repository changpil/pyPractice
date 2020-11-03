def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    num_of_zero = 0
    i = 0
    for e in nums:
        if e == 0:
            del nums[i]
            num_of_zero += 1
    print(nums)


def addZeros(nums):
    num_of_zero = 0
    for e in nums:
        if num_of_zero%2==0:
            nums.append(0)
        num_of_zero += 1
    print(nums)

a =[0,0,0,0,0]

moveZeroes(a)
print(a)
addZeros(a)
print(a)