def sort(l):
    for i in range(1, len(l)):
        # all sorted beofore index i
        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                l[j], l[j-1] =l[j-1], l[j]
l=[9,8,7,6,5,4,3]

sort(l)
print(l)
