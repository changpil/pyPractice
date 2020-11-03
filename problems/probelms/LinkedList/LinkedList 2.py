class Node:
    def __init__(self, obj, next):
        self.object=obj
        self.next=next

class LinkedList:
    def __init__(self, obj=None, next=None):
        self.node = None

    def add(self, obj):
        if self.node == None:
            self.node = Node(obj,None)
        else:
            p=self.node.next
            #self.node=Node(obj,p) # Wrong
            self.node = Node(obj, self.node)

    def addLast(self, obj):
        i=self.node
        if i == None:
            self.add(obj)
            return
        while i.next != None:
            i=i.next
        i.next=Node(obj=obj,next=None)

    def getLast(self):
        i=self.node
        while i != None:
            i=i.next
        return i.object

    def remove(self):
        if self.node == None:
            return
        i=self.node.next
        self.node=i


    def removeElement(self, obj):
        prev = self.node
        i=self.node
        while i != None:
            if i.object == obj and self.node.object == obj:
                self.node = self.node.next
            if i.object == obj:
                prev.next= i.next
            prev=i
            i=i.next

    def removeLast(self):
        if self.node == None:
            return
        i=self.node
        prev=i
        while i.next != None:
            prev=i
            i=i.next
        prev.next=None

    def contains(self,obj):
        i = self.node
        while i != None:
            if i.object == obj:
                return True
            i = i.next
        return False

    def __len__(self):
        i = self.node
        count =0
        while i != None:
            count +=1
            i = i.next
        return count

    def __str__(self):
        ss=str()
        i = self.node
        while i != None:
            ss += str(i.object) + " ==> "
            i=i.next
        return ss + "None"


if __name__ == "__main__":
    ll = LinkedList()
    ll.add(5)
    ll.add(4)
    ll.add(3)
    ll.add(2)
    ll.add(1)
    ll.addLast(6)
    print(ll)
    ll.removeLast()
    print(ll)
    ll.removeElement(1)
    print(ll)
    ll.removeElement(5)
    print(ll)
    ll.remove()
    print(ll)
    ll.remove()
    print(ll)
    ll.remove()
    print(ll)
    ll.remove()
    print(ll)
    ll.addLast("a")
    ll.addLast("b")
    ll.addLast("c")
    print(ll)