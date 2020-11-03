from LinkedList import LinkedList

def remove(ll, k):
    h1 = ll.head

    if h1 == None:
        return
    p = h1
    pp = p.next
    f = h1
    while f != None and k != 0:
        f = f.next
        k -= 1

    if f == None:
        ll.head = ll.head.next
        return

    while f.next != None:
        f = f.next
        p =pp
        pp=pp.next

    p.next = pp.next

linkelist1 = LinkedList()
linkelist1.add(15)
linkelist1.add(10)
linkelist1.add(5)
linkelist1.add(4)
linkelist1.p()
print("#"*100)

remove(linkelist1, 3)
linkelist1.p()

