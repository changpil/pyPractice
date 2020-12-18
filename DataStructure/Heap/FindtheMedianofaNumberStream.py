# Problem Statement #
# Design a class to calculate the median of a number stream. The class should have the following two methods:
#
# insertNum(int num): stores the number in the class
# findMedian(): returns the median of all numbers inserted in the class
# If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

from heapq import *
class MedianOfAStream:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def insert_num(self, num):
        if self.minHeap and self.minHeap[0] > num:
            heappush(self.maxHeap, num*-1)
        else:
            heappush(self.minHeap, num)

        # Balance the minHeap and MaxHeap
        if len(self.minHeap) > len(self.maxHeap):
            n = heappop(self.minHeap)
            heappush(self.maxHeap, n*-1)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            n = heappop(self.maxHeap)
            heappush(self.minHeap, n *-1)


    def find_median(self):
        median = 0
        if len(self.minHeap) == len(self.maxHeap):
            median = (self.minHeap[0] + self.maxHeap[0]*-1)/2
        else:
            median = self.maxHeap[0]*-1

        return median


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()