# Course Schedule
# There are n courses to take, they are referred to by numbers from 0 to n-1.
# Some of them have prerequisites, e.g. courses A and B must be completed before course C can be taken (in other words, course C depends on A and B).
# Find and return an ordering in which all the given courses can be taken while satisfying all the prerequisites.
# If there exists more than one such ordering, any one of them would be a correct answer.
# If no such ordering exists, return a special value: [-1].
def build_graph(n, prerequisites):
    graph = {}
    for i in range(n):
        graph[i] = []
    for e in prerequisites:
        fr, to = e[1], e[0]
        graph[fr].append(to)
    return graph


def course_schedule(n, prerequisites):
    """
    Args:
        n (int)
        prerequisites (List[List[int]])
    Returns:
        List[int]
    """
    graph = build_graph(n, prerequisites)
    s = topSort(graph)
    if s == None:
        return [-1]
    l = []
    while s:
        l.append(s.pop())
    return l


def topSort(graph):
    visited = set()
    stack = []
    done = set()
    for v in graph:
        if v not in visited:
            if topologicalsort(graph, v, visited, stack, done):
                return None
    return stack


def topologicalsort(graph, v, visited, stack, done):
    visited.add(v)
    for neb in graph[v]:
        if neb not in visited:
            if topologicalsort(graph, neb, visited, stack, done):
                return True
        else:
            if neb not in done:
                return True
    stack.append(v)
    done.add(v)
    return False


prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

print(course_schedule(len(prerequisites), prerequisites))
