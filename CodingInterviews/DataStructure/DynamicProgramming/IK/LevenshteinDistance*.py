# Levenshtein Distance
# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
# a) Insert a character
# b) Delete a character
# c) Replace a character
# The minimum number of steps required to convert word1 to word2 with the given set of allowed operations is called edit distance.
# e.g. Minimum edit distance between the words 'kitten' and 'sitting', is 3.
# kitten → sitten (substitution of "s" for "k")
# sitten → sittin (substitution of "i" for "e")
# sittin → sitting (insertion of "g" at the end)
# Read more about edit distance here:

# 1. My recursive formula
# if s1[i] != s2[j]:
#    f(i,j) = min(f(i-1, j), f(i, j-1), f(i-1, j-1)) +1
# if s1[i] == s2[j] :
#    f{(i,j) = f(i-1, j-1)

# 2. DP range DP[len(s1)+1][len(s2) +1]
# 3. My direction DP[0][0] ==> DP[len(s1)][len(s2]

# def  levenshteinDistance(strWord1, strWord2):
#     DP = [ [0]*(len(strWord2) + 1) for _ in range(len(strWord1) + 1)]
#     for j in range(len(DP[0])):
#         DP[0][j]= j
#
#     for i in range(len(DP)):
#         DP[i][0] = i
#
#     for i in range(1, len(DP)):
#         for j in range(1, len(DP[0])):
#             if strWord1[i-1] == strWord2[j-1]:
#                 DP[i][j] = DP[i-1][j-1]
#             else:
#                 DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) +1
#
#     return DP[-1][-1]




def levenshteinDistance(strWord1, strWord2):
    len1, len2 = len(strWord1), len(strWord2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        dp[i][0] = i

    for i in range(len2+1):
        dp[0][i] = i

    for a in dp:
        print(a)
    for i in range(1, len1):
        for j in range(1, len2):
            if strWord1[i - 1] == strWord2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
    return dp[-1][-1]

print(levenshteinDistance("bat", "cat"))