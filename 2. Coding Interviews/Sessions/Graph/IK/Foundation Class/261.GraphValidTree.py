"""
https://leetcode.com/problems/graph-valid-tree/
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.



Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
"""


def validTree(n, edges):
    graph = build(n, edges)
    visited = set()
    component = 0
    parents = {}
    for v in graph:
        if v not in visited:
            cycle = bfs(graph, v, visited, parents)
            # parents[v] = None
            # cycle = dfs(graph, v, visited, parents)
            if cycle:
                return False
            component += 1
            if component > 1:
                return False
    return True

import collections
def build(v, edges):
    graph = collections.defaultdict(lambda: [])
    for i in range(v):
        graph[i]
    for src, dst in edges:
        graph[src].append(dst)
        graph[dst].append(src)
    return graph

def bfs(graph, v, visited, parents):
    q = collections.deque()
    q.append(v)
    visited.add(v)
    parents[v] = None
    while q:
        src = q.popleft()
        for ne in graph[src]:
            if ne not in visited:
                visited.add(ne)
                q.append(ne)
                parents[ne] = src
            else:
                if parents[src] != ne:
                    return True
    return False

def dfs(graph, v, visited, parents):
    visited.add(v)
    for ne in graph[v]:
        if ne not in visited:
            visited.add(ne)
            parents[ne] = v
            if dfs(graph, ne, visited, parents):
                return True
        else:
            if parents[v] != ne:
                return True
    return False
edges = [[0,1],[0,2],[0,3],[1,4]]
print(validTree(5, edges))

edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
print(validTree(5, edges))

edges = [[0,1],[2,3]] # False
print(validTree(4, edges))