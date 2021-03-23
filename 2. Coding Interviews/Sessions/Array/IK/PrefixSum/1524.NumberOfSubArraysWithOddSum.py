"""
Given an array of integers arr. Return the number of sub-arrays with odd sum.

As the answer may grow large, the answer must be computed modulo 10^9 + 7.



Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All sub-arrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All sub-arrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16
Example 4:

Input: arr = [100,100,99,99]
Output: 4
Example 5:

Input: arr = [7]
Output: 1

"""

def numOfSubarrays(nums):
    hmap = {0:1, 1:0}
    count = 0
    prefixSum = 0
    for num in nums:
        prefixSum = prefixSum + num
        if prefixSum % 2 == 1:
            count += hmap[0]
        else:
            count += hmap[1]
        hmap[prefixSum%2] += 1
    return count


nums = [1,3, 5] # 4
print(numOfSubarrays(nums))

nums = [ 2,4,6] # 0
print(numOfSubarrays(nums))

nums = [1,2,3,4,5,6,7] # 16
print(numOfSubarrays(nums))

nums = [100,100,99,99] # 4
print(numOfSubarrays(nums))

nums = [7] # 1
print(numOfSubarrays(nums))