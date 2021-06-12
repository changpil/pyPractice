"""
Assume we're given an unsorted array of numbers such as this:

[ 2, 5, 1, 4, 9, 6, 3, 7 ]

We are told that when this array is sorted, there is a series of n consecutive numbers. You are given a lower bound and an upper bound for this sequence.

There is one consecutive number missing, and we need to find it.

As an example, look at the below example. We're told that the lower bound is 1 and the upper bound is 9. The number that's missing in the unsorted series bounded by these two number is 8.

JAVASCRIPT
const arr = [ 2, 5, 1, 4, 9, 6, 3, 7 ];
const lowerBound = 1;
const upperBound = 9;

missingInUnsorted(arr, lowerBound, upperBound);
// 8
Here's the challenge-- can you find the missing number in O(n) time? Can you do it without sorting?

Constraints
Length of the array <= 10000
The upper bound <= 10000
The lower bound >= -10000
Expected time complexity : O(n)
Expected space complexity : O(1)
"""

def missing_in_unsorted(arr, lowerBound, upperBound):
    i = 0
    while i < len(arr):
      while arr[i] - lowerBound < len(arr) and arr[arr[i] - lowerBound] != lowerBound + i:
        ii = arr[i] - lowerBound
        arr[i], arr[ii] = arr[ii], arr[i]
      i += 1
    i = 0
    print(arr)
    while i < len(arr):
      if arr[i] != lowerBound + i:
        return lowerBound + i
      i += 1
    return len(arr)

print(missing_in_unsorted([ 2, 5, 1, 4, 9, 6, 3, 7 ], 1, 9))