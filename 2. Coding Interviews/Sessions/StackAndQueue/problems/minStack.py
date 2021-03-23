# Using your knowledge, create an efficient min() function using a stack.
# You have to implement the MinStack class which will have a min() function. Whenever min() is called, the minimum value of the stack is returned in O(Pattern1:knapsack) time.
# The element is not popped from the stack. Its value is simply returned.
from stack import Stack

class MinStack:
    def __init__(self):
        self.s = Stack()
        self._min = Stack()

    def push(self, v):
        if self._min.isEmpty():
            self._min.push(v)
        elif self._min.top() >= v:
            self._min.push(v)
        self.s.push(v)

    def pop(self):
        if not self._min.isEmpty() and self.s.top() == self._min.top():
            self._min.pop()
        return self.s.pop()

    def min(self):
        return self._min.top()

    def __str__(self):
        _s = str(self.s)
        _s += ("\n" + "-" * 3 + " Minstack " + "-" * 3 + "\n")
        _s += str(self._min)

        return _s



s = MinStack()
s.push(1); s.push(3); s.push(2);s.push(1)

print(s)
print(s.min())
s.pop()
print(s)
print(s.min())
s.pop()
print(s)
print(s.min())
s.pop()
print(s)
print(s.min())
