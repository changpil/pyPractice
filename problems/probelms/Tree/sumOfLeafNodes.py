from Tree.bst import bst

def sumOfLeafNodes(node):

    if node.left == None and node.right == None:
        return node.key

    sum = 0
    if node.left:
        sum += sumOfLeafNodes(node.left)
    if node.right:
        sum += sumOfLeafNodes(node.right)
    return sum


def _findThesumOfpath(node, sum, param):
    if node == None:
        return None

    if param + node.key == sum:
        return node

    left =  _findThesumOfpath(node.left, sum, param + node.key)
    right = _findThesumOfpath(node.right, sum, param + node.key)

    if left:
        return left
    if right:
        return right
    return None

def findThesumOfpath(node, sum = 185):
    return _findThesumOfpath(node, sum, 0)

count = 0
def kthNodeInorderTraversal(node, k):

    if node == None:
        return None

    n1 = kthNodeInorderTraversal(node.left, k)
    global count
    count += 1
    if count == k:
        return node
    n2 = kthNodeInorderTraversal(node.right, k)

    if n1:
        return n1
    if n2:
        return n2

print(sumOfLeafNodes(bst.root))
print( findThesumOfpath(bst.root, 185).key)
print(kthNodeInorderTraversal(bst.root, 10))


