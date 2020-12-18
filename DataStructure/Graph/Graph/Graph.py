class Graph:
    def __init__(self, vertices, edges, directed=False):
        self.graph = dict()
        self.directed = directed
        for v in vertices:
            self.graph[v] = set()

        for s, d in edges:
            self.graph[s].add(d)
            if not directed:
                self.graph[d].add(s)

    def add_edge(self, s, d):
        if s not in self.graph:
            self.graph[s] = set()

        if d not in self.graph:
            self.graph[d] = set()

        self.graph[s].add(d)
        if not self.directed:
            self.graph[d] = s

    def add_vertex(self, v):
        self.graph[v] = set()

    def __str__(self):
        s = ""
        for vertex in self.graph:
            s += f"{vertex} : "
            for neighbor in self.graph[vertex]:
                s += f"{neighbor} "
            s += "\n"
        return s



g = {   "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "c", "d", "e"],
        "d" : ["a", "c"],
        "e" : ["c"],
        "f" : []
    }

e = []
for k in g:
    for d in g[k]:
        e.append([k, d])
graph = Graph(g.keys(), e, True)
print(g)
print(graph)
graph.add_edge("a", "f")
graph.add_vertex("g")
print(graph)