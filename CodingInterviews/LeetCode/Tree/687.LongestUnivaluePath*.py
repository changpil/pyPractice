"""
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestUnivaluePath(root):
    if root == None:
        return 0
    maxpath = [0]
    foo(root, maxpath)
    return maxpath[0]


def foo(node, maxpath):
    if node.left == None and node.right == None:
        return node.val, 0

    leftV, leftX, rightV, rightX = None, 0, None, 0
    if node.left:
        leftV, leftX = foo(node.left, maxpath)
        if leftV == node.val:
            leftX += 1

    if node.right:
        rightV, rightX = foo(node.right, maxpath)
        if rightV == node.val:
            rightX += 1

    if node.left and node.right and leftV == rightV == node.val:
        maxpath[0] = max(maxpath[0], rightX + leftX)
        return node.val, max(rightX, leftX)
    if node.left and node.val == leftV:
        maxpath[0] = max(maxpath[0], leftX)
        return node.val, leftX

    if node.right and node.val == rightV:
        maxpath[0] = max(maxpath[0], rightX)
        return node.val, rightX
    return node.val, 0