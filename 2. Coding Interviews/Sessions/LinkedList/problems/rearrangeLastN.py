"""
Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what you'll be asked during an interview.

Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.

Example

For l = [1, 2, 3, 4, 5] and n = 3, the output should be
rearrangeLastN(l, n) = [3, 4, 5, 1, 2];
For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
rearrangeLastN(l, n) = [7, 1, 2, 3, 4, 5, 6].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 105,
-1000 ≤ element value ≤ 1000.

[input] integer n

A non-negative integer.

Guaranteed constraints:
0 ≤ n ≤ list size.

[output] linkedlist.integer

Return l with the n last elements moved to the beginning.
"""
class ListNode(object):
  def __init__(self, x, next = None):
    self.value = x
    self.next = next

def rearrangeLastN(l, n):
    cur = l
    total = 0
    if l == None or n == 0:
        return l
    while cur:
        cur = cur.next
        total += 1
    n = n % total
    if n == 0:
        return l
    n = total - n
    cur = l
    prev = None

    while n:
        prev = cur
        cur = cur.next
        n -= 1
    prev.next = None
    newHead = cur

    while cur:
        prev = cur
        cur = cur.next

    prev.next = l
    return newHead



l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
newl = rearrangeLastN(l, 3)

cur = newl
while cur:
    print(cur.value)
    cur = cur.next
