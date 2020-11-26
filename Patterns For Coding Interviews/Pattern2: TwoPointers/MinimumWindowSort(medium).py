# Minimum Window Sort (medium) #
# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
#
# Example 1:
#
# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
# Example 2:
#
# Input: [1, 3, 2, 0, -1, 7, 10]
# Output: 5
# Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
# Example 3:
#
# Input: [1, 2, 3]
# Output: 0
# Explanation: The array is already sorted
# Example 4:
#
# Input: [3, 2, 1]
# Output: 3
# Explanation: The whole array needs to be sorted.

def shortest_window_sort(arr):
    start , end = -1,-1
    i, j =0,0

    while i < len(arr) -1:
        j = i + 1
        while j <len(arr) and arr[i] < arr[j]:
            j += 1
        if j != len(arr):
            if start == -1:
                start = i
            end = j
            #i = j -1
        i +=1
    return arr[start:end+1]

print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
print(shortest_window_sort([1, 2, 3]))
print(shortest_window_sort([ 3,2,1]))

