'''
    For your reference:

    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''

order = 0
knum = None
def kth_smallest_element(root, k):
    if root == None:
        return knum

    kth(root,k)
    return knum

def kth(root, k):
    global order, knum

    if root == None:
        return

    kth(root.left_ptr, k)
    order += 1
    if order == k:
        knum = root.val

    kth(root.right_ptr, k)
