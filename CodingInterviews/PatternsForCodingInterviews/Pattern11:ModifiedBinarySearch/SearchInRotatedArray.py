# Educative solution

def search_rotated_with_duplicates(arr, key):
    i, j = 0, len(arr) - 1
    while i <= j:
        mid = i + (j - i) // 2
        if arr[mid] == key:
            return mid

        if arr[i] < arr[mid]:
            # Sorted i to mid
            if arr[i] <= key < arr[mid]:
                j = mid - 1
            else:
                i = mid + 1
        elif arr[mid] < arr[j]:
            # sorted mid to j
            if arr[mid] < key <= arr[j]:
                i = mid + 1
            else:
                j = mid - 1
        else:
            if arr[i] == arr[mid]:
                i = i + 1
            if arr[mid] == arr[j]:
                j = j-1
    return -1




def main():
    print(search_rotated_with_duplicates([10, 15, 1, 3, 8], 15))
    print(search_rotated_with_duplicates([4, 5, 7, 9, 10, -1, 2], 10))
    print(search_rotated_with_duplicates([10, 10, 10, 10, 10, 10 - 1, 2], 10))
    print(search_rotated_with_duplicates([4, 5, 7, 9, 10, 10, 10, 10, 10, 10 - 1, 2], 10))
    print(search_rotated_with_duplicates([-1, 2, 2, 2, 3, 3, 3, 3], 3))

    print(search_rotated_with_duplicates([3, 7, 3, 3, 3], 7))
    print(search_rotated_with_duplicates([4,5,6,6,6,2], 2))

main()
