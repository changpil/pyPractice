
class Stack:

    class Node:
        def __init__(self, data, next):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = self.Node("TAIL", None)

    def push(self, data):
        new_node = self.Node(data, self.head)
        self.head = new_node

    def pop(self):
        if self.head.next == None:
            raise IndexError
        item = self.head.data
        self.head = self.head.next
        return item

    def peek(self):
        if self.head.data == "TAIL":
            raise IndexError
        return self.head.data

    def isEmpty(self):
        rv = False
        if self.head.next == None:
            rv = True
        return rv

    def __str__(self):
        ptr = self.head
        rv = ""
        while True:
            if ptr.data == "TAIL":
                rv += "None"
                break
            rv += "{} => ".format(ptr.data)
            ptr = ptr.next
        return rv