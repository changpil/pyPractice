"""
Given an array, return another array with just the ordered unique elements from the given array. In other words, you're removing any duplicates.

Note: Order needs to be preserved, so no sorting should be done. And the order should be maintained with the first occurrence of the element in the given array.


JAVASCRIPT
function uniques(arr) {
  // fill in
}

let arr = [3, 5, 6, 9, 9, 4, 3, 12]
uniques(arr);
// Correct: [3, 5, 6, 9, 4, 12]
// But this is incorrect: [5, 6, 9, 4, 3, 12]

arr = [13, 5, 3, 5, 8, 13, 14, 5, 9]
uniques(arr);
// Correct: [13, 5, 3, 8, 14, 9]
// Incorrect: [3, 5, 8, 13, 14, 9]
Constraints
Length of the array <= 100000
The values in the array between -1000000000 and 1000000000
Expected time complexity: O(n)
Expected space complexity: O(n)
"""

def uniques(arr):
    visited = set()
    i = 0
    lasti = -1
    while i < len(arr):
        if arr[i] not in visited:
            visited.add(arr[i])
            lasti += 1
            arr[i], arr[lasti] = arr[lasti], arr[i]

        i += 1
    return arr[:lasti+1]

print(uniques([8,8,15,6,19,7,12,6,6,3,13,9,15,14,1,13,4,11,16]))