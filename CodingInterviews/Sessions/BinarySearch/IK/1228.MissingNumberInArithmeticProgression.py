def missingNumber(arr):

    # a, a+d, a+2d, a+3d, a+4d
    a = arr[0]
    gap = (arr[-1] - arr[0]) // len(arr)

    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        # This is not working for decreasing Arithmetic progession.
        # if arr[mid] <= a + mid*gap:
        if arr[mid] == a + mid * gap:
            start = mid + 1
        else:
            end = mid - 1

    return arr[end] + gap