"""
Given a graph, find if it represents a tree.
The graph is traversed in both functions. Hence, the time complexity is O(V + E).
If we do well on mother of vertex.
"""

import sys
sys.path.append("")
from Graph.array_linkedlist_graph import Graph
from lib.myStack import MyStack
from bfs_undirected_graph_cyclic_detection import *
from motherVertex import *



def is_tree(g):
    isCyclic = detect_cycle(g)
    motherV = find_mother_vertex(g)
    if not isCyclic and motherV != -1:
        return True
    return False


g= Graph(5)
g.add_edge(3,4)
g.add_edge(4,2)
g.add_edge(2,1)
g.add_edge(0,3)
g.print_graph()
print(is_tree(g))

g = Graph(7)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.print_graph()
print(is_tree(g))


g= Graph(5)
g.add_edge(3,4)
g.add_edge(4,2)
g.add_edge(2,1)
g.add_edge(0,3)
g.add_edge(4,3)
g.print_graph()
print(is_tree(g))

g = Graph(7)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(6, 6)
g.print_graph()
print(is_tree(g))