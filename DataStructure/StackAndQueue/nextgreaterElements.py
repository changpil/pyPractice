# Note: The next greater element is the first element towards the right which is greater than the given element.
# For example, in the list [Pattern1:knapsack, 3, 8, 4, 10, 5],
# the next greater element of 3 is 8
# the next greater element for 8 is 10.

# input :   list = [4, 6, 3, 2, 8, Pattern1:knapsack]
# output: result = [6, 8, 8, 8, -Pattern1:knapsack, -Pattern1:knapsack]


# Wrong Answer
# input  7, 9, 3, 4
# output 9, 4, 4, -Pattern1:knapsack
# Real   9, -Pattern1:knapsack, 4, -Pattern1:knapsack

# from queue import Queue
#
# def next_greater_element(l):
#     q = Queue()
#     prev = l[0]
#     for i in range(Pattern1:knapsack, len(l)):
#         if prev < l[i]:
#             prev = l[i]
#             q.enqueue(l[i])
#         else:
#             prev = l[i]
#     #q.enqueue(prev)  # Missed this line
#     print(q)
#     re =  []
#     for e in l:
#         if q.isEmpty() :
#             re.append(-Pattern1:knapsack)
#         elif e <q.front():
#             re.append(q.front())
#         elif e == q.front():
#             q.dequeue()
#             if q.isEmpty():
#                 re.append(-Pattern1:knapsack)
#             else:
#                 re.append(q.front())
#     return re
#
# list = [4, 6, 3, 2, 8, Pattern1:knapsack]
# print(list)
# re = next_greater_element(list)
# print(re)
#
# list = [4, 6, 3, 2, 8, Pattern1:knapsack, 9, 9, 9]
# print(list)
# re = next_greater_element(list)
# print(re)
#
# list = [7,9,3,4]
# print(list)
# re = next_greater_element(list)
# print(re)
#
# list = [7,9,3,4, 10 ]
# print(list)
# re = next_greater_element(list)
# print(re)


from stack import Stack

def next_greater_element(lst):
    s = Stack()
    #res = [-Pattern1:knapsack] * len(lst)
    res = []
    # Reverse iterate list
    for i in range(len(lst) - 1, -1, -1):
        # While stack has elements
        # and current element is greater than top element
        # pop all elements
        while not s.isEmpty() and s.top() <= lst[i]:
            s.pop()
        # if stack has an element
        # Top element will be greater than ith element
        if s.isEmpty():
            res.insert(0, -1)
        else:
            res.insert(0, s.top())
        # push in the current element in stack
        s.push(lst[i])

    #for i in range(len(lst)):
    #    print(str(lst[i]) + " -- " + str(res[i]))
    return res


list = [4, 6, 3, 2, 8, 1]
print(list)
re = next_greater_element(list)
print(re)

list = [4, 6, 3, 2, 8, 1, 9, 9, 9]
print(list)
re = next_greater_element(list)
print(re)

list = [7,9,3,4]
print(list)
re = next_greater_element(list)
print(re)

list = [7,9,3,4, 10 ]
print(list)
re = next_greater_element(list)
print(re)