"""
Given circular linked list, implement an algorithm that returns the node at the begining of the loop.

"""

from LinkedList.LinkedList import LinkedList

def detect_loop(head):
    s = set()
    cur = head

    while cur:
        if cur in s:
            return True
        s.add(cur)
        cur = cur.next
    return False

ll = LinkedList()
ll.add("a")
ll.add("b")
ll.add("c")
cur = ll.head
next = cur
while next.next:
    next = next.next
next.next = cur

print(detect_loop(ll.head))

def print_loop(head):
    d = dict()
    cur = head
    n = 0
    while cur:
        print(hash(cur))
        if cur in d:
            return d
        d[cur] = n
        cur = cur.next
        n += 1
    return d

print(print_loop(ll.head))