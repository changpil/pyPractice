"""
The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your set of integers in non-decreasing order, then:

If your set contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted set ,  is the median.
If your set contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted set ,  is the median.
Given an input stream of  integers, perform the following task for each  integer:

Add the  integer to a running list of integers.
Find the median of the updated list (i.e., for the first element through the  element).
Print the updated median on a new line. The printed value must be a double-precision number scaled to  decimal place (i.e.,  format).
Example

Sorted          Median
[7]             7.0
[3, 7]          5.0
[3, 5, 7]       5.0
[2, 3, 5, 7]    4.0
Each of the median values is stored in an array and the array is returned for the main function to print.

Note: Add formatting to the print statement.

Function Description
Complete the runningMedian function in the editor below.

runningMedian has the following parameters:
- int a[n]: an array of integers

Returns
- float[n]: the median of the array after each insertion, modify the print statement in main to get proper formatting.

Input Format

The first line contains a single integer, , the number of integers in the data stream.
Each line  of the  subsequent lines contains an integer, , to be inserted into the list.
"""

from heapq import *
def runningMedian(a):
    maxheap, minheap = [], []
    results = []
    for i in range(0, len(a)):
        if len(maxheap) == 0 or  -maxheap[0] < a[i]:
            heappush(minheap, a[i])
        else:
            heappush(maxheap, -a[i])

        while abs(len(maxheap)-len(minheap)) >= 2:
            if len(maxheap) > len(minheap):
                heappush(minheap, -heappop(maxheap))
            else:
                heappush(maxheap, -heappop(minheap))

        if len(maxheap) == len(minheap):
            results.append((-maxheap[0] + minheap[0])/2)
        else:
            if len(maxheap) > len(minheap):
                results.append(-maxheap[0])
            else:
                results.append(minheap[0])
    return results
nums = [3,2,6,9,10]
print(runningMedian(nums))