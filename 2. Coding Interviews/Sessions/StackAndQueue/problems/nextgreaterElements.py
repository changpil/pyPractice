# Note: The next greater element is the first element towards the right which is greater than the given element.
# For example, in the list [1, 3, 8, 4, 10, 5],
# the next greater element of 3 is 8
# the next greater element for 8 is 10.

# input :   list = [4, 6, 3, 2, 8, 1]
# output: result = [6, 8, 8, 8, 1, -1]

# Transform and Concur
def next_greater_element(l):
    stack = []
    stack.append(l[-1])
    for i in range(len(l)-2, -1, -1):
        if stack[-1] < l[i]:
            stack.append(l[i])
    nge = []
    for i in range(len(l)):
        if stack and l[i] == stack[-1]:
            stack.pop()
        if len(stack) == 0:
            nge.append(-1)
        elif stack[-1] > l[i]:
            nge.append(stack[-1])
        else:
            nge.append(-1)
    return nge

list = [4, 6, 3, 2, 8, 1]
print(list)
print(next_greater_element(list))

list = [4, 6, 3, 2, 8, 1, 9, 9, 9]
print(list)
print(next_greater_element(list))

list = [7,9,3,4]
print(list)
print(next_greater_element(list))

list = [7,9,3,4, 10 ]
print(list)
print(next_greater_element(list))