# Using your knowledge, create an efficient min() function using a stack.
# You have to implement the MinStack class which will have a min() function.
# Whenever min() is called, the minimum value of the stack is returned in O(1) time.
# The element is not popped from the stack. Its value is simply returned.
import heapq
class Node:
    def __init__(self, n, left= None, right = None):
        self.num = n
        self.left = left
        self.right = right
    def __lt__(self, other):
        return self.num < other.num

class MinStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.stack = []

    def push(self, n):
        if self.head == None:
            self.head = Node(n)
            self.tail = self.head
            self.stack.append(self.tail)
        else:
            newNode = Node(n)
            self.tail.right = newNode
            newNode.left = self.tail
            self.tail = newNode
            if self.stack[-1].num >= newNode.num:
                self.stack.append(newNode)

    def pop(self):
        if self.head is self.tail:
            ptr = self.head
            self.head = None
            self.tail = None
        else:
            ptr = self.tail
            self.tail= self.tail.left
            self.tail.right = None

        if ptr is self.stack[-1]:
            self.stack.pop()
        return ptr.num

    def min(self):
        return self.stack[-1].num

    def top(self):
        return self.tail.num

    def __str__(self):
        s = ""
        cur = self.head
        while cur:
            s += str(cur.num) + " <-> "
            cur = cur.right
        s +=  "\n"
        return s



# s = MinStack()
# s.push(1); s.push(3); s.push(2);s.push(1)
#
# print(s)
# print(s.min())
# s.pop()
# print(s)
# print(s.min())
# s.pop()
# print(s)
# print(s.min())
# s.pop()
# print(s)
# print(s.min())

s = MinStack()
s.push(-2); s.push(0); s.push(-3)

print(s.min())
s.pop()
s.top()
print(s.min())
print(s)