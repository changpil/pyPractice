
# My solution
# def findMaxConsecutiveOnes(nums):
#     zeroIndex = []
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             zeroIndex.append(i)
#
#     if not zeroIndex:
#         return sum(nums)
#
#     max1 = 0
#     for index in zeroIndex:
#         i, j = index - 1, index + 1
#         left1, right1 = 0, 0
#         while i >= 0 and nums[i] == 1:
#             left1 += 1
#             i -= 1
#         while j < len(nums) and nums[j] == 1:
#             right1 += 1
#             j += 1
#         max1 = max(max1, left1 + right1 + 1)
#     return max1


# General window solution
def findMaxConsecutiveOnes(nums):
    i, j = 0, 0
    max1 = 0
    zeros = 0


    while j < len(nums):
        if nums[j] == 0:
            zeros += 1

        while i < j and zeros == 2 :
            if nums[i] == 0:
                zeros -= 1
            i += 1
        max1 = max(max1, j - i +1)
        j += 1
    return max1

a = [1,1,1,0,0,1,0,1]

print(findMaxConsecutiveOnes(a))