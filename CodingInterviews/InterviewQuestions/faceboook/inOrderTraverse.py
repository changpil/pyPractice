# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class InorderIterator(object):
#
#
#     def __init__(self, root):
#         """
#         :type root: TreeNode
#         """
#         self.cur = root
#         self.stack = []
#
#     def next(self):
#         """
#         :rtype: int
#         """
#         # while self.cur and self.stack: Bug
#         while self.cur or self.stack:
#             while self.cur:
#                 self.stack.append(self.cur)
#                 self.cur = self.cur.left
#             self.cur = self.stack.pop()
#             next = self.cur.val
#             self.cur = self.cur.right
#             return next
#
#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         if self.cur == None and not self.stack:
#             return False
#         return True

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class BSTIterator(object):
#
#     def __init__(self, root):
#         """
#         :type root: TreeNode
#         """
#         self.cur = root
#         self.stack = []
#
#     def next(self):
#         """
#         :rtype: int
#         """
#         # while self.cur and self.stack: Bug
#         while self.cur or self.stack:
#             while self.cur:
#                 self.stack.append(self.cur)
#                 self.cur = self.cur.left
#             self.cur = self.stack.pop()
#             next = self.cur.val
#             self.cur = self.cur.right
#             return next
#
#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         if self.cur == None and not self.stack:
#             return False
#         return True

# root = TreeNode(7, TreeNode(3),TreeNode(15, TreeNode(9), TreeNode(20)))
# i = BSTIterator(root)
# while i.hasNext():
#     print(i.next())


# Without memory
class InorderIterator(object):
    def __init__(self, root):
        self.cur = root
        self.prev = None

    def next(self):
        if self.cur == None:
            self.cur= None
            return
        cur = self.cur
        self.cur = self.cur.left
        self.next()

        yield cur.val

        self.cur = cur.right
        self.next()


    def hasNext(self):
        if self.cur == None:
            return False
        return True



root = TreeNode(7, TreeNode(3),TreeNode(15, TreeNode(9), TreeNode(20)))
i = InorderIterator(root)
while i.hasNext():
    print(i.next())
