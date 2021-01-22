from Tree.bst import BST

kthMax = None
counter = 0
def findKthMax(root, k):
    return recursive_way(root, k)


def recursive_way(node, k):
    if node == None:
        return None
    global counter
    v1 = recursive_way(node.right, k)
    if v1 != None:
        return v1
    counter += 1
    if counter == k:
        return  node.val
    v3 = recursive_way(node.left, k)
    return v3

bst = BST(6)
bst.add(4)
bst.add(9)
bst.add(5)
bst.add(2)
bst.add(8)
print(bst)
print(findKthMax(bst.root, 4))