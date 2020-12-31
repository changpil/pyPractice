# Find the maximum value in a given Bitonic array.
# An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
# Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

# def find_max_in_bitonic_array(arr):
#     i , j = 0, len(arr) -1
#
#     while i <= j:
#         mid = i + (j-i)//2
#
#         if mid + 1 < len(arr) and arr[mid] < arr[mid +1]:
#             i = mid + 1
#         elif mid-1 >= 0 and arr[mid-1] > arr[mid]:
#             j = mid -1
#         else:
#             return arr[mid]
#     return -1

# Better way in solution
def find_max_in_bitonic_array(arr):
    i , j = 0, len(arr) -1

    while i < j:
        mid = i + (j-i)//2
        if arr[mid] < arr[mid +1]:
            i = mid + 1
        else:
            j = mid
    return i

def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))
  print(find_max_in_bitonic_array([9]))

main()
