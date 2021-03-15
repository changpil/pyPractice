def firstBadVersion(n):
    start, end = 1, n

    while start <= end:
        mid = (start + end) // 2
        res = None # isBadVersion(mid)
        if res:
            end = mid - 1
        else:
            start = mid + 1

    return start