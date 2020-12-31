# Given a sorted array of numbers, find if a given number ‘key’ is present in the array.
# Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.
# You should assume that the array can have duplicates.

# Recursive Way
def binary_search_recursive(arr, key):
    ascending = False
    if arr[0] < arr[-1]:
        ascending = True
    return helper(arr, key, 0, len(arr)-1, ascending)

def helper(arr,  key, i, j, ascending):
    if i > j:
        return -1
    mid = (i + j)//2
    if key > arr[mid] and ascending:
        return helper(arr, key, mid +1, j, ascending)
    elif key >arr[mid] and not ascending:
        return helper(arr, key, i, mid -1, ascending)
    elif key < arr[mid] and ascending:
        return helper(arr, key, i, mid - 1, ascending)
    elif key < arr[mid] and not ascending:
        return helper(arr, key, mid+1, j, ascending)
    else:
        return mid

def binary_search(arr, key):
    ascending = False
    if arr[0] < arr[-1]:
        ascending = True
    i , j = 0, len(arr)-1
    while i <= j:
        mid = (i + j)//2
        if key > arr[mid] and ascending:
            i = mid + 1
        elif key > arr[mid] and not ascending:
            j = mid - 1
        elif key < arr[mid] and ascending:
            j = mid - 1
        elif key < arr[mid] and not ascending:
            i = mid + 1
        else:
            return mid
    return -1
def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search_recursive([4, 6, 10], 10))
  print()
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search_recursive([1, 2, 3, 4, 5, 6, 7], 5))
  print()
  print(binary_search([10, 6, 4], 10))
  print(binary_search_recursive([10, 6, 4], 10))
  print()
  print(binary_search([10, 6, 4], 4))
  print(binary_search_recursive([10, 6, 4], 4))


main()
