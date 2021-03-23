import collections


def getSrcDst(w1, w2):
    for i in range(min(len(w1), len(w2))):
        if w1[i] != w2[i]:
            return w1[i], w2[i]
    return None, None


def build_graph(words):
    vertices = set()
    for w in words:
        for c in w:
            vertices.add(c)
    graph = {} #collections.defaultdict(set)
    for v in vertices:
        graph[v] = set()
    for i in range(1, len(words)):
        src, dst = getSrcDst(words[i - 1], words[i])
        if src and dst:
            graph[src].add(dst)
    return graph


def bfs(graph, c, visited, topsort):
    visited.add(c)
    for n in graph[c]:
        if n not in visited:
            bfs(graph, n, visited, topsort)
    topsort.appendleft(c)



def alienOrder(words):
    graph = build_graph(words)
    print(graph)
    ingress = {}
    for src, dsts in graph.items():
        for dst in dsts:
            ingress[dst] = ingress.get(dst, 0) + 1
    visited = set()
    topsort = collections.deque()
    for c in graph:
        if c not in ingress:

            bfs(graph, c, visited, topsort)
            if len(topsort) == len(graph):
                return "".join(list(topsort))
    return ""

# ""
s = ["abc","ab"]
print(alienOrder(s))

# "yxz"
s = ["zy","zx"]
print(alienOrder(s))