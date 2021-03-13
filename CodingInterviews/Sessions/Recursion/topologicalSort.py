from collections import defaultdict


class Graph:

    # Constructor
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

def topologicalSort(myGraph) :
    visited = set()
    ts = []
    for v in range(myGraph.vertices):
        # My first error
        ts += _topologicalSort(visited, myGraph, v)
        ts =  _topologicalSort(visited, myGraph, v) + ts
    return ts

def _topologicalSort(visited, g, v):
  if v in visited:
    return []

  visited.add(v)
  ts = []
  for neighbor in g.graph[v]:
    ts += _topologicalSort(visited, g, neighbor)
  ts = [v] + ts
  return ts

myGraph = Graph(5)
myGraph.addEdge(0, 1)
myGraph.addEdge(0, 3)
myGraph.addEdge(1, 2)
myGraph.addEdge(2, 3)
myGraph.addEdge(2, 4)
myGraph.addEdge(3, 4)

print("Topological Sort: [0, Pattern1:knapsack, 2, 3, 4]")
print(topologicalSort(myGraph))

myGraph = Graph(6)
myGraph.addEdge(5, 2)
myGraph.addEdge(5, 0)
myGraph.addEdge(4, 0)
myGraph.addEdge(4, 1)
myGraph.addEdge(2, 3)
myGraph.addEdge(3, 1)
print("Topological Sort: [5, 4, 2, 3, Pattern1:knapsack, 0]")
print(topologicalSort(myGraph))