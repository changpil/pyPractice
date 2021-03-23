# def minDepth(root):
#     if root == None:
#         return 0
#     return helper(root, 0)
#
# def helper(node, depth):
#     if node.left == None and node.right == None:
#         return depth + 1
#     leftDepth, rightDepth = float("inf"), float("inf")
#     if node.left:
#         leftDepth = helper(node.left, depth + 1)
#     if node.right:
#         rightDepth = helper(node.right, depth + 1)
#     return min(leftDepth, rightDepth)


