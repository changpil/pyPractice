"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""

# Requirement O(n^2)
# Key hint
# Type 1: aba
# Type 2: abba

# O(n^2)
def getMaxPalindrome(w, s, e):
    while 0 <= s and e < len(w) and w[s] == w[e]:
        s -= 1
        e += 1
    return (e-s- 1, s+1, e-1)

def longestPalindrome(w):
    maxpNumOfPlindrome, t1, t2  = (1, 0,0), (1, 0,0), (1, 0,0)
    for i in range(len(w)):
        t1 = getMaxPalindrome(w, i, i)
        if i+1 < len(w):
            t2 = getMaxPalindrome(w, i, i + 1)

        maxpNumOfPlindrome = max(maxpNumOfPlindrome, t1, t2)

    s = maxpNumOfPlindrome[1]
    e = maxpNumOfPlindrome[2]
    return w[s:e + 1]

# print(longestPalindrome("babad"))
# print(longestPalindrome("babab"))
# print(longestPalindrome("aabab"))

import timeit
w = "uhrfjotnewtodhmbplsaolnpcdaohiytmfllukijouxipvqohtsgxbtfoxyfkfczkfwhzimbefiohmtimrcxbpgcxogystdkcqujvbxsgirpccdnvejtljftwkdpsqpflzwruwwdzovsbmwbcvlftkjnxqaguvtsycylqzquqkbnybnbaeahbxejhphwrpmymcemuhljwtuvxefqfzjhskuqhifydkxpnfwfxkpeexnjltfqwfvchphmtsrsyayxukvmlqodshqwbeaxhcxdbssnrdzvxtusngwqdxvluauphmmbwmgtazjwvolenegwbmjfwprfuswamyvgrgshqocnhirgyakbkkggviorawadzhjipjjgiwpelwxvtaegauerbwpalofrbghfhnublttqtcmqskcocwwwxpnckrnbepusjyohsrretrqyvgnbezuvwmzizcefxyumtdwnqjkgsktyuacfpnqocqjxcurmipjfqmjqrkdeqsfseyigqlwmzgqhivbqalcxhlzgtsfjbdbfqiedogrqasgmimifdexbjjpfusxsypxobxjtcwxnkpgkdpgskgkvezkriixpxkkattyplnpdbdifforxozfngmlgcunbnubzamgkkfbswuqfqrvzjqmlfqxeqpjaqayodtetsecmfbplscmslpqiyhhykftzkkhshxqvdwmwowokpluwyvavwvofwqtdilwqjgrprukzyhckuspyzaoe"
start = timeit.timeit()
print(longestPalindrome(w))
end = timeit.timeit()
print(end - start)

print("DP approach")
# Dynamic Approach O(n^2)
# If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.

# We define F(i, j) = True, if Substring Si .... Sj is a Palrindrome
#                     False, Otherwise
#
# Therefore, F(i, j) = F(i-1, j+1) and Si == Sj

# It is o(n^2) but Expand Around Center seems better solution.
# Becasue it got time out
def longestPalindrome_dp(s):
    dp = [[True]*(len(s) +1) for _ in range(len(s) + 1)]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 or j == 0 :
                dp[i][j] = True
            if i >= j:
                dp[i][j] = True

    for j in range(1, len(dp[0])):
        for i in range(0, j):
            if s[i-1] == s[j-1]:
                if dp[i+1][j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
            else:
                dp[i][j] = False

    maxd = (0, 0, 0)

    #for l in dp:
    #    print(l)
    for j in range(1, len(dp[0])):
        for i in range(1, j):
            if dp[i][j] == True and maxd[0] < j - i:
                maxd = (j-i, i-1, j-1)
    return s[maxd[1] : maxd[2] +1]


# print(longestPalindrome_dp("babad"))
# print(longestPalindrome_dp("babab"))
# print(longestPalindrome_dp("aabab"))
# print(longestPalindrome_dp("cbbd"))
# print(longestPalindrome_dp("bb"))
# print(longestPalindrome_dp("a"))

# This had timeout
w = "uhrfjotnewtodhmbplsaolnpcdaohiytmfllukijouxipvqohtsgxbtfoxyfkfczkfwhzimbefiohmtimrcxbpgcxogystdkcqujvbxsgirpccdnvejtljftwkdpsqpflzwruwwdzovsbmwbcvlftkjnxqaguvtsycylqzquqkbnybnbaeahbxejhphwrpmymcemuhljwtuvxefqfzjhskuqhifydkxpnfwfxkpeexnjltfqwfvchphmtsrsyayxukvmlqodshqwbeaxhcxdbssnrdzvxtusngwqdxvluauphmmbwmgtazjwvolenegwbmjfwprfuswamyvgrgshqocnhirgyakbkkggviorawadzhjipjjgiwpelwxvtaegauerbwpalofrbghfhnublttqtcmqskcocwwwxpnckrnbepusjyohsrretrqyvgnbezuvwmzizcefxyumtdwnqjkgsktyuacfpnqocqjxcurmipjfqmjqrkdeqsfseyigqlwmzgqhivbqalcxhlzgtsfjbdbfqiedogrqasgmimifdexbjjpfusxsypxobxjtcwxnkpgkdpgskgkvezkriixpxkkattyplnpdbdifforxozfngmlgcunbnubzamgkkfbswuqfqrvzjqmlfqxeqpjaqayodtetsecmfbplscmslpqiyhhykftzkkhshxqvdwmwowokpluwyvavwvofwqtdilwqjgrprukzyhckuspyzaoe"
start = timeit.timeit()
print(longestPalindrome(w))
end = timeit.timeit()
print(end - start)