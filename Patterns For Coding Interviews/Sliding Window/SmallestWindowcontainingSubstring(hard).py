# Smallest Window containing Substring (hard) #
# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.
#
# Example 1:
#
# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"
# Example 2:
#
# Input: String="abdbca", Pattern="abc"
# Output: "bca"
# Explanation: The smallest substring having all characters of the pattern is "bca".
# Example 3:
#
# Input: String="adcad", Pattern="abc"
# Output: ""
# Explanation: No substring in the given string has all characters of the pattern.

def find_substring(str, pattern):
  s = set()
  for e in pattern:
    s.add(e)

  short = str + str
  for i in range(len(str)):
    tmp = pattern
    start = i

    while start < len(str) and tmp != "":
      if str[start] in s:
        index = tmp.find(str[start])
        tmp = tmp[:index] + tmp[index+1:]
      start += 1
    if tmp =="" and len(short) > start -i:
      short = str[i:start]
  if short == str + str:
    return ""
  return short

print(find_substring("aabdec", "abc"))
print(find_substring("abdabca", "abc"))
print(find_substring("adcad", "abc"))