"""
input :3 => 5 => 8 => 5 => 10 => 2 => Pattern1:knapsack => None [partition 5]
output:3 => Pattern1:knapsack => 2 => 5 => 5 => 10 => 8 => None
"""
from LinkedList import LinkedList

def partition(l, key):
    n = LinkedList()
    i = l.node.next
    while i != None:
        if int(i.obj) > key:
            n.add(i.obj)
        i=i.next
    i = l.node.next
    while i != None:
        if int(i.obj) == key:
            n.add(i.obj)
        i=i.next
    i = l.node.next
    while i != None:
        if int(i.obj) < key:
            n.add(i.obj)
        i = i.next
    return n


l= LinkedList()
l.add("Pattern1:knapsack")
l.add("2")
l.add("10")
l.add("5")
l.add("8")
l.add("5")
l.add("3")
print(l)
n = partition(l, 5)
print(n)
