
# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# pp = None
# p = None
# leaf = False
# head = None
#
#
# def flipUpsideDown(root):
#     """Complete this function.
#     Args:
#         root (TreeNode): Root of the input tree
#     Returns:
#         TreeNode: Root of the output tree
#     """
#     global p
#     helper(root)
#
#     if p:
#         p.left_ptr = None
#         p.right_ptr = None
#     if pp:
#         pp.right_ptr = None
#         pp.left_ptr = None
#
#     return head
#
#
# def helper(cur):
#     global pp, p, leaf, head
#
#     if cur == None:
#         return
#
#     flipUpsideDown(cur.left_ptr)
#     flipUpsideDown(cur.right_ptr)
#
#     if not head:
#         head = cur
#
#     if leaf:
#         leaf = False
#     else:
#         if pp :
#             pp.left_ptr = p
#             pp.right_ptr = cur
#         leaf = True
#     pp = p
#     p = cur

def getleftmost(root):
    if root.left_ptr == None:
        return root
    re = getleftmost(root.left_ptr)
    return re


def flipUpsideDown(root):
    """Complete this function.
    Args:
        root (TreeNode): Root of the input tree
    Returns:
        TreeNode: Root of the output tree
    """
    if root == None:
        return None
    head = getleftmost(root)
    helper(root, None)
    root.left_ptr = None
    root.right_ptr = None
    return head


def helper(node, parent):
    if node == None:
        return

    helper(node.left_ptr, node)
    if parent:
        node.left_ptr = parent.right_ptr
    node.right_ptr = parent