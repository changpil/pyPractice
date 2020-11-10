import sys
sys.path.append("")
from graph_implementation_options.array_linkedlist_graph import Graph
from lib.myStack import MyStack

# Since this algorithm traverses the whole graph once, its time complexity is O(V + E).
def isCyclic(g, s, visited):
    while not s.is_empty():
        edges = s.pop()
        print(f"{edges[0]} -->", end="")
        if edges[0] in visited:
            return True
        visited.add(edges[0])
        cur = edges[1].get_head()
        while cur:
            s.push((cur.data, g.array[cur.data]))
            cur = cur.next_element
    return False


# O(V+E), which we already know is the complexity of traversing the adjacency list that represents our graph.
def detect_cycle(g):
    s = MyStack()
    visited = set()

    order = [i for i in range(0, len(g.array))]
    for i in order:
        if i not in visited:
            s.push((i, g.array[i]))
            if isCyclic(g, s, visited) == True:
                return True
    return False

# g= Graph(5)
# g.add_edge(3,4)
# g.add_edge(4,2)
# g.add_edge(2,1)
# g.add_edge(0,3)
# g.print_graph()
# print(detect_cycle(g))
#
# g = Graph(7)
# g.add_edge(1, 2)
# g.add_edge(1, 3)
# g.add_edge(2, 4)
# g.add_edge(2, 5)
# g.add_edge(3, 6)
# g.print_graph()
# print(detect_cycle(g))
#
#
# g= Graph(5)
# g.add_edge(3,4)
# g.add_edge(4,2)
# g.add_edge(2,1)
# g.add_edge(0,3)
# g.add_edge(4,3)
# g.print_graph()
# print(detect_cycle(g))
#
# g = Graph(7)
# g.add_edge(1, 2)
# g.add_edge(1, 3)
# g.add_edge(2, 4)
# g.add_edge(2, 5)
# g.add_edge(3, 6)
# g.add_edge(6, 6)
# g.print_graph()
# print(detect_cycle(g))