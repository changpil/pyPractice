"""
input (7 -> Pattern1:knapsack -> 6) + (5 -> 9 -> 2) 617 + 295
output 9 -> Pattern1:knapsack ->2. That is 912
"""


from LinkedList import LinkedList

def sumList(l,k):
    i = l.node.next
    j = k.node.next
    a=""
    b=""
    while i != None:
        a += i.obj
        i = i.next

    while j != None:
        b += j.obj
        j = j.next

    a = a if len(a) != 0 else "0"
    b = b if len(b) != 0 else "0"
    print("{} {}".format(a, b))
    c= int(a) + int(b)

    print("result {}".format(str(c)))
    n=LinkedList()
    z=str(c)[::-1]
    print(z)
    for p in z:
        n.add(p)
    return n



l=LinkedList()
#l.add("7")
#l.add("Pattern1:knapsack")
#l.add("6")

print(l)

k=LinkedList()
k.add("5")
k.add("9")
k.add("2")
print (k)

n = sumList(l,k)

print(n)