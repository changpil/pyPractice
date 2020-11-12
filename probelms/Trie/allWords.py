from Trie.trie1 import Trie


# As the algorithm traverses all the nodes, its run time is O(n) where n is the number of nodes in the trie.
def find_words(root):
    if root == None:
        return
    l = list()
    _find_words(root, "", l)
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


# t = Trie()
# t.insert("abc")
# t.insert("there")
# t.insert("their")
# t.insert("top")
# print(t)
#
# print(find_words(t.root))

