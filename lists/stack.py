class Stack:
    def __init__(self):
        self.s = list()
    def push(self, item):
        self.s.append(item)
    def pop(self):
        return self.s.pop()
    def size(self):
        return len(s)
    def top(self):
        return self.s[len(self.s)-1]
    def empty(self):
        return True if len(self.s) != 0 else False

s = Stack()
for i in range(5):
    s.push(i)

for _ in range(5):
    print(s.pop())