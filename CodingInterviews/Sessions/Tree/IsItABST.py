
# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below

def isBST(root):
    if root == None:
        return True

    l = isBST(root.left_ptr)
    r = isBST(root.right_ptr)

    if not (l and r):
        return False

    # if root.left_ptr and root.val < root.left_ptr.val:
    #     return False
    #
    # if root.right_ptr and root.val < root.right_ptr.val:
    #     return False

    if root.left_ptr:
        maxVal = maxNode(root.left_ptr).val
        if root.val < maxVal:
            return False

    if root.right_ptr:
        minVal = minNode(root.right_ptr).val
        if root.val > minVal:
            return False

    return True
