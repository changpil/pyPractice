class Node:
    def __init__(self, data=None, next=None):
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

    def add_in_tail(self, data):
        p =  self.head
        newNode = Node(data, None)
        if p == None:
            self.head = newNode
            return
        while p.next != None:
            p = p.next
        p.next = newNode

    def remove(self, value):
        cur, prev = self.head, None

        while cur:
            if cur.data == value:
                if prev == None:
                    self.head = cur.next
                    return True
                else:
                    prev.next = cur.next
                    return True
            prev = cur
            cur = cur.next

    def search(self, value):
        p = self.head
        while p != None:
            if p.data == value:
                return True
            p = p.next
        return False

    def reverse(self):
        cur, prev = self.head, None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        self.head = prev

    @staticmethod
    def make_loop(ll):
        cur = ll.head
        prev = None
        while cur:
            prev = cur
            cur = cur.next
        prev.next = ll.head

    @staticmethod
    def detect_loop(ll):
        s = set()
        cur = ll.head
        while cur:
            if id(cur) in s:
                return True
            s.add(id(cur))
            cur = cur.next
        return False

    #Floyd’s Cycle-Finding Algorithm
    # def detect_loop(lst):
    #     onestep = lst.get_head()
    #     twostep = lst.get_head()
    #     while onestep and twostep and twostep.next_element:
    #         onestep = onestep.next_element  # Moves one node at a time
    #         twostep = twostep.next_element.next_element  # Skips a node
    #         if onestep == twostep:  # Loop exists
    #             return True
    #     return False

    @staticmethod
    def find_mid(lst):
        onestep = lst.get_head()
        if onestep == None:
            return None
        twosteps = onestep.next_element

        while twosteps and twosteps.next_element:
            onestep = onestep.next_element
            twosteps = twosteps.next_element.next_element
        return onestep.data

    def remove_duplicates(self):
        cur, prev = self.head, None
        s = set()

        if cur == None:
            return
        while cur:
            if cur.data in s:
                prev.next = cur.next
            else:
                s.add(cur.data)
            prev = cur
            cur = cur.next

    def find_nth(self, n):
        # Write your code here
        nth = self.haed
        for _ in range(n):
            if nth == None:
                return -1
            nth = nth.next_element
        cur = self.head
        while nth:
            nth = nth.next_element
            cur = cur.next_element
        return cur.data
    
    def __str__(self):
        p = self.head
        s = "head-->"
        while p:
            s += f"{p.data}-->"
            p = p.next
        s += "None"
        return s

l = LinkedList()
l.add_in_tail(-1)
l.remove(-1)
print(l)
l.reverse()
print(l)
l.add(4)
l.add(6)
l.add(8)
l.add(9)
print(l)
l.remove(9)
l.remove(6)
l.reverse()
print(LinkedList.detect_loop(l))


l = LinkedList()
l.add(4)
l.add(6)
l.add(8)
l.add(9)
LinkedList.make_loop(l)
print(LinkedList.detect_loop(l))

