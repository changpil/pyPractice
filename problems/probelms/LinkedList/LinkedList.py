
class LinkedList:
    class Node:
        def __init__(self, data= None, next = None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = self.Node(data, self.head)
        self.head = new_node

    def remove(self, data):

        p = self.head
        pp = p
        if pp.data == data:
            if pp == self.head:
                self.head = self.head.next
                return True
        pp = p.next

        while pp != None:
            if pp.data == data:
                p.next = pp.next
                return True
            p = pp
            pp = pp.next

        return False



    def p(self, depth =100):
        p = self.head
        print("self.head==>", end='')
        while p != None and depth !=0:
            print("{}==>".format(p.data), end='')
            p = p.next      # Missed This : infinite loop
            depth -= 1
        print("None")