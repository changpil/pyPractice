import collections


def reverse(s):
    stack = collections.deque()

    start, i = 0, 0
    while s[i] != " ":
        i += 1

    stack.append(s[start: i])
    start = i
    isspace = False
    while i < len(s):
        if s[i] == " ":
            isspace = True
        if isspace and s[i] != " ":
            stack.append(s[start: i])
            start = i
            isspace = False
        i += 1

    stack.append(s[start:])
    result = []
    while stack:
        t = foo(stack.pop())
        result.append(t)
    return "".join(result)


def foo(s):
    i = len(s) - 1
    print(s)
    while i >= 0 and i == " ":
        i -= 1

    t = s[i:] + s[:i + 1]
    print(t)
    return t
# w = " abc  d    gzzzz   "
# print(reverse(w))

# print(foo("gzzzz   "))

w = " a b cdef"
print(reverse(w))