class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def clone(root):
    if root == None:
        return
    newNode = TreeNode(root.val)
    newNode.left = clone(root.left)
    newNode.right = clone(root.right)
    return newNode

import collections
def clone_iterrative(root):
    q = collections.deque()
    newRoot = TreeNode(root.val)
    q.append((root, newRoot))
    while q:
        for _ in range(len(q)):
            node, newNode = q.popleft()
            if node.left:
                newL = TreeNode(node.left.val)
                newNode.left = newL
                q.append((node.left, newL))
            if node.right:
                newR = TreeNode(node.right.val)
                newNode.right = newR
                q.append((node.right, newR))
    return newRoot

def printTree(node):
    q =collections.deque()
    q.append(node)
    while q:
        for node in q:
            print(node.val, end = " ")
        print()
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
printTree(root)
print()
root = clone(root)
printTree(root)
print()
root = clone_iterrative(root)
printTree(root)