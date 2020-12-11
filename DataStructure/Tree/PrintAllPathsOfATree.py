# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below
# Input: root of the input tree
# Output: A list of integer lists denoting the node values of the paths of the tree

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left_ptr = left
        self.right_ptr = right

def allPathsOfABinaryTree(root):
    result, running_path = [], []
    helper(root, result, running_path)
    return result

def helper(node, result, running_path):

    # I do not understand without this, it has an left_ptr error.
    # Edge case: In the case of Node is None
    if node == None:
        return


    if node.left_ptr == None and node.right_ptr == None:
        running_path.append(node.val)
        result.append(running_path.copy())
        running_path.pop()
        return

    running_path.append(node.val)
    if node.left_ptr:
        helper(node.left_ptr, result, running_path)

    if node.right_ptr:
        helper(node.right_ptr, result, running_path)

    running_path.pop()


def main():
    root = TreeNode(-1)
    root.left_ptr = TreeNode(0)
    #root.right_ptr = TreeNode(0)
    #root.left_ptr.left_ptr = TreeNode(1)
    root.left_ptr.right_ptr = TreeNode(1)
    #root.right_ptr.left_ptr = TreeNode(15)
    #root.right_ptr.right_ptr = TreeNode(26)
    print(allPathsOfABinaryTree(root))

main()