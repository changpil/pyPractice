# Longest Substring with K Distinct Characters (medium)
# Problem Statement #
# Given a string, find the length of the longest substring in it with no more than K distinct characters.
#
# Example Pattern1:knapsack:
#
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# Example 2:
#
# Input: String="araaci", K=Pattern1:knapsack
# Output: 2
# Explanation: The longest substring with no more than 'Pattern1:knapsack' distinct characters is "aa".
# Example 3:
#
# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".


def loingestcharsWithK(chars, k):
    s = set()
    start, noc = 0, 0

    for end in range(len(chars)):
        if chars[end] not in s:
            s.add(chars[end])

        if len(s) > k:
            leading_ch = chars[start]
            s.remove(chars[start])
            while chars[start] == leading_ch:
                start += 1

        noc = max(noc, end-start + 1)
    return noc

print(loingestcharsWithK("araaci", 2))
print(loingestcharsWithK("aaaraaci", 2))
print(loingestcharsWithK("araaci", 1))