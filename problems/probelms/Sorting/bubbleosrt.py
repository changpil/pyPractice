
def bubbleSort(l):
    for _ in range(len(l)):
        for i in range(len(l) -1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]

l = [4,3,2,1]
bubbleSort(l)

print(l)