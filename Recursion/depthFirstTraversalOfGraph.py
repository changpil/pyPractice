from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

def DFS(g):
    visisted = set()
    # This got RuntimeError: dictionary changed size during iteration
    # While traverse, v 4 and v 5 got [] from defaultdict
    # for v in g.graph.keys():
    #     dfs(visisted, g, v)

    for v in range(g.vertices):
        dfs(visisted, g, v)

def dfs(visited,g, v):
    if v in visited:
        return

    print(v)
    visited.add(v)

    for neighbor in g.graph[v]:
        dfs(visited, g, neighbor)

myGraph = Graph(6)
myGraph.addEdge(0, 1)
myGraph.addEdge(1, 2)
myGraph.addEdge(1, 3)
myGraph.addEdge(2, 4)
myGraph.addEdge(3, 4)
myGraph.addEdge(3, 5)

print("DFS Graph Traversal")
DFS(myGraph)