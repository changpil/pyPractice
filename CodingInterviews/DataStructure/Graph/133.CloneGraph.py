
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    visited = set()
    newNodes = {}
    dfs(node, visited, newNodes)
    return newNodes[node.val]

def dfs(node, visited, newNodes):
    visited.add(node.val)
    newNode = Node(node.val)
    newNodes[newNode.val] = newNode
    for n in node.neighbors:
        if n.val not in visited:
            dfs(n, visited, newNodes)
            if newNode.neighbors == None:
                newNode.neighbors = []
            newNode.neighbors.append(newNodes[n])
        else:
            if newNode.neighbors == None:
                newNode.neighbors = []
            newNode.neighbors.append(newNodes[n])
