"""
given you have isSubstring, Given two strings, s1, s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.

waterbottle is rotation of erbottlewat
"""
def isSubstring(a, suba):
    return True if a.count(suba) != 0 else False




def stringRotation(rotatedString, substring):
    string = rotatedString + rotatedString
    return isSubstring(string, substring)

a = "abcde"
b = "e"

print(stringRotation(a, b))