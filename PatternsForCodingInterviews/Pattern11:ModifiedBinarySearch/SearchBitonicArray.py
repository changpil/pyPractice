def max_index(arr):
    i , j = 0, len(arr) -1

    while i < j:
        mid = i + (j-i)//2
        if arr[mid] < arr[mid +1]:
            i = mid + 1
        else:
            j = mid
    return i

def binary_search(arr, key, i, j):
    while i <= j:
        mid = i +(j-i)//2
        if key == arr[mid]:
            return mid

        if arr[i] < arr[j]:
            if arr[mid] > key:
                j = mid - 1
            else:
                i = mid + 1
        else:
            if arr[mid] > key:
                i = mid + 1
            else:
                j = mid - 1

    return -1

def search_bitonic_array(arr, key):
    m_index = max_index(arr)
    #print(m_index)
    if m_index == 0 or m_index == len(arr) -1:
        return binary_search(arr, key, 0, len(arr)-1)
    else:
        ascending = binary_search(arr, key, 0, m_index)
        if ascending != -1:
            return ascending
        return binary_search(arr, key, m_index, len(arr) -1)



def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))

main()