import sys
sys.path.append(".")
from graph_implementation_options.array_linkedlist_graph import Graph
from lib.myQueue import MyQueue

# O(v^E) Recursive solution
def minpath(g, s, d, n, visited):
    if s == d:
        return n

    if s in visited:
        return -1

    visited.add(s)
    cur = g.array[s].get_head()
    steps = []

    while cur:
        _min = minpath(g, cur.data, d, n+1, visited)
        if _min > 0:
            steps.append(_min)
        cur = cur.next_element

    visited.remove(s)

    if len(steps) == 0:
        return -1
    return min(steps)

def find_min(g, source, destination):
    visited = set()
    _min = minpath(g,source,destination, 0, visited)
    return _min


#
# g= Graph(6)
# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(0,3)
# g.add_edge(2,4)
# g.add_edge(3,5)
# g.add_edge(5,4)
#
# g.print_graph()
# print(find_min(g, 0, 4))
#
#
# g= Graph(6)
# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(0,3)
# g.add_edge(2,5)
# g.add_edge(3,5)
# g.add_edge(5,4)
# g.add_edge(1,3)
#
# g.print_graph()
# print(find_min(g, 0, 4))





# iterrative solution O(E+V)
# This is much better solution
def find_min(g, a, b):
    num_of_vertices = g.vertices
    # A list to hold the history of visited nodes (by default all false)
    # Make a node visited whenever you enqueue it into queue
    visited = set()

    # For keeping track of distance of current_node from source
    distance = [0] * num_of_vertices

    # Create Queue for Breadth First Traversal and enqueue source in it
    queue = MyQueue()
    queue.enqueue(a)
    visited[a] = True
    # Traverse while queue is not empty
    while (not queue.is_empty()):
        # Dequeue a vertex/node from queue and add it to result
        current_node = queue.dequeue()
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Queue
        # and also update their distance from `a`
        # by adding 1 in current_nodes's distance
        temp = g.array[current_node].head_node
        while (temp is not None):
            if (visited not in temp.data) or (temp.data is b):
                queue.enqueue(temp.data)
                visited.add(temp.data)
                distance[temp.data] = distance[current_node] + 1
                if temp.data is b:
                    return distance[b]
            temp = temp.next_element
    # end of while
    return -1

g= Graph(6)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(2,4)
g.add_edge(3,5)
g.add_edge(5,4)

g.print_graph()
print(find_min(g, 0, 4))


g= Graph(6)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(2,5)
g.add_edge(3,5)
g.add_edge(5,4)
g.add_edge(1,3)

g.print_graph()
print(find_min(g, 0, 4))