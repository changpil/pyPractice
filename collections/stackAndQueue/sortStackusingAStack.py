from stack import Stack

print("*"*10)
print("*  Solution1 O(n^2) *")
print("*"*10)

def sort(s):
    tmp = Stack()
    while not s.isEmpty():
        v = s.pop()
        while not tmp.isEmpty() and tmp.top() > v:
            s.push(tmp.pop())
        tmp.push(v)

    while not tmp.isEmpty():
        s.push(tmp.pop())


s = Stack()
s.push(-3)
s.push(10)
s.push(4)
s.push(9)

print(s)
sort(s)
print(s)

print("*"*10)
print("*  Solution2 recursive way without tmp stock O(n^2)*")
print("*"*10)

def sort(stack):
    if stack.isEmpty():
        return

    v = stack.pop()
    if stack.size() > 0  and v > stack.top():
        sort(stack)
        tmp = stack.pop()
        stack.push(v)
        v = tmp
    sort(stack)
    stack.push(v)


s = Stack()
s.push(-2);s.push(0);s.push(1);s.push(4);s.push(6);s.push(-1);s.push(10)
print(s)
sort(s)
print(s)

s = Stack()
s.push(23);s.push(60);s.push(12);s.push(42);s.push(4);s.push(97);s.push(2)
print(s)
sort(s)
print(s)
#
# def sort(stack):
#     if stack.isEmpty():
#         return
#         value = stack.pop()
#
#         # Sort the remaining stack recursively
#         sort(stack)
#
#         # Push the top element back into the sorted stack
#         insert(stack, value)
#
#
# def insert(stack, value):
#     if (stack.isEmpty() or value < stack.top()):
#         stack.push(value)
#     else:
#         temp = stack.pop()
#         insert(stack, value)
#         stack.push(temp)
#
#
# s = Stack()
# s.push(-3)
# s.push(10)
# s.push(4)
# s.push(9)
#
# print(s)
# sort(s)
# print(s)