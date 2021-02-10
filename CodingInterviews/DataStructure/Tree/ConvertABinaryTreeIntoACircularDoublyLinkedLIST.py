
class TreeNode():
   def __init__(self, val=None, left_ptr=None, right_ptr=None):
       self.val = val
       self.left_ptr = left_ptr
       self.right_ptr = right_ptr

# complete the function below


# predecessor = None
# head = None
#
# predecessor = None
# head = None
#
#
# def BTtoLL(root):
#     global predecessor, head
#     if root == None:
#         return head
#     cur = root
#     while cur.left_ptr:
#         cur = cur.left_ptr
#     head = cur
#     helper(root)
#     head.left_ptr = predecessor
#     predecessor.right_ptr = head
#     return head
#
# def helper(cur):
#     global predecessor
#     if cur.left_ptr:
#         helper(cur.left_ptr)
#     if predecessor:
#         # tmp = cur.right_ptr
#         cur.left_ptr = predecessor
#         predecessor.right_ptr = cur
#     predecessor = cur
#     if cur.right_ptr:
#         helper(cur.right_ptr)


def BTtoLL(root):
    if root == None:
        return None
    header, tail = root, root
    while header.left_ptr:
        header = header.left_ptr
    while tail.right_ptr:
        tail = tail.right_ptr
    inorder = [None]
    helper(root, inorder)
    header.left_ptr = tail
    tail.right_ptr = header
    return header


def helper(cur, inorder):
    if cur == None:
        return

    helper(cur.left_ptr, inorder)

    cur.left_ptr = inorder[0]
    if inorder[0] != None:
        inorder[0].right_ptr = cur

    inorder[0] = cur

    helper(cur.right_ptr, inorder)


root = TreeNode(1, TreeNode(2), TreeNode(3))
root.left_ptr.left_ptr = TreeNode(4)
root.left_ptr.right_ptr = TreeNode(5)

def printNodes(node, s):
    if node in s:
        return
    s.add(node)
    print(node.val, end="")
    printNodes(node.right_ptr, s)

printNodes(BTtoLL(root), set())