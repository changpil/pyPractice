def merge_sort(arr):
    # Write your code here
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    left = arr[:m]
    right = arr[m:]

    merge_sort(left)
    merge_sort(right)

    return merge(left, right)


def merge(left, right):
    re = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            re.append(left[i])
            i += 1
        else:
            re.append(right[j])
            j += 1

    while i < len(left):
        re.append(left[i])
        i += 1

    while j < len(right):
        re.append(right[j])
        j += 1

    return re

l = [0,1,3,2]

print(merge_sort(l))