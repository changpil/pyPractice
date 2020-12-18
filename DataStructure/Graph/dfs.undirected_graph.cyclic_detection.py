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


def _is_cyclic_dfs(graph, v, visited, parent):
    visited.add(v)
    for neb in graph[v]:
        if neb not in visited:
            parent[neb] = v
            if _is_cyclic_dfs(graph, neb, visited, parent):
                return True
        else:
            if neb != parent[v]:
                return True
    return False


def is_cyclic_dfs(graph):
    visited = set()
    parent = {}
    component = 0
    isCyclic = False
    for v in graph:
        if v not in visited:
            component += 1
            if _is_cyclic_dfs(graph, v, visited, parent):
                isCyclic = True
    print(f"Cyclic Graph Result: {isCyclic}")
    return



# If graph is undirected, this logic works.
v = [1, 2, 3, 4]
edges = [[1, 4], [1, 2], [4, 3], [2, 3]]
g = build_graph(v, edges, directed=False)
print_graph(g)
is_cyclic_dfs(g)

# If graph is directed, this logic does not work.
#   1 --->  2 ---> 3
#    |             ^
#    |             |
#     ---> 4 --->  |


v = [1, 2, 3, 4]
edges = [[1, 4], [1, 2], [4, 3], [2, 3]]
g = build_graph(v, edges, directed=True)
print_graph(g)
is_cyclic_dfs(g)


