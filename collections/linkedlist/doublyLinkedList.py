class Node:
    def __init__(self, data, prev = None, next=None):
        self.data = data
        self.next = next
        self.prev = prev

class DLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            self.head = Node(data, None, self.head)

    def remove(self, value):
        p = self.head
        while p != None:
            if p.data == value:
                if p.prev == None:
                    self.head = p.next
                    p.next.prev = None  # Do not forget updating prev
                    return True
                else:
                    p.prev.next = p.next
                    if p.next != None:
                        p.next.prev = p.prev   # Do not forget updating prev
                    return True
            p = p.next
        return False

    def search(self, value):
        p = self.head
        while p != None:
            if p.data == value:
                return True
            p = p.next
        return False


    def __str__(self):
        p = self.head
        s = "head-->"
        while p:
            s += f"{p.data}<-->"
            p = p.next
        s += "None"
        return s

l = DLinkedList()
l.add(1)
l.add(2)
l.add(3)
print(l)
l.remove(4)
print(l)
l.remove(3)
print(l)

l = DLinkedList()
l.remove(3)
print(l)