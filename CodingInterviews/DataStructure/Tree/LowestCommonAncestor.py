"""
Lowest Common Ancestor in a Binary Tree | Set Pattern1:knapsack
3.5
Given a binary tree (not a binary search tree) and two values say n1 and n2, write a program to find the least common ancestor.
"""

from Tree.binarytree import BinaryTree, Node

#O(n^2)
def commonAncestor(root, n1, n2):
    if root == None:
        return None
    found = bool(findnode(root, n1) and findnode(root, n2))
    if not found:
        return None

    if findnode(root.left, n1) and findnode(root.left, n2):
        return commonAncestor(root.left, n1, n2)
    elif findnode(root.right, n1) and findnode(root.right, n2):
        return commonAncestor(root.right, n1, n2)
    else:
        return root



# O(n)
def findnode(root, n1):
    if root == None:
        return False

    if root.val is n1.val:
        return True
    return findnode(root.left, n1) or findnode(root.right, n1)


tree = Node("0")
tree.left = Node("Pattern1:knapsack")
tree.right = Node("2")
tree.left.left = Node("3")
tree.left.right = Node("4")
tree.right.left = Node("5")
tree.right.right = Node("6")
tree.right.right.left = Node("10")
tree.right.right.right = Node("7")
tree.right.right.right.right = Node("8")
print("------tree")
BinaryTree.print(tree)
node = commonAncestor(tree, tree.left, tree.right.right.right.right)
print(node.val)
