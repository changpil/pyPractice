"""
find to the kth last element of signlly linked list
"""

from LinkedList import LinkedList

def remove_kth_from_last(l, k):
    count = 1
    i = l.node.next
    if l.node.next == None:
        return
    while count != k and i.next != None:
        count += 1
        i = i.next
    if count != k:
        return
    prev = l.node
    kth = l.node.next

    try:
        while i.next != None:
            i = i.next
            prev = kth
            kth = kth.next
        prev.next = kth.next
    except AttributeError as e:
        pass

l= LinkedList()
l.add("asa")
l.add("sss")
l + "zzz"
l.add("aaa")
print(l)
remove_kth_from_last (l, 0)
print(l)
remove_kth_from_last (l, 3)
print(l)
remove_kth_from_last (l, 3)
print(l)
remove_kth_from_last (l, 3)
print(l)
remove_kth_from_last (l, 3)
print(l)
remove_kth_from_last (l, 2)
print(l)
remove_kth_from_last (l, 1)
print(l)