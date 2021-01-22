def createStack(l=None) : # Function to create an empty stack
  stack = None
  if l == None:
    stack = []
  else:
    stack = l
  return stack

def isEmpty(stack) :
  return len(stack) == 0

def push(stack, item) : # push item to stack
  stack.append( item )

def pop(stack) : # pop item from stack
  if(isEmpty(stack)) : # display error if stack empty
    print("Stack Underflow ")
    exit(1)
  return stack.pop()

def printStack(stack):
  for i in range(len(stack)-1, -1, -1) :
    print(stack[i], end = ' ')

# My Solution
def reverse(s) :
    if isEmpty(s):
        return
    top = pop(s)
    reverse(s)
    tmp = createStack()
    while not isEmpty(s):
        push(tmp,pop(s))
    push(s,top)
    while not isEmpty(tmp):
        push(s, pop(tmp))

def reverse(stack) :
  # Recursive case
  if not isEmpty(stack) :
    temp = pop(stack)
    reverse(stack)
    insertAtBottom(stack, temp)

def insertAtBottom(stack, item) : # Recursive function that inserts an element at the bottom of a stack.
  # Base case
  if isEmpty(stack) :
    push(stack, item)

  # Recursive case
  else:
    temp = pop(stack)
    insertAtBottom(stack, item)
    push(stack, temp)




# Driver Code
myStack = createStack()
push(myStack, str(8))
push(myStack, str(5))
push(myStack, str(3))
push(myStack, str(2))

print("Original Stack")
printStack(myStack)

reverse(myStack)

print("\n\nReversed Stack")
printStack(myStack)