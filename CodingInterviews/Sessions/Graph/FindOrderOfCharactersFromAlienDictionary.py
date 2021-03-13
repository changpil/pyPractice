# Find Order Of Characters From Alien Dictionary
# Given a sorted dictionary of an alien language, find the order of characters in the alphabet.
# Example One
#
# Input: ["baa", "abcd", "abca", "cab", "cad"]
# Output: "bdac"
# Example Two
# Input: words = ["caa", "aaa", "aab"]
# Output: "cab"

# First try : solved
# def build_graph(words):
#     graph = {}
#     for word in words:
#         for c in word:
#             if c not in graph:
#                 graph[c] = []
#     for i in range(len(words) -1):
#         j = 0
#         char_len = min(len(words[i]), len(words[i+1]))
#         while j < char_len and words[i][j] == words[i+1][j]:
#             j += 1
#         if j != char_len:
#             graph[words[i][j]].append(words[i+1][j])
#     return graph
#
# # No cycle because it is lexicograpical order
# def find_order(words):
#     graph = build_graph(words)
#
#     visited = set()
#     stack = []
#     for v in graph:
#         if v not in visited:
#             topologicalSort(graph, v, visited, stack)
#
#     i = 0
#     while i < len(stack)//2:
#         stack[i] , stack[len(stack)-i-1] = stack[len(stack)-i-1], stack[i]
#         i += 1
#     return "".join(stack)
#
# def topologicalSort(graph, node, visited, stack):
#     visited.add(node)
#     for v in graph[node]:
#         if v not in visited:
#             topologicalSort(graph, v, visited, stack)
#     stack.append(node)

words = ["baa", "abcd", "abca", "cab", "cad"]

import collections

def getSrcDst(w1, w2):
    for i in range(min(len(w1), len(w2))):
        if w1[i] != w2[i]:
            return w1[i], w2[i]
    return None, None

def build_graph(words):
    vertices = set()
    for w in words:
        for c in w:
            vertices.add(c)
    graph = collections.defaultdict(set)
    for v in vertices:
        graph[v] = set()
    for i in range(1, len(words)):
        src, dst = getSrcDst(words[i - 1], words[i])
        if src and dst:
            graph[src].add(dst)
    return graph

def find_order(words):
    graph = build_graph(words)
    ingress = {}
    for src, dsts in graph.items():
        for dst in dsts:
            ingress[dst] = ingress.get(dst, 0) + 1

    #print(graph)
    #return
    visited = set()
    topsort = collections.deque()
    for c in graph:
        if c not in ingress:
            visited.clear()
            topsort.clear()
            bfs(graph, c, visited, topsort)
            if len(topsort) == len(graph):
                return "".join(list(topsort))
    return ""

def bfs(graph, c, visited, topsort):
    visited.add(c)

    for n in graph[c]:
        if n not in visited:
            bfs(graph, n, visited, topsort)
    topsort.appendleft(c)

words = ['g','g','g','g']
words = ['zy', 'zx']
words = ['ab', 'abc']
print(find_order(words))