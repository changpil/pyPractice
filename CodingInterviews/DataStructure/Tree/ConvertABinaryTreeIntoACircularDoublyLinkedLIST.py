
# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below


predecessor = None
head = None

predecessor = None
head = None


def BTtoLL(root):
    global predecessor, head
    if root == None:
        return head

    cur = root
    while cur.left_ptr:
        cur = cur.left_ptr
    head = cur

    helper(root)

    head.left_ptr = predecessor
    predecessor.right_ptr = head

    return head

def helper(cur):
    global predecessor

    if cur.left_ptr:
        helper(cur.left_ptr)

    if predecessor:
        # tmp = cur.right_ptr
        cur.left_ptr = predecessor
        predecessor.right_ptr = cur

    predecessor = cur

    if cur.right_ptr:
        helper(cur.right_ptr)