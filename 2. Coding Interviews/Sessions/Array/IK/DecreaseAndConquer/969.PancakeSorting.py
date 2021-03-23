"""
Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[0...k-1] (0-indexed).
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.



Example 1:

Input: arr = [3,2,4,1]
Output: [4,2,4,3]
Explanation:
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: arr = [3, 2, 4, 1]
After 1st flip (k = 4): arr = [1, 4, 2, 3]
After 2nd flip (k = 2): arr = [4, 1, 2, 3]
After 3rd flip (k = 4): arr = [3, 2, 1, 4]
After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.
"""

"""
Strategy: 2 steps
Get the highest and flip to top
|         7        |
flip every thing
|7                 |
The heighest is in bottom
|                 7|


"""
def pancakeSort(nums):
    result = []
    for i in range(len(nums)-1, 0, -1):
        highest_index = get_highest_index(nums, i)
        if highest_index == i:
            continue
        elif highest_index == 0:
            print(f"{i + 1} {highest_index + 1} {nums}", end="")
            flip(nums, i + 1)
            result.append(i+ 1)
            print(nums)
        else:
            print(f"{i + 1} {highest_index + 1} {nums}", end = "")
            flip(nums, highest_index + 1)
            flip(nums, i + 1)
            print(nums)
            result.extend([highest_index+1, i + 1])

    return result

def get_highest_index(nums, l):
    highest_v = nums[0]
    highest_i = 0
    for i in range(l + 1):
        if highest_v < nums[i]:
            highest_v = nums[i]
            highest_i = i
    return highest_i

def flip(nums, i):
    for idx in range(i//2):
        nums[idx], nums[i -1 - idx] = nums[i -1 - idx], nums[idx]

arr = [3,2,4,1]
print(pancakeSort(arr))


arr = [1,2,3]
print(pancakeSort(arr))