# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
#
# Example Pattern1:knapsack:
#
# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:
#
# Input: String="abbcb", k=Pattern1:knapsack
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:
#
# Input: String="abccde", k=Pattern1:knapsack
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".


# Brte Force O(n^2)

# Sliding Windows

def isAllowed(d, k):
    # Dug was len(d) >k: I did not include majority char.
    if len(d) > k + 1 :
        return False
    if len(d) <= 1:
        return True

    count = list(d.values())
    count.sort()

    allowance = k
    for i in range(len(d)-1):
        if i < len(count):
            allowance -= count[i]
    if allowance >= 0:
        return True
    return False

def longestSubstring(chars, k):
    d = dict()
    start, noc = 0, 0
    for end in range(len(chars)):
        d[chars[end]] = d.get(chars[end], 0) + 1
        while not isAllowed(d, k):
            d[chars[start]] = d[chars[start]] -1
            if d[chars[start]] == 0:
                del d[chars[start]]
            start += 1
        noc = max(noc , end - start + 1)
    return noc

print(longestSubstring("aabccbb", 2))
print(longestSubstring("abbcb", 1))
print(longestSubstring("abccde", 1))