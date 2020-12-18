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

ts = 1
def _is_cyclic_dfs(g, v, visited, arrival, done):
    global ts
    visited.add(v)
    arrival[v] = ts
    ts += 1
    for neb in g.graph[v]:
        if neb not in visited:
            if _is_cyclic_dfs(g, neb, visited, arrival, done):
                return True
        else:
            if neb not in done:
                return True
    done[v] = ts
    ts += 1
    return False


def is_cyclic_dfs(g):
    global ts
    ts = 0
    visited = set()
    component = 0
    arrival = {}
    done = {}
    isCyclic = False
    for v in g.graph:
        if v not in visited:
            component += 1
            if _is_cyclic_dfs(g, v, visited, arrival, done):
                isCyclic = True
    s = ""
    for v in g.graph:
        s += f"{v} : "
        s += f"{True if v in visited else False} :{arrival.get(v, -1)}/{done.get(v, -1)} \n"
    print(s)

    return isCyclic


v = [1, 2, 3, 4]
edges = [[1, 4], [1, 2], [4, 3], [2, 3]]

g = Graph(v, edges, directed=True)
print(g)
print(is_cyclic_dfs(g))


v = [0, 1, 2, 3, 4, 5]
edges = [[0, 1], [0, 2], [1, 5], [2, 3], [2, 4]]
g = Graph(v, edges, directed=True)
print(g)
print(is_cyclic_dfs(g))

v = [0, 1, 2, 3, 4, 5]
edges = [[0, 1], [0, 2], [1, 5], [5, 2], [2, 4], [4, 3], [3, 5]]
g = Graph(v, edges, directed=True)
print(g)
print(is_cyclic_dfs(g))