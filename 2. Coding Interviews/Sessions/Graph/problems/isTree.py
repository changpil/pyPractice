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

################################################################
import collections


def is_graph_tree(n, edges):
    graph = buildGraph(n, edges)
    queue = collections.deque()
    visited = set()
    queue.append(n)
    component = 0
    parents = dict()
    parents[n] = None
    visited.add(n)
    while queue:
        node = queue.popleft()
        for neb in graph[node]:
            if neb not in visited:
                visited.add(neb)
                parents[neb] = node
                queue.append(neb)
            else:
                # parent is not cycle
                if parents[node] == neb:
                    pass
                else:
                    return False
    #print(visited)
    if len(visited) != len(graph):
        return False
    return True


def buildGraph(n, edges):
    graph = collections.defaultdict(lambda: [])
    for s, d in edges:
        graph[s].append(d)
        graph[d].append(s)
    return graph

print(is_graph_tree(3, [[1, 3], [2, 3], [1, 2]]))
print(is_graph_tree(4, [[1, 2], [1, 3], [3, 4], [4, 1]]))
print(is_graph_tree(4, [[1, 2], [1, 3], [3, 4], [4, 6]]))
print(is_graph_tree(4, [[1, 2], [1, 3], [3, 4], [4, 6], [9, 11]]))
