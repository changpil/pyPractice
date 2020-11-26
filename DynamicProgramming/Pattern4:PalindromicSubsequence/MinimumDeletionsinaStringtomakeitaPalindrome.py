# Problem Statement #
# Given a string, find the minimum number of characters that we can remove to make it a palindrome.
#
# Example 1:
#
# Input: "abdbca"
# Output: 1
# Explanation: By removing "c", we get a palindrome "abdba".
# Example 2:
#
# Input: = "cddpd"
# Output: 2
# Explanation: Deleting "cp", we get a palindrome "ddd".
# Example 3:
#
# Input: = "pqr"
# Output: 2
# Explanation: We have to remove any two characters to get a palindrome, e.g. if we
# remove "pq", we get palindrome "r".

def minimumDeletionForPlindrome(st):
    return minimumDeletion(st, 0, len(st)-1)

def minimumDeletion(st, start, end):
    if start >= end:
        return 0

    r0, r1, r2 = len(st)-1, len(st)-1, len(st)-1

    if st[start] == st[end]:
        r0 = minimumDeletion(st, start+1, end -1)
    else:
        r1 = minimumDeletion(st,start, end-1)
        r2 = minimumDeletion(st,start+1, end)
        r1 += 1
        r2 += 1
    return min(r0, r1, r2)


print(minimumDeletionForPlindrome("abdbca"))
print(minimumDeletionForPlindrome("cddpd"))
print(minimumDeletionForPlindrome("pqr"))