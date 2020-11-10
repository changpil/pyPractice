class Graph:
    def __init__(self, graph = None):
        if not graph:
            self.graph = dict()
        else:
            self.graph = graph

    def add_edge(self, source, destination):

        if not (source in self.graph.keys() and destination in self.graph.keys()):
            raise ValueError

        edges = self.graph.get(source,[])
        if destination not in edges:
            edges.append(destination)
        self.graph[source] = edges

    def add_vertex(self, v):
        if v not in self.graph.keys():
            self.graph[v] = []

    def __generate_edges(self):
        edges = set()
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                edges.add((vertex, neighbour))
        return edges

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

graph = Graph(g)
print(g)
print(graph)
graph.add_edge("a","f")
graph.add_vertex("g")
print(graph)