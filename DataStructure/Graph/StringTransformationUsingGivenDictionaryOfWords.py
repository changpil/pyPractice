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

def isOneDifference(w1, w2):
    diff = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff += 1
    if diff == 1:
        return True
    return False

def get_oneDifferedWords(w, words):
    neighbor_words = []
    for word in words:
        if isOneDifference(w, word) and word not in neighbor_words:
            neighbor_words.append(word)
    return neighbor_words

def build_graph(words):
    graph = dict()
    for w in words:
        graph[w] = get_oneDifferedWords(w, words)
    return graph

from collections import deque
def bfs(words, start, stop):
    if start not in words:
        words.append(start)
    if stop not in words:
        words.append(stop)
    graph = build_graph(words)
    queue = deque()
    visited = set()
    parent = {}
    queue.append(start)
    if start != stop:
        visited.add(start)
    parent[start] = None
    while queue:
        node = queue.popleft()
        for neb in graph[node]:
            if neb not in visited:
                visited.add(neb)
                queue.append(neb)
                parent[neb] = node
                if neb == stop:
                    return parent
    return parent

def string_transformation(words, start, stop):
    if isOneDifference(start, stop):
        return [start, stop]

    parent = bfs(words, start, stop)
    trace = deque()

    # End is not found
    if parent.get(stop, None) == None:
        return ["-1"]

    # found paths
    back = stop
    while back:
        trace.appendleft(back)
        if back == start == stop:
            tmp = parent[back]
            parent[back] = None
            back = tmp
        else:
            back = parent[back]

    return list(trace)

# words =  ["cat", "hat", "bad", "had"]
# print( string_transformation(words, "bat", "had"))
#

words =  ["cccw", "accc", "accw"]
print( string_transformation(words, "cccc", "cccc"))

words =  []
print( string_transformation(words, "zzz", "zzz"))

words =  ["a","b","c",]
print( string_transformation(words, "y", "z"))


