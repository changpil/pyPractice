class Node(object):
   def __init__(self, data, left=None, right=None):
       self.data = data
       self.left = left
       self.right = right



def lca(root, a, b):
    if root == None:
        return None

    if root.data == a:
        return root.data

    if root.data == b:
        return root.data

    left = lca(root.left, a, b)
    right = lca(root.right, a, b)


    if left and right:
        return root.data

    return left or right

t = Node(1, Node(2), Node(3))

print(lca(t, 2, 1))


def lca(root, a, b):
    if root is None:
        return
    if root in (a,b):
        return root.data
    left = lca(root.left,a,b)
    right = lca(root.right,a,b)
    if left and right:
        return root.data
    return left or right