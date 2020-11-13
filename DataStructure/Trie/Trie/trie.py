class Node:
    def __init__(self):
        self.chars = dict()
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = Node()

    def has_more_words(self, node):
        return len(node.chars) != 0

    def insert(self, word):
        if word == None or len(word) == 0:
            return
        cur = self.root
        for c in word:
            if c not in cur.chars:
                cur.chars[c] = Node()
            cur = cur.chars[c]
        cur.isEndOfWord = True

    def search(self, word):
        if word == None or len(word) == 0:
            return
        cur = self.root
        for ch in word:
            if ch not in cur.chars:
                return False
            cur = cur.chars[ch]
        if not cur.isEndOfWord:
            return False
        return True

    def delete(self, word):
        if word == None or len(word) == 0:
            return
        self._delete(word, self.root, len(word) -1 , 0)

    def _delete(self, word, node, length, level):
        if node == None:
            print("Key does not exist")
            return False

        if level == length:
            if len(node.chars) == 1:
                del node.chars[word[level]]
                deleted_self = True
            else:
                node.isEndOfWord = False
                deleted_self = False
        else:
            child_node = node.chars[word[level]]
            child_deleted = self._delete(word, child_node, length, level + 1)
            if child_deleted:
                del node.chars[word[level]]
                if node.isEndOfWord:
                    deleted_self = False
                elif len(node.chars) != 0:
                    deleted_self = False
                else:
                    # node = None
                    deleted_self = True
            else:
                deleted_self = False
        return deleted_self

    def __str__(self):
        cur = self.root
        s = ""
        l = []
        for c in cur.chars:
            self.str_helper(c, cur.chars[c], l)
        return " ".join(l)

    def str_helper(self, chars,  node, l):
        if node.isEndOfWord and len(node.chars) == 0:
            l.append(chars)
            return
        elif node.isEndOfWord:
            l.append(chars)

        for c in node.chars:
            self.str_helper(chars + c, node.chars[c], l)




# t = Trie()
# t.insert("abc")
# t.insert("there")
# t.insert("their")
# t.insert("top")
# print(t)
#
# print("Search: top")
# print(t.search("top"))
# print("Search: the")
# print(t.search("the"))
# print("Search: there")
# print(t.search("there"))
# print("Search: thered")
# print(t.search("thered"))
#
# t.delete("their")
# t.delete("top")
# print(t)

