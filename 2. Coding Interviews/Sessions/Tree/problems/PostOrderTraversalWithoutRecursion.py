'''
 class TreeNode():
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr
'''


# Complete the function below.
# The function takes a TREENODE as input and is expected to return an INTEGER ARRAY.
def postorder_traversal(root):
    order = []
    stack = []
    cur = root

    while cur or stack:
        while cur:
            if cur.right_ptr:
                stack.append(cur.right_ptr)
            stack.append(cur)
            cur = cur.left_ptr

        cur = stack.pop()
        if cur.right_ptr and stack and cur.right_ptr is stack[-1]:
            head = cur
            cur = stack.pop()
            stack.append(head)
        else:
            order.append(cur.val)
            cur = None
    return order
