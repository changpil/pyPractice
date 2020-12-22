# Given a strongly connected directed graph, build a new graph with the same number of nodes but every edge reversed.
# This is also called transposing a graph.

# For your reference:
#
class Node:
    def __init__(self):
        self.val = 0
        self.neighbours = []

def build_other_graph(node):
    visited = set()
    reverse_node = None
    reverseNodes = {}
    for v in node.neighbours:
        if v.val not in visited:
            reverse_node = dfs(v, visited, reverseNodes)
    return reverse_node

def dfs(v, visited, reverseNodes):

    node = Node()
    node.val = v.val
    reverseNodes[node.val] = node
    visited.add(v.val)

    for neb in v.neighbours:
        if neb.val not in visited:
            revneb = dfs(neb, visited, reverseNodes)
            revneb.neighbours.append(node)
        else:
            reverseNodes[neb.val].neighbours.append(node)
    return node


