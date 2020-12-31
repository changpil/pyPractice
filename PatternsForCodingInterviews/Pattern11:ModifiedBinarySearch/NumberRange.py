# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’.
# The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
#
# Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

def find_range(arr, key):
    result = [- 1, -1]
    i, j = 0, len(arr) - 1

    while i <= j:
        mid = i + (j - i) // 2
        if arr[mid] > key:
            j = mid - 1
        elif arr[mid] < key:
            i = mid + 1
        else:
            start, end = mid, mid
            while start >= 0 and arr[start] == key:
                start -= 1
            while end < len(arr) and arr[end] == key:
                end += 1
            return [start +1, end-1]

    return result


def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))
  print(find_range([1, 1, 1, 3, 8, 10, 15], 1))
  print(find_range([1, 1, 1, 3, 8, 10, 15, 15, 15,15], 15))
  print(find_range([6, 6, 6, 6, 6], 6))
main()
