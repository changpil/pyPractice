"""
return numm if the linkedlist is not cycled
 return starting point if the linkedlist is cycled

"""

from LinkedList import LinkedList

def make_cyclice_linkedlist(ll, k):
    h1 = ll.head
    if h1 == None:
        return
    p = h1
    pp = p.next

    while pp != None and k != 0:
        p =pp
        pp=pp.next
        k -= 1

    if k != 0:
        return

    k_point = p

    p = h1
    pp = p.next
    while pp!= None:
        p = pp
        pp = pp.next

    p.next = k_point


def cyclic_linkedlist(ll):
    _set = set()

    h1 =ll.head

    while h1 != None:
        if h1 in _set:
            return h1
        else:
            _set.add(h1)
        h1 = h1.next
    return None


linkelist1 = LinkedList()
linkelist1.add(15)
linkelist1.add(10)
linkelist1.add(5)
linkelist1.add(4)
linkelist1.p()
print("#"*100)
make_cyclice_linkedlist(linkelist1, 2)
linkelist1.p(10)

print(cyclic_linkedlist(linkelist1))
