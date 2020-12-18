class Graph:
    def __init__(self, vertices, edges, directed=True):
        self.graph = dict()
        self.directed = directed
        for v in vertices:
            self.graph[v] = set()

        for s, d in edges:
            self.graph[s].add(d)
            if not directed:
                self.graph[d].add(s)

    def __str__(self):
        s = ""
        for vertex in self.graph:
            s += f"{vertex} : "
            for neighbor in self.graph[vertex]:
                s += f"{neighbor} "
            s += "\n"
        return s


from collections import deque
def _is_cyclic_bfs(g, v, visited):
    queue = deque()
    queue.append(v)
    visited.add(v)
    parent = {}
    cyclic_graph = False
    while queue:
        node = queue.popleft()
        for v in g.graph[node]:
            if v in visited:
                # All visited Nodes are not cycled for undirected graph
                # If we return true, all graphs that have more than 1 node will be returned true
                #return True
                if parent[node] != v:
                    cyclic_graph =  True
            else:
                queue.append(v)
                visited.add(v)
                parent[v] = node
    return cyclic_graph

def is_cyclic_bfs(g):

    visited = set()
    component = 0
    for v in g.graph:
        if v not in visited:
            component += 1
            if _is_cyclic_bfs(g, v, visited):
                return True
    return False

v = [1, 2, 3, 4]
edges = [[1, 4], [1, 2], [4, 3], [2, 3]]

g = Graph(v, edges, directed=False)
print(g)
print(is_cyclic_bfs(g))


v = [0, 1, 2, 3, 4, 5]
edges = [[0, 1], [0, 2], [1, 5], [2, 3], [2, 4]]
g = Graph(v, edges, directed=False)
print(g)
print(is_cyclic_bfs(g))