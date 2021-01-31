import collections
def build_graph(equations, values):
    graph = collections.defaultdict(dict)
    for i, vars in enumerate(equations):
        src, dst = vars[0], vars[1]
        graph[src][dst] = values[i]
        graph[dst][src] = 1/values[i]
    return graph

def dfs(graph, src, dst, visited):
    if src not in graph or dst not in graph:
        return -1.0
    visited.add(src)
    if src == dst:
        return 1.0
    rev = 1
    for n in graph[src]:
        rev *= graph[src][n]
        if n not in visited:
            re = dfs(graph, n, dst, visited)
            if re != -1.0:
                return rev * re
        rev /= graph[src][n]
    return -1.0

def calcEquation(equations, values, queries):
    graph = build_graph(equations, values)
    visited = set()
    vals = []
    for src, dst in queries:
        visited.clear()
        val = dfs(graph, src, dst, visited)
        vals.append(val)
    return vals



equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(calcEquation(equations, values, queries))