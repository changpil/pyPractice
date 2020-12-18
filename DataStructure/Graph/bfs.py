from collections import deque


# Since this algorithm traverses the whole graph once, its time complexity is O(V + E).
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


def bfs(g):
    visited = set()
    for v in g.graph:
        if v not in visited:
            visited.add(v)
            _bfs(g, v, visited)



def _bfs(g, v, visited):
    queue = deque()
    queue.append(v)
    visited.add(v)
    while queue:
        node = queue.popleft()
        visited.add(node)
        print(node, "-->", end="")
        for v in g.graph[node]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    print()



v = [0, 1, 2, 3, 4, 5]
edges = [[3, 4], [4, 2], [2, 1], [4, 0], [4, 3]]

g = Graph(v, edges, directed=False)
print(g)
bfs(g)


v = [0, 1, 2, 3, 4, 5]
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [4, 3]]
g = Graph(v, edges)
print(g)
bfs(g)
