import sys
sys.path.append(".")
from graph_implementation_options.array_linkedlist_graph import Graph
from lib.myStack import MyStack


# Since this algorithm traverses the whole graph once, its time complexity is O(V + E).
def traverse(g, s, visited):
    result = ""
    while not s.is_empty():
        edges = s.pop()
        if edges[0] in visited:
            continue
        result += "{}".format(edges[0])
        visited.add(edges[0])
        cur = edges[1].get_head()
        while cur:
            s.push((cur.data, g.array[cur.data]))
            cur = cur.next_element
    return result

# def dfs_traversal(g, source):
#     result = ""
#     s = MyStack()
#     visited = set()
#     s.push((source, g.array[source]))
#     result += traverse(g, s, visited)
#
#     for i in range(g.vertices):
#         if i not in visited:
#             s.push((i, g.array[i]))
#             result += traverse(g, s, visited)
#     return result

def dfs_traversal(g, source):
    result = ""
    s = MyStack()
    visited = set()

    order = [source] + [i for i in range(0, source)] + [i for i in range(source + 1, len(g.array))]
    for i in order:
        if i not in visited:
            s.push((i, g.array[i]))
            result += traverse(g, s, visited)
    return result

g= Graph(5)
g.add_edge(3,4)
g.add_edge(4,2)
g.add_edge(2,1)
g.add_edge(0,3)
g.print_graph()
print(dfs_traversal(g, 3))

g = Graph(7)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.print_graph()
print(dfs_traversal(g, 1))