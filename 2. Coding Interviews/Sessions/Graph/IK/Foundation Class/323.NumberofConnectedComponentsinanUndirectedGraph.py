"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.
"""


def countComponents(v, edges):

    graph = build(v, edges)
    visited = set()
    dfs_component = 0
    for v in graph:
        if v not in visited:
            dfs(graph, v, visited)
            dfs_component += 1

    visited.clear()
    bfs_component = 0
    for v in graph:
        if v not in visited:
            bfs(graph, v, visited)
            bfs_component += 1
    return dfs_component, bfs_component

import collections
def build(v, edges):
    graph = collections.defaultdict(lambda: [])
    for i in range(v):
        graph[i]
    for src, dst in edges:
        graph[src].append(dst)
        graph[dst].append(src)
    return graph

def dfs(graph, v, visited):
    visited.add(v)
    for ne in graph[v]:
        if ne not in visited:
            dfs(graph, ne, visited)
def bfs(graph, v, visited):
    q = collections.deque()
    q.append(v)
    visited.add(v)
    while q:
        src = q.popleft()
        for ne in graph[src]:
            if ne not in visited:
                visited.add(ne)
                q.append(ne)


edges = [[0,1],[1,2],[3,4]]
print(countComponents(5, edges))

edges = [[0,1],[1,2],[2,3],[3,4]]
print(countComponents(5, edges))

edges =  [[0,1],[0,2],[1,2]]
print(countComponents(4, edges))

edges = [[1,0]] # 1
print(countComponents(2, edges))

edges = [[2,3],[1,2],[1,3]]  #2
print(countComponents(4, edges))