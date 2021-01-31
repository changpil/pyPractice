# Given a strongly connected directed graph, build a new graph with the same number of nodes but every edge reversed.
# This is also called transposing a graph.

# For your reference:
#
class Node:
    def __init__(self):
        self.val = 0
        self.neighbours = []

# First
# def build_other_graph(node):
#     visited = set()
#     reverse_node = None
#     reverseNodes = {}
#     for v in node.neighbours:
#         if v.val not in visited:
#             reverse_node = dfs(v, visited, reverseNodes)
#     return reverse_node
#
# def dfs(v, visited, reverseNode):
#     visited.add(v.val)
#     node = Node()
#     node.val = v.val
#     reverseNode[node.val] = node
#     for neb in v.neighbours:
#         if neb.val not in visited:
#             revneb = dfs(neb, visited, reverseNode)
#             revneb.neighbours.append(node)
#         else:
#             reverseNode[neb.val].neighbours.append(node)
#     return node

def build_other_graph(node):
    visited = set()
    reverseNodes = {}
    for v in node.neighbours:
        if v.val not in visited:
            dfs(v, visited, reverseNodes)
    if not reverseNodes:
        r = Node()
        r.val = node.val
        return r
    return reverseNodes[node.val]

def dfs(v, visited, reverseNode):
    visited.add(v.val)
    node = Node()
    node.val = v.val
    reverseNode[node.val] = node
    for neb in v.neighbours:
        if neb.val not in visited:
            dfs(neb, visited, reverseNode)
            reverseNode[neb.val].neighbours.append(node)
        else:
            reverseNode[neb.val].neighbours.append(node)

n = Node()
n.val = 1
n = build_other_graph(n)




