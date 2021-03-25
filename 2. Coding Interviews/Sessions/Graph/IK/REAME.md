###Algorithm for directed graph and undirected graph
Popular graph search algorithms for interviews   
Breadth-first search (BFS) - bipartite, connected components & cycles    
Depth-first search (DFS)  - Topological Sort, connected components & cycles    
Prim’s algorithm for Minimum Spanning Trees   
Dijkstra’s algorithm for shortest paths   
Best-first search and A*   
DAG - Directed Acyclic Graph

### BFS Traverse Template
```
1. Build Adjacency List
2. BFS function
    for node in graph:
        if node not in visited:
            BFS(node)
        
3. Outer loop
    def bfs(graph, node):
        visited = set()
        q = collections.deque()
        q.append(node)
        visited.add(node)
        parent = [None] * len(graph)
        while q:
            v = q.popleft()
            for neigbor in graph[v]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
                    parent[neighbor] = v
Time Complexity: O(n) + O(m)
```

### DFS Template
```
def dfs(graph, node, visited):
    visited.add(node.val)
    for n in node.neighbors:
        if n.val not in visited:
            dfs(n, visited)
            
Time Complexity: O(n) + O(m)
```

### Foundation Class
323. Number of Connected Components in an Undirected Graph (medium)
261. Graph Valid Tree (medium)
785. Is Graph Bipartite (medium)
886. Possible Bipartite (medium)
200. Number of Islands (medium)
695. Max Area of Island (medium)
733. Flood Fill (easy)
909. Snake and Ladders (medium)
207. Course Schedule (medium)
210. Course Schedule II (medium)
1192. Critical Connections in a Network (hard)





 