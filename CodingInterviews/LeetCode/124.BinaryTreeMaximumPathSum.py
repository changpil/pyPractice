# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# import math
#
#
# def maxPathSum(root):
#     maxValues = [-math.inf] * 2
#     foo(root, maxValues)
#     return maxValues[-1]
#
#
# def foo(node, pv):
#     if not node:
#         return
#
#     foo(node.left, pv)
#     tmp = pv[0]
#     if pv[0] == -math.inf:
#         if node.val < 0:
#             pv[0] = 0
#             pv[1] = node.val
#         else:
#             pv[0] = node.val
#             pv[1] = node.val
#
#     else:
#         pv[1] = max(pv[1], pv[0] + node.val)
#         if pv[0] + node.val < 0:
#             pv[0] = 0
#         else:
#             pv[0] += node.val
#     foo(node.right, pv)
#     pv[0] = tmp

import math



def maxPathSum( root) :
    tmp = []
    m = foo(root, tmp)
    return max(m, max(tmp))

def foo(node, tmp):
    if not node:
        return -math.inf

    l = foo(node.left, tmp)
    r = foo(node.right, tmp)

    m =  max(node.val, l, r, l + node.val, r + node.val, l + r + node.val)
    tmp.append(m)
    if l == -math.inf and r == -math.inf:
        return node.val
    # elif l != -math.inf and l >= r and l + node.val > 0:
    #     return l + node.val
    # elif r != -math.inf and r > l and r + node.val > 0:
    #     return r + node.val
    # else:
    #     return -math.inf

    return max(node.val, l + node.val, r + node.val)

node = TreeNode(2, None, TreeNode(-1, None, None))
print(maxPathSum(node))


node = TreeNode(-1, None, TreeNode(2, None, None))
print(maxPathSum(node))

node = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(maxPathSum(node))


node = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
print(maxPathSum(node))
# Input
# [1,-2,-3,1,3,-2,null,-1]
# Output
# 4
# Expected
# 3