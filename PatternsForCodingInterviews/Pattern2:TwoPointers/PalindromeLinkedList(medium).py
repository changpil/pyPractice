# Palindrome LinkedList (medium) #
# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
#
# Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished.
# The algorithm should have O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.
#

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

# With Extra space O(N)
# def is_palindromic_linked_list(head):
#     arr = []
#     cur = head
#     while cur:
#       arr.append(cur.value)
#       cur = cur.next
#     return isPalindrome(arr)
#
# def isPalindrome(arr):
#   i, j = 0, len(arr)-1
#   while i < j:
#     if arr[i] != arr[j]:
#       return False
#     i += 1
#     j -= 1
#   return True

#O(N^2)
# def getValue(n, head):
#     while n:
#         head = head.next
#         n -= 1
#     return head.value
#
# def is_palindromic_linked_list(head):
#     nodes =0
#     cur =head
#     while cur:
#         nodes += 1
#         cur = cur.next
#
#     start , end = 0, nodes -1
#
#     while start < end:
#         if getValue(start, head) != getValue(end, head):
#             return False
#         start += 1
#         end -= 1
#     return True

# Educative Time O(N) Space O(1)
def reverse(head):
    cur = head
    next = cur.next
    while next:
        tmp = next.next
        next.next = cur
        cur = next
        next = tmp
    head.next = None
    return cur

def is_palindromic_linked_list(head):
    half, start = head, head
    while start and start.next:
        start = start.next.next
        half = half.next

    tail = reverse(half)
    start, end  = head, tail
    result = True
    while start and end:
        if start.value != end.value:
            result = False
            break
        start = start.next
        end = end.next

    #There is next in the last of the node
    #i = head
    #while i.next:
    #    i = i.next

    reverse(tail)
    #i.next = head2

    return result

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  cur = head
  while cur:
      print(f"{cur.value} --> ", end="")
      cur=cur.next
main()