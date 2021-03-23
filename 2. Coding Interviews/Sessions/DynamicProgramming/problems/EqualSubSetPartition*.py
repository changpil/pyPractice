# Equal Sub Set Partition
#
# Given an array s of n integers, partition it into two non-empty subsets, s1 and s2, such that the sum of all elements in s1 is equal to the sum of all elements in s2. Return a boolean array of size n where i-th element is True if i-th element of s belongs to s1 and False if it belongs to s2. Any valid answer will be accepted. If such partitioning is not possible, return an empty array.
#
# Example
# Input: n = 6, s = [10, -3, 7, 2, 1, 3]
# Output: [True, True, False, False, False, True]
#
# There are multiple partitionings where s1 sums up to 10 and s2 sums up to 10; they are all correct answers:
# s1 = [ 10 , -3 , 3 ] and s2 = [ 7 , 2 , 1 ] (Sample output)
# s1 = [ 7 , 2 , 1 ] and s2 = [ 10 , -3 , 3 ]
# s1 = [10] and s2 = [-3, 3, 7, 2, 1]
# s1 = [-3, 3, 7, 2, 1] and s2 = [10]
# s1 = [10, -3, 2, 1] and s2 = [7, 3]
# s1 = [7, 3] and s2 = [10, -3, 2, 1]


# def equalSubSetSumPartition(s):
#     group1, group2 = [], []
#     cache = []
#     r = helper(s, 0, group1, group2, cache)
#     return cache
#
# def helper(s, i, group1, group2, cache):
#     if i == len(s):
#         if sum(group1) == sum(group2):
#             cache.append(set(group1))
#             cache.append(set(group2))
#             return True
#         else:
#             return False
#     group1.append(s[i])
#     r1 = helper(s, i + 1, group1, group2, cache)
#     group1.pop()
#     if r1:
#         return True
#     group2.append(s[i])
#     r2 = helper(s, i + 1, group1, group2, cache)
#     group2.pop()
#     if r2:
#         return True
#     return False

# True/False DP Version
# def equalSubSetSumPartition(s):
#     halfsum = sum(s)//2
#     DP = [[False]*(halfsum +1) for _ in range(len(s) + 1)]
#     for i in range(len(DP)):
#         DP[i][0] = True
#
#     for i in range(1,halfsum + 1):
#         DP[0][i] = False
#
#     for i in range(1, len(DP)):
#         for j in range(1, halfsum + 1):
#             result = False
#             if 0<= j - s[i-1] < len(DP):
#                 result = DP[i-1][j - s[i-1]]
#             DP[i][j] = result or DP[i-1][j]
#     for i in range(len(DP)):
#        print(DP[i])
#     return DP[-1][-1]

#
# Output Format: If a valid partition exists, then the first line contains an integer s1, denoting the size of the first subset and next S1 line contains
# i-th elements in the set s1 in the order they appear in the input array s. Next line contains an integer s2, denoting the size of the second subset.
# Next s2 lines will contain integers denoting the ith element in the set s2 in the order they appear in the input array s.
# In case a valid partition is not possible the output contains only one line having integer -1.
# For the above-provided custom input, one possible custom output could be:
# 2
# 1
# -1
# 1
# 0

# def equalSubSetSumPartition(s):
#     if sum(s) %2 != 0:
#         return [-1]
#
#     halfsum = sum(s)//2
#     DP = [[False]*(halfsum +1) for _ in range(len(s) + 1)]
#
#     for i in range(len(DP)):
#         DP[i][0] = (True, [])
#
#     for i in range(1,halfsum + 1):
#         DP[0][i] = (False,[])
#
#     for i in range(1, len(DP)):
#         for j in range(1, halfsum + 1):
#             result = (False, [])
#             if 0 <= j - s[i-1] < len(DP):
#                 result = DP[i-1][j - s[i-1]]
#             if result[0]:
#                 newList = result[1][:]
#                 newList.append(i-1)
#                 DP[i][j] = (result[0], newList)
#             else:
#                 if DP[i - 1][j][0] == True:
#                     newList = DP[i - 1][j][1][:]
#                     DP[i][j] = (DP[i - 1][j][0], newList)
#                 else:
#                     DP[i][j] = result
#
#     if DP[-1][-1][0] == False:
#         return []
#     for line in DP:
#         print(line)
#     result = [False]*len(s)
#     for i in DP[-1][-1][1]:
#         result[i] = True
#     return result

def equalSubSetSumPartition(values):
    # Write your code here
    s = sum(values)
    if s % 2 != 0:
        return []
    halfsum = s // 2

    dp = [[False] * (abs(halfsum) + 1) for _ in range(len(values) + 1)]

    # With empty set, every sum should be False
    for col in range(len(dp[0])):
        dp[0][col] = False

    # With 0 sum, every set can be possible with {}
    for row in range(len(dp)):
        dp[row][0] = True

    for row in range(1, len(dp)):
        for col in range(1, len(dp[0])):
            dp[row][col] = dp[row - 1][col]
            if 0 <= col- values[row - 1] < len(dp[0]):
                dp[row][col] = dp[row-1][col] or dp[row-1][col- values[row - 1]]

    if dp[-1][-1] == False:
        return []
    rea = []
    col = len(dp[0]) -1
    row = len(dp) - 1


    # for row in dp:
    #    print(row)

    prevCol = 0
    if halfsum == 0:
        prevCol = 1
    for row in range(1, len(dp)):
        curCol = 0
        for col in range(1, len(dp[0])):
             if dp[row][col]:
                 curCol = col
        if curCol != prevCol:
            rea.append(True)
            prevCol = curCol
        else:
            rea.append(False)
    return rea
# Input: n = 6, s = [10, -3, 7, 2, 1, 3]
# Output: [True, True, False, False, False, True]
#
# s = [1,2, 3]
# print(equalSubSetSumPartition(s))
# s = [10, -3, 7, 2, 1, 3]
# print(equalSubSetSumPartition(s))
# s = [1, 2, 3, 5, 1]
# print(equalSubSetSumPartition(s))
# s = [100, 99,3 , 98, 1]
# print(equalSubSetSumPartition(s))
# s = [100, -100, 99, 99, 22, -22]
# print(equalSubSetSumPartition(s))
# -1
s = [1, -1]
print(equalSubSetSumPartition(s))

# -1
s = [1, 0, -1]
print(equalSubSetSumPartition(s))
# #
# #
#[True, False]
s = [0, 0]
print(equalSubSetSumPartition(s))
#[True, False, False, True, False]
s = [-1, -6, -3, -10, -2]
print(equalSubSetSumPartition(s))

s = [-6, 6, 13, -10, -3]
print(equalSubSetSumPartition(s))