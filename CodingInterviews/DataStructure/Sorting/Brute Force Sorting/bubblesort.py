# Put the smallest element in the first place by bubbling up
# put the next smallest element in the next place by bubbling up

def i_bubbleSort(l):
    for i in range(1, len(l)):
        for j in range(len(l)-1, i-1, -1):
            if l[j-1] > l[j]:
                l[j-1], l[j] = l[j], l[j-1]

def r_bubbleSort(l):
    _r_bubbleSort(l, len(l)-1)

def _r_bubbleSort(l, n):
    if n == 0:
        return

    _r_bubbleSort(l, n-1)
    while n >= 1 and l[n-1] > l[n]:
        l[n-1], l[n] = l[n], l[n-1]
        n -= 1

l = [4,3,0, 2,-3, 1]
i_bubbleSort(l)
print(l)

l = [4,3,0, 2,-3, 1]
r_bubbleSort(l)
print(l)