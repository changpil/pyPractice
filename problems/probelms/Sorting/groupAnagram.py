"""
Write a method to sort an array of strings so that all the anagrams are next to each other
"""


def isAnagram(s1, s2):
    data = [0]*125
    for i in s1:
        i = i.lower()
        data[ord(i)] = data[ord(i)] + 1

    for i in s2:
        data[ord(i)] = data[ord(i)] - 1

    for i in data:
        if i != 0:
            return False
    return True


def groupAnagram(l):
    i = 0
    while i < len(l):
        j = i + 1
        while j < len(l):
            if isAnagram(l[i], l[j]):
                temp = l[j]
                del l[j]
                l.insert(i,temp)
                i += 1
            j += 1
        i += 1


l =["as", "dd", "ssa", "asas","sas", 'ddd', "asas"]

groupAnagram(l)
print(l)
