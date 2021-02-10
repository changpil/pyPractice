class Node(object):
   def __init__(self, data=None, left=None, right=None):
       self.data = data
       self.left = left
       self.right = right


# least_lca = None
#
#
# def lca(root, a, b):
#     _lca(root, a, b)
#
#     if least_lca:
#         return least_lca.data
#     return None
#
#
# def _lca(root, a, b):
#     global least_lca
#
#     if root == None:
#         return False
#
#     l = _lca(root.left, a, b)
#     r = _lca(root.right, a, b)
#
#     if l and r:
#         least_lca = root
#         return True
#
#     # This took so long to figure out: Edge Case
#     # lca(root, a, a)
#     if root is a and  root is b:
#         least_lca = root
#         return True
#
#     if (root is a) or (root is b):
#         if l or r:
#             least_lca = root
#         return True
#
#     if l or r:
#         return True
#
#
#     return False

def lca(root, a, b):
    # Write your code here
    lcaP = [None]
    helper(root, a, b, lcaP)
    return lcaP[0]


def lca(root, a, b):
    # Write your code here
    lcaP = [None]
    helper(root, a, b, lcaP)
    return lcaP[0]


def helper(node, a, b, lcaP):
    if node == None:
        return None

    left = helper(node.left, a, b, lcaP)
    right = helper(node.right, a, b, lcaP)

    if (left == a and right == b) or (left == b and right == a):
        lcaP[0] = node.data
        return
    if (left == a and node == b) or (left == b and node == a):
        lcaP[0] = node.data
        return
    if (right == a and node == b) or (right == b and node == a):
        lcaP[0] = node.data
        return
    if a == node == b:
        lcaP[0] = node.data
        return

    if left and not right:
        return left

    if right and not left:
        return right

    if node == a:
        return a
    if node == b:
        return b


def main():
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    print("d"*100)
    print(lca(node, 2, 3))

main()