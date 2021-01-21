# String Anagrams (hard) #
# Given a string and a pattern, find all anagrams of the pattern in the given string.
#
# Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:
#
# abc
# acb
# bac
# bca
# cab
# cba
# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.
#
# Example 1:
#
# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
# Example 2:
#
# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

def find_string_anagrams(str, pattern):
  result_indexes = []
  s = dict()
  for e in pattern:
    s[e] = s.get(e, 0) + 1

  for i in range(len(str)):
    start = i
    d = dict()
    while start < len(str) and str[start] in s and start -i < len (pattern):
      d[str[start]] = d.get(str[start], 0) + 1
      start += 1
    print(f"{s} {d}")
    if s == d :
      result_indexes.append(i)
  return result_indexes

print(find_string_anagrams("ppqp", "pq"))
print(find_string_anagrams("abbcabc", "abc"))