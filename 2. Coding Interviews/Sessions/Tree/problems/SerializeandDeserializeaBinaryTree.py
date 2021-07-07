import collections
import os
def deserialize(filename):
    result = []
    with open(os.path.join(os.getcwd(), filename), "r") as f:
        temp = f.readline().split()
    for c in temp:
        if c == "None":
            result.append(None)
        else:
            result.append(int(c))

    queue = collections.deque()
    root = TreeNode(result[0])
    queue.append(root)
    i = 1
    while queue:
        one = queue.popleft()
        left, right = None, None
        if result[i]!= None:
            left = TreeNode(result[i])
        if result[i+1] != None:
            right = TreeNode(result[i+1])
        one.left = left
        one.right = right
        if left:
            queue.append(left)
        if right:
            queue.append(right)
        i += 2
    return root



def serialize(root, filename):
    queue = collections.deque()
    queue.append(root)
    result = []
    while queue:
        one = queue.popleft()
        if one == None:
            result.append(None)
        else:
            result.append(one.val)
        if one:
            queue.append(one.left)
            queue.append(one.right)

    with open(os.path.join(os.getcwd(), filename), "w") as f:
        for c in result:
            f.write(str(c))
            f.write(" ")

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(0)
root.left = TreeNode(-7)
root.right = TreeNode(19)
root.left.left = TreeNode(-11)
root.right.left = TreeNode(15)
root.right.right = TreeNode(26)

def inOrder(root):
    stack, order = [], []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        order.append(cur.val)
        cur = cur.right
    return order
print(inOrder(root))
serialize(root, "serializedbst.tree")
root = deserialize("serializedbst.tree")
print(inOrder(root))