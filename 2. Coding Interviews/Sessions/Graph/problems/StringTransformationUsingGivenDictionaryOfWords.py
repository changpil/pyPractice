# You need to find the shortest possible sequence of strings (two or more) such that:
#
# 1. First string is start.
# 2. Last string is stop.
# 3. Every string (except the first one) differs from the previous one by exactly one character.
# 4. Every string (except, possibly, first and last ones) are in the dictionary of words.
#
# Example One
# Input:
# words = ["cat", "hat", "bad", "had"]
# start = "bat"
# stop = "had"
#
# Output:
# ["bat", "bad", "had"]
# or
# ["bat", "hat", "had"]
#
# From "bat" change character 't' to 'd', so new string will be "bad".
# From "bad" change character 'b' to 'h', so new string will be "had".
# or
# From "bat" change character 'b' to 'h', so new string will be "hat".
# From "hat" change character 't' to 'd', so new string will be "had".

# This is easy to make errors, you need to practice
# Time exceeded


# First Implementation
# def isOneDifference(w1, w2):
#     diff = 0
#     for i in range(len(w1)):
#         if w1[i] != w2[i]:
#             diff += 1
#     if diff == 1:
#         return True
#     return False
#
# def get_oneDifferedWords(w, words):
#     neighbor_words = []
#     for word in words:
#         if isOneDifference(w, word) and word not in neighbor_words:
#             neighbor_words.append(word)
#     return neighbor_words
#
# def build_graph(words):
#     graph = dict()
#     for w in words:
#         graph[w] = get_oneDifferedWords(w, words)
#     return graph
#
# from collections import deque
# def bfs(words, start, stop):
#     if start not in words:
#         words.append(start)
#     if stop not in words:
#         words.append(stop)
#     graph = build_graph(words)
#     queue = deque()
#     visited = set()
#     parent = {}
#     queue.append(start)
#     if start != stop:
#         visited.add(start)
#     parent[start] = None
#     while queue:
#         node = queue.popleft()
#         for neb in graph[node]:
#             if neb not in visited:
#                 visited.add(neb)
#                 queue.append(neb)
#                 parent[neb] = node
#                 if neb == stop:
#                     return parent
#     return parent
#
# def string_transformation(words, start, stop):
#     if isOneDifference(start, stop):
#         return [start, stop]
#
#     parent = bfs(words, start, stop)
#     trace = deque()
#
#     # End is not found
#     if parent.get(stop, None) == None:
#         return ["-1"]
#
#     # found paths
#     back = stop
#     while back:
#         trace.appendleft(back)
#         if back == start == stop:
#             tmp = parent[back]
#             parent[back] = None
#             back = tmp
#         else:
#             back = parent[back]
#
#     return list(trace)

# words =  ["cat", "hat", "bad", "had"]
# print( string_transformation(words, "bat", "had"))
# words =  ["cccw", "accc", "accw"]
# print( string_transformation(words, "cccc", "cccc"))
#
# words =  []
# print( string_transformation(words, "zzz", "zzz"))
#
# words =  ["a","b","c",]
# print( string_transformation(words, "y", "z"))

def isOneCharDiffer(w1, w2):
    diffChars = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diffChars += 1
        if diffChars == 2:
            return False
    if diffChars == 0:
        return False
    return True

def getNext(words, word, visited):
    for w in words:
        if w not in visited and isOneCharDiffer(word, w) :
            yield w


# def string_transformation(words, start, stop):
#     paths = []
#     visited = set()
#     # Time Limit Excceded
#     #r = DFShelper(words, start, stop, paths, visited)
#     r = BFShelper(words, start, stop, paths, visited)
#     if not r:
#         return ["-1"]
#     return r
#
# def DFShelper(words, curr, stop, paths, visited):
#     paths.append(curr)
#     visited.add(curr)
#
#     if isOneCharDiffer(curr, stop):
#         paths.append(stop)
#         tr = paths.copy()
#         paths.pop()
#         paths.pop()
#         visited.discard(curr)
#         return tr
#
#     minPath = None
#     for nextWord in getNext(words, curr, visited):
#         r = DFShelper(words, nextWord, stop, paths, visited)
#         if minPath == None and r != None:
#             minPath = r
#         elif r != None and len(minPath) > len(r):
#             minPath = r
#
#     paths.pop()
#     visited.discard(curr)
#     return minPath
#
from collections import deque

def string_transformation(words, start, stop):
    visited = set()
    queue = deque()
    parent = {}
    queue.append(start)
    visited.add(start)
    parent[start] = None
    while queue:
        curWord = queue.popleft()
        if isOneCharDiffer(curWord, stop):
            parent[stop] = curWord
            break

        for n in getNext(words, curWord, visited):
            if n is not visited:
                queue.append(n)
                parent[n] = curWord
                visited.add(n)
    if stop not in parent:
        return ["-1"]
    returnL = deque()
    backTrack = stop
    while backTrack:
        returnL.appendleft(backTrack)
        backTrack = parent[backTrack]
        if start == stop:
            parent[start] = None
    if len(returnL) == 1:
        return ["-1"]
    return list(returnL)


# words =  ["cat", "hat", "bad", "had"]
# print(string_transformation(words, "bat", "had"))

# words =  ["cccw", "accc", "accw"]
# print( string_transformation(words, "cccc", "cccc"))

words =  []
print( string_transformation(words, "zzz", "zzz"))
#
# words =  ["a","b","c",]
# print( string_transformation(words, "y", "z"))


