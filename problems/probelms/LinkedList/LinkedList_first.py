
class LinkedList:
    class Node:
        def __init__(self, obj, next):
            self.obj, self.next = obj, next

    def __init__(self):
        self.head = self.Node("HEAD", None)

    def add(self, obj):
        prev=self.head
        target=prev.next
        prev.next=self.Node(obj, target)

    def __str__(self):
        i = self.head.next
        _str=""
        while i != None:
            _str += str(i.obj) + " => "
            i=i.next
        return _str + "None"

    def remove(self, target = None):
        if target == None:
            self.head.next = self.head.next.next if self.head.next != None else None
            return

        prev = self.head
        i = self.head.next
        if i == None:
            return
        while i.next != None:
            if i.obj == target:
                break
            prev = i
            i = i.next
        prev.next = i.next


    def remove_from_last(self):
        prev=self.head
        i=self.head.next
        if i == None:
            return
        while i.next != None:
            prev = i
            i = i.next
        prev.next = None

def test():
    l=LinkedList()
    l.add("asa")
    l.add("sss")
    l.add("zzz")
    l.add("aaa")
    print(l)
    l.remove("aaa")
    print(l)
    l.remove("zzz")
    print(l)
    l.remove("sss")
    print(l)
    l.remove("asa")
    print(l)
    l.remove("asa")
    print(l)
test()