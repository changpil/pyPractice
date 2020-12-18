# Since this algorithm traverses the whole graph once, its time complexity is O(V + E).

def build_graph(vertices, edges, directed=True):
    graph = dict()
    directed = directed
    for v in vertices:
        graph[v] = set()

    for s, d in edges:
        graph[s].add(d)
        if not directed:
            graph[d].add(s)
    return graph

def print_graph(graph):
        s = ""
        for vertex in graph:
            s += f"{vertex} : "
            for neighbor in graph[vertex]:
                s += f"{neighbor} "
            s += "\n"
        print(s)
        return

def shortestPath(g, v1, v2):
    visited = []
    mindepth = {}
    done_explorer = {}
v = [i for i in range(6)]
e = [[0, 1], [0, 2], [0, 3], [2, 4], [3, 5], [5, 4]]
graph = build_graph(v, e,True)

print_graph(graph)
#print(find_min(g, 0, 4))

v = [i for i in range(6)]
e = [[0, 1], [0, 2], [0, 3], [2, 5], [3, 5], [5, 4], [1, 3]]
graph = build_graph(v, e,True)
print_graph(graph)
#print(find_min(g, 0, 4))