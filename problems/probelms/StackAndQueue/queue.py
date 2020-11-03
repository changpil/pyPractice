class Queue:

    class Node:
        def __init__(self, data, next):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = self.Node("TAIL",None)

    def add(self, data):
        pre = self.head
        ptr = pre.next
        if ptr == None:
            new_node = self.Node(data, self.head)
            self.head = new_node
            return
        while True:
            if ptr.data == "TAIL":
                break
            pre = ptr
            ptr= ptr.next
        new_node = self.Node(data, ptr)
        pre.next = new_node


    def remove(self):
        if self.head.data == "TAIL":
            raise IndexError
        rv = self.head.data
        self.head = self.head.next
        return rv

    def peek(self):
        if self.head.data == "TAIL":
            raise IndexError
        return self.head.data

    def isEmpty(self):
        rv = False
        if self.head.data == "TAIL":
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


