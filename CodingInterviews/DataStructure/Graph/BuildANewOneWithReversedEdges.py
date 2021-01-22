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
    reversenodes = {}
    re = dfs(node, visited, reversenodes)
    return re

def dfs(node, visited, reversenodes):
    newNode = None
    if node.val not in  visited:
        visited.add(node.val)
        newNode = Node()
        newNode.val = node.val
        reversenodes[node.val] = newNode

    for n in node.neighbors:
        if n.val not in visited:
            nNode = Node()
            nNode.val = n.val
            reversenodes[n.val] = nNode
            nNode.neighbors.append(newNode)






