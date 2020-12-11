'''
    For your reference:

    class TreeNode:
        def __init__(self):
            self.children = []

'''


# Complete the function below.

def find_height(root):
    return height(root)

def height(node):
    if node == None
        return 0

    maxHeight = -1

    for child in node.children:
        h = height(child)
        maxHeight = max(maxHeight, h)

    return maxHeight + 1