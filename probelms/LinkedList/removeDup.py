"""
Write code to remove duplicateds from an unsorted linked list
in-place?
"""

from LinkedList import LinkedList

#Difference between matched objects no skip prev.
def remove_dup(l):
    i = l.node.next
    if i is None:
        return

    while i != None:
        prev=i
        target=i.next
        while target != None:
            if i.obj == target.obj and target.next is not None:
                prev.next = target.next
                target= target.next     #####
            elif i.obj == target.obj and target.next is None:
                prev.next = None
                target = target.next    #####
            else:
                prev=target             #####
                target=target.next      #####
        i = i.next #(missed)

l=LinkedList()
l.add("a")
l.add("a")
l.add("a")
l.add("a")
l.add("b")
l.add("a")
l.add("c")
l.add("c")
print(l)
remove_dup(l)
print(l)

