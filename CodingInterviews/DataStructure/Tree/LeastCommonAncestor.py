class Node(object):
   def __init__(self, data, left=None, right=None):
       self.data = data
       self.left = left
       self.right = right


least_lca = None


def lca(root, a, b):
    _lca(root, a, b)

    if least_lca:
        return least_lca.data
    return None


def _lca(root, a, b):
    global least_lca

    if root == None:
        return False

    l = _lca(root.left, a, b)
    r = _lca(root.right, a, b)

    if l and r:
        least_lca = root
        return True

    # This took so long to figure out: Edge Case
    # lca(root, a, a)
    if root is a and  root is b:
        least_lca = root
        return True

    if (root is a) or (root is b):
        if l or r:
            least_lca = root
        return True

    if l or r:
        return True


    return False


def main():
    node = Node(1)
    node.left = Node(2)
    node.right = Node(1)

    print(lca(node, node, node))

main()