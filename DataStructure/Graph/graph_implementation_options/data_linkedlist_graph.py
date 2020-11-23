import sys
sys.path.append("../../../probelms")
from LinkedList.LinkedList import LinkedList

class Graph:
    class Node:
        def __init__(self, data=None, ll=None):
            self.data = data
            self.ll = LinkedList()

    def __init__(self):
        self.vertices = []

    def add_vertex(self, v):
        # check duplication and add
        self.vertices.append(Graph.Node(v))

    def add_edge(self, source, destination):
        #Error if there is no vertices on source or destination
        for node in self.vertices:
            if node.data == source:
                # Check duplication of destination in ll and add
                node.ll.add(destination)

    def __str__(self):
        s = ""
        for node in self.vertices:
            s += f"{node.data} : {node.ll}"
            s += "\n"
        return s

class Graph:
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # definining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.array = []
        # Creating a new Linked List for each vertex/index of the list
        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    # Function to add an edge from source to destination
    def add_edge(self, source, destination):
        if (source < self.vertices and destination < self.vertices):
            # As we are implementing a directed graph, (Pattern1:knapsack,0) is not equal to (0,Pattern1:knapsack)
            self.array[source].insert_at_head(destination)

        # If we were to implement an Undirected Graph i.e (Pattern1:knapsack,0) == (0,Pattern1:knapsack)
        # We would create an edge from destination towards source as well
        # i.e self.list[destination].insertAtHead(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        print
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while (temp is not None):
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")

g = Graph()
g.add_vertex("a"); g.add_vertex("b")
g.add_edge("a", "b")
g.add_vertex("c"); g.add_vertex("d")
g.add_edge("c", "b")
print(g)