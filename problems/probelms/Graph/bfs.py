import sys
sys.path.append(".")
from graph_implementation_options.array_linkedlist_graph import Graph
from lib.myQueue import MyQueue

# Since this algorithm traverses the whole graph once, its time complexity is O(V + E).

def traverse(g, q, visited):
    result = ""
    while not q.is_empty():
        edges = q.dequeue()
        if edges[0] in visited:
            continue
        result += "{}".format(edges[0])
        visited.add(edges[0])
        cur = edges[1].get_head()
        while cur:
            q.enqueue((cur.data, g.array[cur.data]))
            cur = cur.next_element
    return result
# def bfs_traversal(g, source):
#     result = ""
#     q = MyQueue()
#     visited = set()
#     q.enqueue((source,g.array[source]))
#     result += traverse(g, q, visited)
#
#     # Search for vertices which is not reachable from source
#     for i in range(g.vertices):
#         if i not in visited :
#             q.enqueue((i,g.array[i]))
#             result += traverse(g, q, visited)
#     return result

def bfs_traversal(g, source):
    result = ""
    q = MyQueue()
    visited = set()
    order = [source] +[i for i in range(0,source)] + [i for i in range(source+1, len(g.array))]
    print(order)
    for i in order:
        if i not in visited :
            q.enqueue((i,g.array[i]))
            result += traverse(g, q, visited)
    return result

g= Graph(6)
g.add_edge(3,4)
g.add_edge(4,2)
g.add_edge(2,1)
g.add_edge(4,0)
g.add_edge(4,3)
g.print_graph()
print(bfs_traversal(g, 4))


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.print_graph()
print(bfs_traversal(g, 0))