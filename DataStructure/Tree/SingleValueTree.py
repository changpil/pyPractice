
count = 0
def findSingleValueTrees(root):
    helper(root)
    return count

def helper(node):
    global count
    if node == None:
        return True

    l = helper(node.left)
    # if not l:
    #     return False

    r = helper(node.right)
    # if not r:
    #     return False
    if not ( l and r):
        return False
    if node.left and node.left.val != node.val:
        return False

    if node.right and node.right.val != node.val:
        return False
    count += 1
    return True
