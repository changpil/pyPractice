# Problem Statement #
# Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

# Example 1:
#
# Input: nums=[1, 2, -1, 3, 5], k = 2
# Output: [1.5, 0.5, 1.0, 4.0]
# Explanation: Lets consider all windows of size ‘2’:
#
# [1, 2, -1, 3, 5] -> median is 1.5
# [1, 2, -1, 3, 5] -> median is 0.5
# [1, 2, -1, 3, 5] -> median is 1.0
# [1, 2, -1, 3, 5] -> median is 4.0
# Example 2:
#
# Input: nums=[1, 2, -1, 3, 5], k = 3
# Output: [1.0, 2.0, 3.0]
# Explanation: Lets consider all windows of size ‘3’:
#
# [1, 2, -1, 3, 5] -> median is 1.0
# [1, 2, -1, 3, 5] -> median is 2.0
# [1, 2, -1, 3, 5] -> median is 3.0


from heapq import *

class SlidingWindowMedian:

    def find_sliding_window_median(self, nums, k):
        result = []
        i = k - 1
        maxHeap, minHeap = self.getHeaps(nums, k)

        while i < len(nums):
            # print(i)
            # print(maxHeap)
            # print(minHeap)
            if len(maxHeap) == len(minHeap):
                result.append((-maxHeap[0] + minHeap[0])/2)
            else:
                result.append(-maxHeap[0])
            i += 1
            if i < len(nums):
                self.shiftWindow(maxHeap, minHeap, nums[i], nums[i-k])

        return result

    def reBalanching(self, maxHeap, minHeap):
        while len(maxHeap) < len(minHeap):
            heappush(maxHeap, -heappop(minHeap))
        while len(maxHeap) > len(minHeap) + 1:
            heappush(minHeap, -heappop(maxHeap))


    def shiftWindow(self, maxHeap, minHeap, new_num, out_num):
        # Max first
        if maxHeap and -maxHeap[0] > new_num:
            maxHeap.append(-new_num)
        else:
            minHeap.append(new_num)
        if -out_num in maxHeap:
            maxHeap.remove(-out_num)
        elif out_num in minHeap:
            minHeap.remove(out_num)
        self.reBalanching(maxHeap, minHeap)

    def getHeaps(self, nums, k):
        minHeap = []
        maxHeap = []

        for i in range(k):
            #maxHeap first
            if maxHeap and -maxHeap[0] > nums[i]:
                maxHeap.append(-nums[i])
            else:
                minHeap.append(nums[i])
            self.reBalanching(maxHeap, minHeap)
        return maxHeap, minHeap


def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()

