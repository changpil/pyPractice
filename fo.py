def numPhoneNumbers(startdigit, phonenumberlength):
    map = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 9], 7: [2, 6], 8: [1, 3],
           9: [4, 2]}
    dp = [[] for _ in range(phonenumberlength + 1)]
    dp[1].append(startdigit)

    for i in range(2, phonenumberlength + 1):
        #tmp = dp[i-1].copy()
        for n in dp[i-1]:
            dp[i].extend(map[n])
    for a in dp:
        print(a)
    return len(dp[-1])

#print(numPhoneNumbers(1, 2))


def numberOfWays(arr, k):
    arr.sort()
    i, j = 0, len(arr) - 1
    out = 0
    while j >= 0:
        cur = arr[j]
        target = k - cur
        i = 0
        while i < j:
            if arr[i] == target:
                out += 1
            elif arr[i] > target:
                break
            i += 1
        j -= 1
    return out

k_1 = 6
arr_1 = [1, 2, 3, 4, 3]
expected_1 = 2
output_1 = numberOfWays(arr_1, k_1)
print(expected_1, output_1)