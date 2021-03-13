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

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.cur = root
        self.stack = []

    def __iter__(self):
        return self

    def __next__(self):
        """
        :rtype: int
        """
        # while self.cur and self.stack: Bug
        while self.cur or self.stack:
            while self.cur:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            self.cur = self.stack.pop()
            next = self.cur.val
            self.cur = self.cur.right
            return next
        raise StopIteration

root = TreeNode(7, TreeNode(3),TreeNode(15, TreeNode(9), TreeNode(20)))

for num in BSTIterator(root):
    print(num)