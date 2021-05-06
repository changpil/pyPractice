#
# Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.
# You can assume that the array does not have any duplicates.


def count_rotations(arr):
    i , j = 0 , len(arr) -1

    while i < j:
        mid = i + (j - i) //2

        if arr[i] > arr[mid]:
            j = mid
        else:
            i = mid + 1
    return i%(len(arr) -1)


def main():
  print(count_rotations([10, 15, 1, 3, 8]))
  print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))


main()