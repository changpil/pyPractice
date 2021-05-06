from collections import deque


class Stack:
    def __init__(self):
        self._stack = deque()

    def push(self, i):
        self._stack.append(i)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return None if self.empty() else self._stack[-1]

    def empty(self):
        return len(self._stack) == 0


class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self._minstack = []  # append, pop

    def push(self, i):
        super().push(i)
        if len(self._minstack) == 0:
            self._minstack.append(i)
        else:
            if i <= self._minstack[-1]:
                self._minstack.append(i)

    def pop(self):
        temp = super().pop()
        if temp == self._minstack[-1]:
            self._minstack.pop()
        return temp

    def min(self):
        """ Returns the minimal value in the stack """
        return None if len(self._minstack) == 0 else self._minstack[-1]


ms = MinStack()
ms.push(5)
print(ms.min())  # should print: 5
ms.push(1)
ms.push(3)
print(ms.min())  # should print: 1
print(ms.pop())  # should print: 3
print(ms.min())  # should print: 1
print(ms.pop())  # should print: 1
print(ms.min())  # should print: 5

print("#" * 20)

ms = MinStack()
ms.push(5)
print(ms.min())
ms.push(1)
ms.push(1)
ms.push(3)

print(ms.min())  # should print: 1
print(ms.pop())  # should print: 3
print(ms.min())  # should print: 1
print(ms.pop())  # should print: 1
print(ms.min())  # should print: 1
print(ms.pop())  # should print: 1
print(ms.min())  # should print: 5
print(ms.pop())  # should print: 5
print(ms.min())  # should print: None