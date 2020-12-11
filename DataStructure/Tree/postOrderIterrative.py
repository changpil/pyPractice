from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postOrder(root, order):
    stack = []
    cur = root
    while cur or stack:
        while cur:
            if cur.right:
                stack.append(cur.right)
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        if stack and cur and cur.right == stack[-1]:
            tmp = cur
            cur = stack.pop()
            stack.append(tmp)
        else:
            order.append(cur.val)
            #cur = stack.pop()
            cur = None





def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    postO = []
    postOrder(root, postO)
    print(postO)
main()