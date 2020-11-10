class Stack:
    def __init__(self):
        self.s = list()
    def push(self, item):
        self.s.append(item)
    def pop(self):
        return self.s.pop()
    def size(self):
        return len(self.s)
    def top(self):
        return self.s[-1]
    def isEmpty(self):
        return True if len(self.s) == 0 else False
    def __str__(self):
        s = ("-"*5 + " stack " + "-"*5 + "\n")
        for i in range(len(self.s)):
            s += f" --> {self.s[i]}"
        s += "\n" + "-" * 20 + "\n"
        return s
# s = Stack()
# for i in range(5):
#     s.push(i)
#
# for _ in range(5):
#     print(s.pop())

# s = Stack()
# s.push(-3)
# s.push(10)
# s.push(4)
# s.push(9)
#
# print(s)