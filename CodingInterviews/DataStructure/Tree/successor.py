from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

successor = None
foundKey = False

def findSuccessor(root, key):
    global successor, foundKey

    if root == None:
        return

    findSuccessor(root.left, key)

    if foundKey and successor == None:
        successor = root

    if root.val == key:
        foundKey = True

    findSuccessor(root.right, key)



def main():
    global successor, foundKey
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(19)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(26)

    findSuccessor(root, 12)
    print(successor.val)


    successor, foundKey = None, None


    findSuccessor(root, 15)
    print(successor.val)

main()