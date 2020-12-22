# Find Order Of Characters From Alien Dictionary
# Given a sorted dictionary of an alien language, find the order of characters in the alphabet.
# Example One
#
# Input: ["baa", "abcd", "abca", "cab", "cad"]
# Output: "bdac"
# Example Two
# Input: words = ["caa", "aaa", "aab"]
# Output: "cab"

def build_graph(words):
    graph = {}
    for word in words:
        for c in word:
            if c not in graph:
                graph[c] = []
    for i in range(len(words) -1):
        j = 0
        char_len = min(len(words[i]), len(words[i+1]))
        while j < char_len and words[i][j] == words[i+1][j]:
            j += 1
        if j != char_len:
            graph[words[i][j]].append(words[i+1][j])
    return graph

# No cycle because it is lexicograpical order
def find_order(words):
    graph = build_graph(words)

    visited = set()
    stack = []
    for v in graph:
        if v not in visited:
            topologicalSort(graph, v, visited, stack)

    i = 0
    while i < len(stack)//2:
        stack[i] , stack[len(stack)-i-1] = stack[len(stack)-i-1], stack[i]
        i += 1
    return "".join(stack)

def topologicalSort(graph, node, visited, stack):
    visited.add(node)
    for v in graph[node]:
        if v not in visited:
            topologicalSort(graph, v, visited, stack)
    stack.append(node)

words = ["baa", "abcd", "abca", "cab", "cad"]

print(find_order(words))