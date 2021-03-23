class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
# def addOneRow(root: TreeNode, v: int, d: int) -> TreeNode:
#     queue = collections.deque()
#     if root:
#         queue.append(root)
#     if d == 1:
#        return TreeNode(v, root)
#     level = 1
#     while queue:
#         if d == 1:
#             return TreeNode(v, root)
#         numOfElems = len(queue)
#         parents = queue.copy()
#         for _ in range(numOfElems):
#             node = queue.popleft()
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         level += 1
#         if level == d:
#             for parent in parents:
#                 if parent.left:
#                     newNode = TreeNode(v, parent.left,None)
#                     parent.left = newNode
#                 if parent.right:
#                     newNode = TreeNode(v, None, parent.right)
#                     parent.right = newNode
#             return root
#     return root

def addOneRow(root, v, d):
    if d == 1:
        return TreeNode(v, root)
    queue = collections.deque()
    if root:
        queue.append(root)
    level = 1
    inserted = False
    while queue:
        numOfElems = len(queue)
        for _ in range(numOfElems):
            node = queue.popleft()
            lastNode = node
            if level < d - 1:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                #if node.left:
                newNode = TreeNode(v, node.left, None)
                node.left = newNode
                #if node.right:
                newNode = TreeNode(v, None, node.right)
                node.right = newNode
                inserted = True
        if inserted:
            return root
        level += 1
    return root

def printTree(node):
    q =collections.deque()
    q.append(node)
    while q:
        for node in q:
            print(node.val, end = " ")
        print()
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
printTree(root)
print()
root = addOneRow(root, 1, 4)
printTree(root)
