"""
We're going to make our own Contacts application! The application must perform two types of operations:

add name, where  is a string denoting a contact name. This must store  as a new contact in the application.
find partial, where  is a string denoting a partial name to search the application for. It must count the number of contacts starting with  and print the count on a new line.
Given  sequential add and find operations, perform each operation in order.

Example
Operations are requested as follows:

add ed
add eddie
add edward
find ed
add edwina
find edw
find a
Three  operations include the names 'ed', 'eddie', and 'edward'. Next,  matches all  names. Note that it matches and counts the entire name 'ed'. Next, add 'edwina' and then find 'edw'.  names match: 'edward' and 'edwina'. In the final operation, there are  names that start with 'a'. Return the array .

Function Description

Complete the contacts function below.

contacts has the following parameters:

string queries[n]: the operations to perform
Returns

int[]: the results of each find operation
Input Format

The first line contains a single integer, , the number of operations to perform (the size of ).
Each of the following  lines contains a string, .

Constraints

 and  contain lowercase English letters only.
The input does not have any duplicate  for the  operation.
Sample Input

STDIN           Function
-----           --------
4               queries[] size n = 4
add hack        queries = ['add hack', 'add hackerrank', 'find hac', 'find hak']
add hackerrank
find hac
find hak
Sample Output

2
0
Explanation
"""

#Time Exceeded
# class Node:
#     def __init__(self):
#         self.ch = [None]*26
#         self.end = False
#
# class Trie:
#     def __init__(self):
#         self.root = Node()
#
#     def add(self, s):
#         _add(self.root, s, 0)
#
#     def find(self, s):
#         store = []
#         _find(self.root, s, 0, store)
#         return store
#
# def _add(node, s, i):
#     index = ord(s[i]) - ord('a')
#     if node.ch[index] == None:
#         node.ch[index] = Node()
#     if i == len(s)-1:
#         node.ch[index].end = True
#     else:
#         _add(node.ch[index],s , i + 1)
#
# def _find(node, s, i, store):
#     if len(s) == i:
#         _get(node, s, store)
#         return
#     index = ord(s[i]) - ord('a')
#     if node.ch[index] == None:
#         return
#     _find(node.ch[index],s , i +1, store )
#
# def _get (node, s, store):
#     if node.end:
#         store.append(s)
#     for i, n in enumerate(node.ch):
#         if n:
#             _get(n, s + chr(ord('a') + i), store )

import collections
class Node:
    def __init__(self):
        self.children = collections.defaultdict(lambda: Node())
        self.end = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()
        #self.visited = set()

    def add(self, s):
        self._add(self.root, s, 0)
        # if s not in self.visited:
        #     self.visited.add(s)
        #     self._add(self.root, s, 0)

    def _add(self, node, s, i):
        if s[i] not in node.children:
            node.children[s[i]] = Node()

        node.children[s[i]].count += 1
        if i < len(s) - 1  :
            self._add(node.children[s[i]], s, i + 1)
        else:
            node.children[s[i]].end =  True

    def find(self, s):
        return self._find(self.root, s, 0)

    def _find(self, node, s, i):
        if i == len(s):
            return node.count
        if s[i] in node.children:
            return self._find(node.children[s[i]],s, i + 1)
        return 0

    def findAllElements(self, s):
        store = []
        node = self._findAllElements(self.root, s, 0)
        if node:
            self.get(node, s, store)
        return store

    def _findAllElements(self, node, s, i):
        if i == len(s):
            return node
        if s[i] in node.children:
            return self._find(node.children[s[i]],s, i + 1)
    def get(self, node, s, store):
        if node.end == True:
            store.append(s)
        for ne in node.children:
            self.get(node.children[ne], s + ne, store )
# trie = Trie()
# trie.add("hack")
# trie.add("hackerrank")
# trie.add("hac")
# print(trie.find("ha"))
# store = []
# _get (trie.root, "", store)
# for s in store:
#     print(s)



def contacts(queries):
    trie = Trie()
    results = []
    for q in queries:
        a = q.split()
        if a[0] == 'add':
            trie.add(a[1])
        elif a[0] == 'find':
            results.append(trie.find(a[1]))
    store = []
    trie.get (trie.root, "", store)
    for s in store:
        print(s)
    return results


queries = ['add hack', 'add hackerrank', 'find hac', 'find hak', 'add hak', 'find h']
print(contacts(queries))
queries = ['add h', 'find h']
print(contacts(queries))