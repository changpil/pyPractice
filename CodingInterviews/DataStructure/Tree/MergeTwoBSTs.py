
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None



# # Complete this function and return root of the BST
# def mergeTwoBSTs(root1, root2):
#     a1, a2 = [], []
#     bstToList(root1, a1)
#     bstToList(root2, a2)
#
#     ma = merge(a1, a2)
#
#     return bst(ma, 0, len(ma) -1 )
#
# def bstToList(node, arr):
#     if node == None:
#         return
#     bstToList(node.left, arr)
#     arr.append(node.key)
#     bstToList(node.right, arr)
#
# def merge(a1, a2):
#     ma = []
#     i, j = 0,0
#     while i < len(a1) and j < len(a2):
#         if a1[i] < a2[j]:
#             ma.append(a1[i])
#             i += 1
#         else:
#             ma.append(a2[j])
#             j += 1
#     while i < len(a1):
#         ma.append(a1[i])
#         i += 1
#     while j < len(a2):
#         ma.append(a2[j])
#         j += 1
#     return ma
#
# def bst (arr, i, j):
#     if i > j:
#         return None
#
#     mid = i + (j-i)//2
#
#     newNode = Node(arr[mid])
#
#     newNode.left = bst(arr, i, mid -1)
#     newNode.right = bst(arr, mid + 1, j)
#     return newNode

def ordered(node, store):
    if node == None:
        return
    ordered(node.left, store)
    store.append(node.key)
    ordered(node.right, store)


# Complete this function and return root of the BST

def bst(l, s, e):
    if s > e:
        return None

    mid = (s + e) // 2

    new = Node(l[mid])
    new.left = bst(l, s, mid - 1)
    new.right = bst(l, mid + 1, e)
    return new


def mergeTwoBSTs(root1, root2):
    l1, l2 = [], []
    ordered(root1, l1)
    ordered(root2, l2)
    l1.extend(l2)
    l1.sort()
    return bst(l1, 0, len(l1) - 1)