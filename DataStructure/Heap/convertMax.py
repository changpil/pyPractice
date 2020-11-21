def convertMax(maxHeap):
    for i in range(len(maxHeap)-1,-1,-1):
        minHeapify(maxHeap, i)
    return maxHeap

def minHeapify(a, i):

    while i < len(a):
        l = 2*i + 1
        r = 2*i + 2
        print(f"{l} {r}")

        if l < len(a) and r < len(a):
            if a[l] < a[i] < a[r] or a[l]< a[r] < a[i]:
                a[l], a[i] = a[i], a[l]
                i =l
            elif a[r] < a[i] < a[l] or a[r]< a[l] < a[i]:
                a[r], a[i] = a[i], a[r]
                i =r
            else:
                return
        elif l < len(a) and not r < len(a):
            if a[l] < a[i]:
                a[l], a[i] = a[i], a[l]
                i =l
            else:
                return
        elif not l < len(a) and r < len(a):
            if a[r] < a[i]:
                a[r], a[i] = a[i], a[r]
                i =r
            else:
                return
        else:
            return
    return

print("Expected Output: [-2, knapsack, 5, 9, 4, 6, 7]")
print(convertMax([9, 4, 7, 1, -2, 6, 5]))
print("Expected Output [knapsack, 2, 7, 3, 4, 14, 9, 12, 16, 15]")
print(convertMax([16, 15, 14, 12, 4, 7, 9, 2, 3, 1]))

# Recursive version
def minHeapify(heap, index):
    left = index * 2 + 1
    right = (index * 2) + 2
    smallest = index
    # check if left child exists and is less than smallest
    if len(heap) > left and heap[smallest] > heap[left]:
        smallest = left
    # check if right child exists and is less than smallest
    if len(heap) > right and heap[smallest] > heap[right]:
        smallest = right
    # check if current index is not the smallest
    if smallest != index:
        # swap current index value with smallest
        tmp = heap[smallest]
        heap[smallest] = heap[index]
        heap[index] = tmp
        # minHeapify the new node
        minHeapify(heap, smallest)
    return heap


def convertMax(maxHeap):
    # iterate from middle to first element
    # middle to first indices contain all parent nodes
    for i in range((len(maxHeap))//2, -1, -1):
        # call minHeapify on all parent nodes
        maxHeap = minHeapify(maxHeap, i)
    return maxHeap