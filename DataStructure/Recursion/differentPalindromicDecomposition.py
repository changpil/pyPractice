def generate_palindromic_decompositions(s):
    collection = list()
    helper(s, 0, collection, "")
    return collection


def isPalindrom(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def helper(s, start, collection, tmp):
    if start > len(s):
        return
    if start == len(s):
        collection.append(tmp[1:])
        return

    for i in range(start + 1, len(s)):
        if isPalindrom(s[start:i+1]):
            helper(s, i + 1, collection, tmp + "|" + s[start:i + 1] )
    helper(s, start +1 ,collection, tmp + "|" + s[start] )

import pprint
pprint.pprint(generate_palindromic_decompositions("abracadabra"))