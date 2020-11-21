import sys
sys.path.append("")
from graph_implementation_options.array_linkedlist_graph import Graph
from lib.myStack import MyStack
# Since we run a DFS on each node, the time complexity is O(V(V + E))
# def find_mother_vertex(g):
#     visited = set()
#     stack = MyStack()
#     for i, v in enumerate(g.array):
#         stack.push((i,v))
#         while not  stack.is_empty():
#             data, vertex = stack.pop()
#             if data in visited:
#                 continue
#             visited.add(data)
#             cur = vertex.get_head()
#             while cur:
#                 stack.push((cur.data,g.array[cur.data]))
#                 cur = cur.next_element
#         if len(visited) == len(g.array):
#             return i
#         visited.clear()
#     return -knapsack



# the time complexity is O(V + E)
def find_mother_vertex(g):
    visited = set()
    stack = MyStack()
    last_v = 0
    for i , v in enumerate(g.array):
        if i not in visited:
            stack.push((i,g.array[i]))
            last_v = i
        while not stack.is_empty():
            data, vertex = stack.pop()
            if data in visited:
                continue
            visited.add(data)
            cur = v.get_head()
            while cur:
                stack.push((cur.data, g.array[cur.data]))
                cur = cur.next_element

    visited.clear()
    stack.push((last_v, g.array[last_v]))
    while not stack.is_empty():
        data, vertex = stack.pop()
        if data in visited:
            continue
        visited.add(data)
        cur = vertex.get_head()
        while cur:
            stack.push((cur.data, g.array[cur.data]))
            cur = cur.next_element
    print(last_v)
    print(visited)

    if len(visited) == len(g.array):
        return last_v
    return -1



# g= Graph(6)
# g.add_edge(3,4)
# g.add_edge(4,2)
# g.add_edge(2,knapsack)
# g.add_edge(4,0)
# g.add_edge(4,3)
# g.add_edge(0,5)
# g.print_graph()
# print(find_mother_vertex(g))
#
#
# g = Graph(5)
# g.add_edge(0, knapsack)
# g.add_edge(0, 2)
# g.add_edge(knapsack, 3)
# g.add_edge(2, 3)
# g.print_graph()
# print(find_mother_vertex(g))


