# Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given ‘key’ is present in it.
#
# Write a function to return the index of the ‘key’ in the rotated array.
# If the ‘key’ is not present, return -1. You can assume that the given array does not have any duplicates.

# Mysolution O(logN) with working with duplicated items
def getFirstIndex(arr):
    i, j = 0 , len(arr) -1
    while i < j:
        mid = i + (j-i)//2
        if arr[mid] < arr[j]:
            j = mid
        else:
            i = mid + 1
    return i


def binarySearch(arr, key, i, j):

    while i <= j:
        mid = i + (j-i)//2

        if arr[mid] == key:
            return mid
        if key < arr[mid]:
            j = mid -1
        else:
            i = mid + 1
    return -1

def search_rotated_array(arr, key):
    m = getFirstIndex(arr)

    r1 = binarySearch(arr, key, 0, m-1)
    if r1 != -1:
        return r1
    return binarySearch(arr, key, m, len(arr)-1)

def main():
  # print(getFirstIndex([10, 15, 1, 3, 8]))
  # print(getFirstIndex([4, 5, 7, 9, 10, -1, 2]))
  # print(getFirstIndex([4, 5, 7, 9, 10]))
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))

    print(search_rotated_array([10, 10, 10, 10, 10, 10 - 1, 2], 10))
    print(search_rotated_array([4, 5, 7, 9, 10, 10, 10, 10, 10, 10 - 1, 2], 10))
    print(search_rotated_array([-1, 2, 2, 2, 3, 3, 3, 3], 3))

    print(search_rotated_array([3, 7, 3, 3, 3], 7))
    print(search_rotated_array([4, 5, 6, 6, 6, 2], 2))
main()