"""
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.
"""

"""
Bipartite
Bipartite graphs are equivalent to two-colorable graphs i.e., coloring of the vertices using two colors in such a way that vertices of the same color are never adjacent along an edge. 
"""

def isBipartite(graph):
    visited = set()
    parents = {}
    colors = {}
    for v in range(len(graph)):
        if v not in visited:
            if bfs(graph, v, visited, parents, colors) == False:
                return False
            # parents[v] = None
            # colors[v] = True
            # visited.add(v)
            # if dfs(graph, v, visited, parents, colors) == False:
            #     return False
    return True


import collections
def bfs(graph, v, visited, parents, colors):
    q = collections.deque()
    q.append(v)
    visited.add(v)
    parents[v] = None
    colors[v] = True
    while q:
        src = q.popleft()
        for ne in graph[src]:
            if ne not in visited:
                visited.add(ne)
                q.append(ne)
                colors[ne] = not colors[src]
                parents[ne] = src
            else:
                if colors[ne] == colors[src]:
                    return False
    return True

def dfs(graph, v, visited, parents, colors):

    for ne in graph[v]:
        if ne not in visited:
            visited.add(ne)
            parents[ne] = v
            colors[ne] = not colors[v]
            if not dfs(graph, ne, visited, parents, colors):
                return False
        else:
            if colors[ne] == colors[v]:
                return False
    return True

graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(isBipartite(graph)) # False


graph = [[1,3],[0,2],[1,3],[0,2]]
print(isBipartite(graph)) # True