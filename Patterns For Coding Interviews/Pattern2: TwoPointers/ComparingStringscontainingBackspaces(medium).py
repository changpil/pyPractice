# Comparing Strings containing Backspaces (medium) #
# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.
#
# Example 1:
#
# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
# Example 2:
#
# Input: str1="xy#z", str2="xyz#"
# Output: false
# Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
# Example 3:
#
# Input: str1="xp#", str2="xyz##"
# Output: true
# Explanation: After applying backspaces the strings become "x" and "x" respectively.
# In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
# Example 4:
#
# Input: str1="xywrrmp", str2="xywrrmu#p"
# Output: true
# Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.

def backspace_compare(str1, str2):
    count1, count2, i1, i2 = 0,0,len(str1)-1,len(str2) -1

    while i1 >= 0 and i2 >= 0:
        while str1[i1] == "#":
            count1 += 1
            i1 -= 1
        while str2[i2] == "#":
            count2 += 1
            i2 -= 1
        while count1 != 0:
            count1 -= 1
            i1 -= 1
        while count2 != 0:
            count2 -= 1
            i2 -= 1

        if str1[i1] != str2[i2]:
            return False
        i1 -= 1
        i2 -= 1
    if i1 != -1 or i2 != -1:
        return False
    return True

print(backspace_compare(str1="xy#z", str2="xzz#"))
print(backspace_compare(str1="xy#z", str2="xyz#"))
print(backspace_compare(str1="xp#", str2="xyz##"))
print(backspace_compare(str1="xywrrmp", str2="xywrrmu#p"))

