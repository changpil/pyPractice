from LinkedList import LinkedList

#merge with  first linkedin
def merge(linkelist1, linkelist2):
    h1 = linkelist1.head
    h2 = linkelist2.head
    if h1 == None:
        linkelist1.head = h2
        return
    elif h2 == None:
        linkelist1.head = h1
        return
    else:
        if h1.data < h2.data:
            linkelist1.head = h1
            p, pp = h1, h1.next
            q = h2
        else:
            linkelist1.head = h2
            p, pp = h2, h2.next
            q = h1

    while pp != None and q != None:
        if pp.data <= q.data:
            p = pp       # this is mistake
            pp = pp.next

        else:
            tmp_q = q.next
            p.next = q
            q.next = pp
            p = q
            q = tmp_q


    if q != None:
        p.next = q

#merge with new linkedin
def get_merge(linkelist1, linkelist2):
    ll = LinkedList()
    h1 = linkelist1.head
    h2 = linkelist2.head

    if h1 == None:
        ll.head = h2
    elif h2 == None:
        ll.head = h1
    else:
        if h1.data > h2.data:
            ll.head = h2
            p, pp = h2, h2.next
            q = h1
        else:
            ll.head = h1
            p, pp = h1, h1.next
            q = h2

    while pp != None and q != None:
        if pp.data > q.data:
            next_q = q.next
            p.next = q
            q.next = pp
            p = q
            q = next_q
        else:
            p = pp
            pp = pp.next

    if q !=None:
        p.next = q
    return ll





linkelist1 = LinkedList()
linkelist1.add(15)
linkelist1.add(10)
linkelist1.add(5)
linkelist1.add(4)
linkelist1.p()

linkelist2 = LinkedList()
linkelist2.add(15)
linkelist2.add(12)
linkelist2.add(4)
linkelist2.add(2)
linkelist2.p()

print("#"*100)
#merge(linkelist1,linkelist2)
#linkelist1.p()

mergedlinkedlist = get_merge(linkelist1,linkelist2)

mergedlinkedlist.p()
