"""
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example

For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
removeKFromList(l, k) = [1, 2, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 105,
-1000 ≤ element value ≤ 1000.

[input] integer k

An integer.

Guaranteed constraints:
-1000 ≤ k ≤ 1000.

[output] linkedlist.integer

Return l with all the values equal to k removed.
"""
# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x, next = None):
    self.value = x
    self.next = next

#### This has logical error: in case, 1 --> 2 --> 3 --> 3- -> 4
# def removeKFromList(l, k):
#     cur, prev = l, None
#     while cur:
#         if cur.value == k:
#             if prev == None:
#                 l = cur.next
#             else:
#                 prev.next = cur.next
#         prev = cur
#         cur = cur.next
#     return l

def removeKFromList(l, k):
    cur, prev = l, None
    if l == None:
        return l
    while cur and cur.value == k:
        cur = cur.next
    l = cur
    prev = None
    while cur:
        head = prev
        while cur and cur.value == k:
            head.next = cur.next
            cur = cur.next
        prev = cur
        if cur:
            cur = cur.next
    return l

l = ListNode(3, ListNode(2, ListNode(3, ListNode(3, ListNode(5)))))
newl = removeKFromList(l, 3)

cur = newl
while cur:
    print(cur.value)
    cur = cur.next


