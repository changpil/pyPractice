
from Trie.trie1 import Trie




# We first insert the nodes into the graph and then traverse all the existing nodes. Hence, the bottleneck worst case time complexity is O(n).
def sort_string(words):
    t = Trie()
    for w in words:
        t.insert(w)
    l = list()
    _find_words(t.root, '', l)
    return l

def _find_words(node, word, l):
    if node == None:
        return
    if node.is_end_word and node.has_no_children():
        l.append(word + node.char)
        return
    elif node.is_end_word and not node.has_no_children():
        l.append(word)

    for i in range(len(node.children)):
        if node.children[i] is not None:
            _find_words(node.children[i], word + node.char, l)

words = ["the", "a", "there", "answer", "any", "by", "bye", "their","abc"]
print(sort_string(words))