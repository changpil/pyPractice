from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

successor = None
foundKey = False

def findSuccessor(root, key):
    global successor, foundKey
    if root == None:
        return
    findSuccessor(root.left, key)
    if foundKey and successor == None:
        successor = root
    if root.val == key:
        foundKey = True
    findSuccessor(root.right, key)

def predecessor(root, key):
    prev = [None] # Prev, Cur
    return predecessorHelper(prev, root, key)

def predecessorHelper(prev, cur, key):

    if cur == None:
        return None
    re = predecessorHelper(prev, cur.left, key)
    if re:
        return re
    if cur.val == key:
        return prev[0]
    prev[0] = cur
    return predecessorHelper(prev, cur.right, key)

def successor(root, key):
    prev = [None] # Prev, Cur
    return successorHelper(prev, root, key)

#InOrder Sucessor
# def successorHelper(prev, cur, key):
#
#     if cur.left:
#         re = successorHelper(prev, cur.left, key)
#         if re:
#             return re
#
#     if prev[0] and prev[0].val == key:
#         return cur
#     prev[0] = cur
#
#     if cur.right:
#         return successorHelper(prev, cur.right, key)

#Preorder Successor
# def successorHelper(prev, cur, key):
#     if prev[0] and prev[0].val == key:
#         return cur
#     prev[0] = cur
#     if cur.left:
#         re = successorHelper(prev, cur.left, key)
#         if re:
#             return re
#
#     if cur.right:
#         return successorHelper(prev, cur.right, key)

#PostOrder Successor
def successorHelper(prev, cur, key):

    if cur.left:
        re = successorHelper(prev, cur.left, key)
        if re:
            return re

    if cur.right:
        re = successorHelper(prev, cur.right, key)
        if re:
            return re

    if prev[0] and prev[0].val == key:
        return cur
    prev[0] = cur

def main():
    #global successor, foundKey
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(19)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(26)

    #findSuccessor(root, 12)
    #print(successor.val)
    #successor, foundKey = None, None
    #findSuccessor(root, 15)
    #print(successor.val)

    #print(predecessor(root, 1).val) # None
    # print(predecessor(root,12).val)
    # print(predecessor(root, 15).val)
    # print(predecessor(root, 26).val)

    try:
        #print(successor(root, 12).val)
        print(successor(root, 7).val)
        print(successor(root, 1).val)
        print(successor(root, 19).val)
        print(successor(root, 15).val)
        print(successor(root, 26).val)
    except:
        print("Except")
main()