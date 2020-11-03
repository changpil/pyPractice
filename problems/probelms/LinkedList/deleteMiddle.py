from LinkedList import LinkedList

def deletMiddle(l):
    if l.node.next == None:
        return
    count = 0
    i = l.node.next
    while i != None:
        i = i.next
        count += 1
    half = count//2
    prev = l.node
    i    = l.node.next
    while half != 0:
        prev = i
        i = i.next
        half -=1
    prev.next=i.next
    return l

l=LinkedList()
l.add("1")
l.add("2")
l.add("10")
l.add("5")
l.add("8")
l.add("5")
l.add("3")

print(l)
a= deletMiddle(l)
print(a)



