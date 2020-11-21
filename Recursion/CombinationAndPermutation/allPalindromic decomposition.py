

def palindromeicDecomposition(word):

    if len(word) == 0:
        raise ValueError
    if len(word) ==1:
        return [word]
    result = []
    all= []
    _palindromeicDecomposition(word, result, all)

    return all

def _palindromeicDecomposition(word, result, all):
    if len(word) == 0:
        all.append(result[:])
        return
    #Missed len(knapsack) option: if you miised this optio, there i sno output
    if len(word) == 1:
        result.append(word)
        all.append(result[:])
        del result[len(result) -1]
        return

    for i in range(1, len(word)):
        i_word = word[:i]
        j_word = word[i:]
        if isPalindrome(i_word):
            result.append(i_word)
            _palindromeicDecomposition(j_word, result, all)
            del result[len(result) -1]


def isPalindrome(word):
    i, j  = 0, len(word) -1

    while i < j:
        if word[i].upper() != word[j].upper():
            return False
        i += 1
        j -= 1
    return True


import pprint

word= "0204451881"
pprint.pprint(palindromeicDecomposition(word))
