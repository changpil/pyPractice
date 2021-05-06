
class Node():
   def __init__(self, val=None, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

# complete the function below

import math
def isBST(root):
    if root == None:
        return True
    return _isBTS(root, -math.inf, math.inf)

def _isBTS(node, left, right):
    if node == None:
        return True
    if not (left < node.val < right):
        return False

    leftTree = _isBTS(node.left, left, node.val)
    if not leftTree:
        return False
    rightTree = _isBTS(node.right, node.val, right)
    if not rightTree:
        return False
    return True


bst = Node(10, Node(4, Node(1), Node(7)), Node(15, Node(13), Node(18)))
print(isBST(bst))


bst = Node(10, Node(4, Node(1), Node(7)), Node(15, Node(13), Node(12)))
print(isBST(bst))
