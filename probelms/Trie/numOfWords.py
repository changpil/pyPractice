from Trie.trie1 import Trie

# For a trie with n number of nodes, the algorithm runs in O(n) because each node has to be traversed
def total_words(node):
    if node == None:
        return 0
    total = 0
    for i in range(len(node.children)):
        if node.children[i] is not None:
            total += total_words(node.children[i])
    if node.is_end_word:
        total += 1
    return total

t = Trie()
t.insert("abc")
t.insert("there")
t.insert("their")
t.insert("top")
print(t)

print(total_words(t.root))


