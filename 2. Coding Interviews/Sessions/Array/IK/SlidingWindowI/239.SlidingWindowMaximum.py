"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]

Time Complexity: O(N)
The algorithm is quite straigthforward :
Process the first k elements separately to initiate the deque.
Iterate over the array. At each step :
Clean the deque :
Keep only the indexes of elements from the current sliding window.
Remove indexes of all elements smaller than the current one, since they will not be the maximum ones.
Append the current element to the deque.
Append deque[0] to the output.
Return the output array.


"""

from heapq import *
import collections
def maxSlidingWindow(nums, k):

    windowMax = []
    queue = collections.deque()
    for i in range(k):
        j = len(queue) -1
        while j >= 0 and queue[j] < nums[i]:
            queue.pop()
            j -= 1
        queue.append(nums[i])
    windowMax.append(queue[0])

    for i in range(k, len(nums)):
        if nums[i-k] == queue[0]:
            queue.popleft()

        j = len(queue) - 1
        while j >= 0 and queue[j] < nums[i]:
            queue.pop()
            j -= 1
        queue.append(nums[i])
        windowMax.append(queue[0])
    return windowMax

nums = [1,3,-1,-3,5,3,6,7]
print(maxSlidingWindow(nums, 3))

nums = [1, -1]
print(maxSlidingWindow(nums, 1))