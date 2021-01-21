def productExceptSelf(nums):

    leftArray = []
    p = 1
    for num in nums:
        leftArray.append(p)
        p = p*num
    rightArray = [0]*len(nums)

    p = 1
    for i in range(len(nums)-1, -1, -1):
        rightArray[i] = p
        p = p* nums[i]

    for i in range(len(nums)):
        s = leftArray[i] * rightArray[i]
        leftArray[i] = s

    return leftArray

print(productExceptSelf([2,4,6]))