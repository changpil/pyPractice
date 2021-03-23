"""
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
"""


def diameterOfBinaryTree(root):
    if not root:
        return 0
    diameter = [0]
    foo(root, diameter)
    return diameter[0]

# I had some problem with calculating height.
def foo(node, diameter):
    # By definition leaf node is 0 height.
    # if you have root node only, height is 0
    if not node.left and not node.right:
        return 0
    left, right = 0, 0
    if node.left:
        left = foo(node.left, diameter) + 1
    if node.right:
        right = foo(node.right, diameter) + 1
    diameter[0] = max(diameter[0], left + right)
    return max(left, right)
