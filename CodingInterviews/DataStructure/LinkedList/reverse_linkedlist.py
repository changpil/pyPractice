from LinkedList import LinkedList
"""
def reverse(ll):
    h1  = ll.head
    if h1 == None or h1.next == None:
        return
    else:
        p = h1
        pp = h1.next
        p.next = None

    while pp != None:
        next_pp = pp.next
        pp.next = p
        p = pp
        pp = next_pp

    ll.head = p
"""

#recurive_way

def _reverse(p , pp):
    if pp == None:
        return p

    next_pp = pp.next
    pp.next = p
    p = pp
    pp = next_pp
    return _reverse(p, pp)

def reverse(ll):
    if ll.head == None or ll.head.next == None:
        return ll
    p = ll.head
    pp = p.next
    p.next = None

    new_head = _reverse(p, pp)
    ll.head = new_head






linkelist1 = LinkedList()
linkelist1.add(15)
linkelist1.add(10)
linkelist1.add(5)
linkelist1.add(4)
linkelist1.p()
print("#"*100)
reverse(linkelist1)
linkelist1.p()