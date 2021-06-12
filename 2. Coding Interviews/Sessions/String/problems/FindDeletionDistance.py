"""
Can you determine the deletion distance between two strings? Let's define the deletion distance as the numbers of characters needed to delete from two strings to make them equal.


For example, the deletion distance of algo and daily is 5. The reason is we can delete the go (2 deletion) in algo, and the d, i and y (3 deletions) in daily.

Constraints
Length of both the strings <= 1000
The strings can be empty
Take into consideration all the ASCII characters
Let m and n be the the lengths of string 1 and string 2
Expected time complexity O(m*n)
Expected space complexity : O(m*n)
"""

def deletionDistance(str1, str2):
    globaldup = 0
    globalindex = 0
    while globalindex < len(str1):
      i, ii = globalindex, 0
      localdup = 0
      while ii < len(str2):
          if str1[i] == str2[ii]:
              # Error I already added this in the last
              # ii += 1
              i += 1
              localdup += 1
          ii += 1
      globaldup = max(globaldup, localdup)
      globalindex += 1
    print(globaldup)
    return len(str1) -globaldup + len(str2) - globaldup

print(deletionDistance('algo', 'daily')) # 5
print(deletionDistance('some', 'thing')) # 9
print(deletionDistance('rag', 'flag')) # 3