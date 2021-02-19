# Cycle in a Circular Array (hard) #
# We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:
#
# If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
# If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
# Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.
#
# Example 1:
#
# Input: [1, 2, -1, 2, 2]
# Output: true
# Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0
# Example 2:
#
# Input: [2, 2, -1, 2]
# Output: true
# Explanation: The array has a cycle among indices: 1 -> 3 -> 1
# Example 3:
#
# Input: [2, 1, -1, -2]
# Output: false
# Explanation: The array does not have any cycle.


def next(arr, index):
     return abs(index + arr[index]) % len(arr)

def circular_array_loop_exists(arr):
    slow, fast = 0, 0
    while True:
        slow = next(arr,slow)
        fast = next(arr, next(arr,slow))
        if slow == next(arr, slow):
            return False

        if next(arr,slow) == next(arr, next(arr, fast)):
            return False

        if slow == fast:
            return True

def main():
  print(circular_array_loop_exists([1, 2, -1, 2, 2]))
  print(circular_array_loop_exists([2, 2, -1, 2]))
  print(circular_array_loop_exists([2, 1, -1, -2]))


main()