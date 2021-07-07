"""
IK String Session 1/26/2021
Fin dthe smallest number by removing 'k' digits while maintaining the order of the existing digits
Input = 3194
k = 2

output 14
"""

import collections
import heapq


def smallestNum(num, k):
    nums = collections.deque()
    tmp = num
    while tmp != 0:
        tmp, div = divmod(tmp, 10)
        nums.appendleft(div)

    i = 0
    windows, result = [], []
    windowSize = 0
    for j in range(len(nums)):
        heapq.heappush(windows, (nums[j], j))
        windowSize += 1
        if windowSize > k:
            minV, mini = heapq.heappop(windows)
            result.append(minV)
            if mini == i:
                i += 1
                windowSize -= 1
            else:
                while i < mini:
                    try:
                        # print(f"{nums}, i: {i}, mini: {mini}, j: {j}")
                        # print(windows)
                        # print(result)
                        windows.remove((nums[i], i))
                    except:
                        pass
                    i += 1
                    k -= 1
                    windowSize -= 1
                heapq.heapify(windows)

    return result

print(smallestNum(3462, 2))

print(smallestNum(34612, 2))

print(smallestNum(134612, 4))