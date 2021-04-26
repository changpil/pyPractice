"""
Note: Your solution should have O(n) time complexity, where n is the number of elements in l, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

Example

For l = [1, 2, 3, 4, 5] and k = 2, the output should be
reverseNodesInKGroups(l, k) = [2, 1, 4, 3, 5];
For l = [1, 2, 3, 4, 5] and k = 1, the output should be
reverseNodesInKGroups(l, k) = [1, 2, 3, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
reverseNodesInKGroups(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
1 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] integer k

The size of the groups of nodes that need to be reversed.

Guaranteed constraints:
1 ≤ k ≤ l size.

[output] linkedlist.integer

The initial list, with reversed groups of k elements.
"""

class ListNode(object):
  def __init__(self, x, next = None):
    self.value = x
    self.next = next

def reverseNodesInKGroups(l, k):
    num = 0
    cur = l
    while cur:
        cur = cur.next
        num += 1
    cycle = num//k
    prevlast, tail = l, l
    newHead = None
    while cycle:
        head, prevTail = tail, tail
        tail = tail.next
        reverse = k - 1
        while reverse:
            nextTail = tail.next
            tail.next = prevTail
            prevTail = tail
            tail = nextTail
            reverse -= 1
        if newHead == None:
            newHead = prevTail
        else:
            prevlast.next = prevTail
            prevlast = head
        cycle -= 1
    prevlast.next = tail
    return newHead

# l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# newl = reverseNodesInKGroups(l, 3)
#
# cur = newl
# while cur:
#     print(cur.value)
#     cur = cur.next

l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
newl = reverseNodesInKGroups(l, 3)

cur = newl
while cur:
    print(cur.value)
    cur = cur.next

