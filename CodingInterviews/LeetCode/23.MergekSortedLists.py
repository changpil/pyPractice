# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from heapq import *
def mergeKLists(lists):
    head, tail = None, None
    minHeap = []
    for node in lists:
        heappush(minHeap, (node.val, node))
    while minHeap:
        _, minNode = heappop(minHeap)
        if not head:
            head = minNode
            tail = minNode
            if minNode.next:
                heappush(minHeap, (minNode.next.val, minNode.next))
        else:
            tail.next  = minNode
            if minNode.next:
                heappush(minHeap, (minNode.next.val, minNode.next))
            tail = minNode

    return head

l = []
one = ListNode(1, ListNode(2, ListNode(9)))
two = ListNode(7, ListNode(8, ListNode(16, ListNode(19))))
l.append(one)
l.append(two)

merged = mergeKLists(l)
while merged:
    print(merged.val)
    merged = merged.next

