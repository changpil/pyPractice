"""
find to the kth last element of signlly linked list
"""
from LinkedList import LinkedList

def removeKthFromLast(ll, k):
    #eliminate k is less than 0 ot not int
    if k < 0 or not isinstance(k, int):
        raise ValueError("Kth should be positive integer")

    if ll.node is None:
        return
    # k is len
    if len(ll) == k:
        ll.node = ll.node.next
        return

    i, leap = ll.node, 0
    while leap != k and i != None:
        i = i.next
        leap += 1

    prev= ll.node
    kth=ll.node
    while i != None:
        i = i.next
        prev=kth
        kth=kth.next
        #normal cases
    if kth != None:
        prev.next=kth.next
    else:
        prev.next = None


ll= LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)
print(ll)

removeKthFromLast(ll, 3)
print(ll)
removeKthFromLast(ll, 3)
print(ll)
removeKthFromLast(ll, 3)
print(ll)
removeKthFromLast(ll, 3)
print(ll)
#removeKthFromLast(ll, 2)
print(ll)
removeKthFromLast(ll, 1)
print(ll)
removeKthFromLast(ll, 1)
print(ll)
"""
Without testing I had some errors.
removeKthFromLast(ll, 0) : the last element
removeKthFromLast(ll, 6) : the first element
"""