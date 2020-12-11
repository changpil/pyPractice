# complete this function

    #For your reference:

class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None



def build_balanced_bst(a):
    if a == None:
        return None

    root = bst(a, 0, len(a)-1)
    return root

def bst(a, i, j):
    if i > j:
        return None
    mid = i + (j-i)//2

    newNode = TreeNode(a[mid])

    newNode.left_ptr = bst(a,i, mid -1 )
    newNode.right_ptr = bst(a, mid +1, j)

    return newNode
