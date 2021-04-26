"""
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers, determine whether or not it's a palindrome.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list
"""

class LinkedNode(object):
  def __init__(self, x, next = None):
    self.val = x
    self.next = next

# Time: O(n) Space: O(n)
# def isPalindrome(head):
#     if head == None:
#         return True
#     cur = head
#     shared = [head]
#     return helper(cur, shared)
#
#
# def helper(backward, forward):
#     re = True
#     if backward.next:
#         re = helper(backward.next, forward)
#
#     if forward[0].val != backward.val:
#         re = False
#     forward[0] = forward[0].next
#     return re

# Time O(N) Space O(1)
def isPalindrome(head):
    if head == None:
        return True
    fast, slow = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    while fast.next:
        fast = fast.next

    prev = slow
    slow = slow.next
    prev.next = None

    prev = slow
    slow = slow.next
    prev.next = None

    while slow: # Bug: while slow and slow.next:
        next = slow.next
        slow.next = prev
        prev = slow
        slow = next

    head1, head2  = head, fast
    while head1:
        print(head1.val, end= "")
        head1 = head1.next
    print()
    while head2:
        print(head2.val, end="")
        head2 = head2.next
    print()
    head1, head2 = head, fast
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next

    if head2:
        return False
    return True

    return slow.val, fast.val


l= LinkedNode(1, LinkedNode(2, LinkedNode(1)))
print(isPalindrome(l))
# l= LinkedNode(1, LinkedNode(2, LinkedNode(1, LinkedNode(3))))
# print(isPalindrome(l))