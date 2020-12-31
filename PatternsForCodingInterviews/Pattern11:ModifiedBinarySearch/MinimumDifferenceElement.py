# Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’.


def search_min_diff_element(arr, key):
    i, j = 0, len(arr) -1

    while i <= j:
        mid = i + (j-i)//2

        if arr[mid] > key:
            j = mid -1
        elif arr[mid] < key:
            i = mid +1
        else:
            return arr[mid]
    if j ==-1:
        return arr[0]
    if i  == len(arr):
        return arr[-1]
    if abs(key - arr[i]) < abs(key- arr[j]):
        return arr[i]
    return arr[j]



def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()