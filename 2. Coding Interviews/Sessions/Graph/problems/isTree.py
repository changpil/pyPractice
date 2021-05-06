"""
Given a graph, find if it represents a tree.
The graph is traversed in both functions. Hence, the time complexity is O(V + E).
If we do well on mother of vertex.
"""
## Cyclic
## single component

import collections
def is_tree(graph):
    visited = set()
    parent = {}
    component = 0
    for v in graph:
        if v not in visited:
            if hasCycle(graph, v, parent, visited):
                return False
            component += 1
    if component > 1:
        return False
    return True

def hasCycle(graph, v, parent, visited):
    visited.add(v)
    for neig in graph[v]:
        if neig not in visited:
            parent[neig] = v
            hasCycle(graph, neig, parent, visited)
        else:
            if parent[neig] == v:
                return False
    return True