"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))


Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
"""


class NumArray1:
    # Initialize O(1)
    # S(n) = O(1)
    # O(n) = O(n)
    def __init__(self, nums):
        self.nums = nums
    def sumRange(self, i, j):
        return sum(self.nums[i:j+1])

numArray = NumArray1([-2, 0, 3, -5, 2, -1]);
print(numArray.sumRange(0, 2)) # return 1 ((-2) + 0 + 3)
print(numArray.sumRange(2, 5)) # return -1 (3 + (-5) + 2 + (-1))
print(numArray.sumRange(0, 5)) # return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

# Store all the answers to the n(n-1)/2 queries in a hash table
class NumArray2:
    # Initialize O(n^2)
    # S(n) = O(N^2)
    # O(n) = O(1)
    def __init__(self, nums):
        self.nums = nums
        self.sum = {}
        for i in range(len(nums)):
            runningSum = 0
            for j in range(i, len(nums)):
                runningSum += nums[j]
                self.sum[(i,j)] = runningSum

    def sumRange(self, i, j):
        return self.sum[(i,j)]

numArray = NumArray2([-2, 0, 3, -5, 2, -1]);
print(numArray.sumRange(0, 2)) # return 1 ((-2) + 0 + 3)
print(numArray.sumRange(2, 5)) # return -1 (3 + (-5) + 2 + (-1))
print(numArray.sumRange(0, 5)) # return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

class NumArray3:
    # Initialize O(n)
    # S(n) = O(n)
    # O(n) = O(1)
    def __init__(self, nums):
        self.nums = nums
        self.runningSum = []
        s = 0
        for num in nums:
            s += num
            self.runningSum.append(s)

    def sumRange(self, i, j):
        if j < i or not (0 <= i < len(self.nums)) or not (0 <= j < len(self.nums)):
            raise IndexError

        if i == 0:
            return self.runningSum[j]
        return self.runningSum[j] - self.runningSum[i-1]

numArray = NumArray3([-2, 0, 3, -5, 2, -1]);
print(numArray.sumRange(0, 2)) # return 1 ((-2) + 0 + 3)
print(numArray.sumRange(2, 5)) # return -1 (3 + (-5) + 2 + (-1))
print(numArray.sumRange(0, 5)) # return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))