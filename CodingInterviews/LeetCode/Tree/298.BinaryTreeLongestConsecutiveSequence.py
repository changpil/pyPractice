"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
The longest consecutive path need to be from parent to child (cannot be the reverse).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestConsecutive(root):
    if not root:
        return 0
    return foo(root, None, 0)
    # gmax = [-math.inf]
    # foo(root, None, 0, gmax)
    # return gmax[0]
import math

# def foo(node, pNode, lmax, gmax):
#     if not pNode:
#         lmax = 1
#     else:
#         if pNode.val +1 == node.val:
#             lmax += 1
#         else:
#             gmax[0] = max(gmax[0], lmax)
#             lmax = 1
#     if not node.left and not node.right:
#         gmax[0] = max(gmax[0], lmax)
#         return
#     if node.left:
#         foo(node.left, node, lmax, gmax)
#     if node.right:
#         foo(node.right, node, lmax, gmax)



def foo(node, pNode, maxCN):
    localMax = -math.inf
    if not pNode:
        maxCN = 1
    else:
        if pNode.val + 1 == node.val:
            maxCN += 1
            localMax = maxCN
        else:
            localMax = maxCN
            maxCN = 1
    if node.left == None and node.right == None:
        return maxCN

    left, right = -math.inf, -math.inf
    if node.left:
        left = foo(node.left, node, maxCN)

    if node.right:
        right = foo(node.right, node, maxCN)

    return max(left, right, localMax)

root = TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(1,None, TreeNode(2, TreeNode(3))))))
print(longestConsecutive(root))