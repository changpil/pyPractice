from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inOrder(root):
    stack, order = [], []
    cur = root
    while cur or stack:
        while cur:
            #order.append(cur.val) PreOrder
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        order.append(cur.val)
        cur = cur.right
    return order


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(19)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(26)

    print(inOrder(root))

main()


