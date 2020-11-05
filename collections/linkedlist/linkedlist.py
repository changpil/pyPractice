class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head == None:
            self.head = Node(data, None)
        else:
            self.head = Node(data, self.head)

    def remove(self, data):
        pp, p = None, self.head
        if p.data == data:
            self.head = p.next
        else:
            pp= p
            p = p.next
            while p:
                if p.data == data:
                    pp.next = p.next
                    break
                pp = p
                p = p.next
    def __str__(self):
        p = self.head
        s = "head-->"
        while p:
            s += f"{p.data}-->"
            p = p.next
        s += "None"
        return s

l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
print(l)
l.remove(4)
print(l)
l.remove(3)
print(l)
l.remove(1)
print(l)
l.remove(2)
print(l)