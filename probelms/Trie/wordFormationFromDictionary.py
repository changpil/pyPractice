
from Trie.trie1 import Trie

# We perform the insert operation m times for a dictionary of size m. After that, the search operation runs on the word in the sequence:
# If the size of the word is n, the complexity for this turns out to be n2. Hence, the total time complexity is O(m + n2).

def is_formation_possible(dictionary, word):
    t = Trie()
    for w in dictionary:
        t.insert(w)

    for i in range(1, len(word)-1):
        if t.search(word[:i]) and t.search(word[i:]):
            return True
    return False

dictionary = ["the", "hello", "there", "answer", "any",
                     "by", "world", "their", "abc"]

print(is_formation_possible(dictionary, "helloworld"))

