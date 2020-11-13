from LinkedList import LinkedList
# sorted LinkedList
def remove_duplicates(ll):
    if ll == None:
        return
    p = ll.head
    pp = p.next

    while pp != None:
        if p .data == pp.data:
            p.next = pp.next
            pp = p.next
        else:
            p = pp
            pp=pp.next


linkelist1 = LinkedList()
linkelist1.add(15)
linkelist1.add(15)
linkelist1.add(15)
linkelist1.add(10)
linkelist1.add(5)
linkelist1.add(4)
linkelist1.add(4)
linkelist1.p()
print("#"*100)
remove_duplicates(linkelist1)
linkelist1.p()