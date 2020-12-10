from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# runningpredecessor = None
# predecessor = None
#
# def findPredecesor(root, key):
#     global runningpredecessor, predecessor
#
#     if root == None or predecessor != None:
#         return
#
#     findPredecesor(root.left, key)
#
#     if root.val == key:
#         predecessor = runningpredecessor
#         return
#
#     runningpredecessor = root
#
#     findPredecesor(root.right, key)


def findPredecesor(root, key, prob):

    if root == None or prob.predecessor != None:
        return

    findPredecesor(root.left, key, prob)

    if root.val == key:
        prob.predecessor = prob.runningpredecessor

    prob.runningpredecessor = root
    findPredecesor(root.right, key, prob)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(19)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(26)

    # findPredecesor(root, 12)
    # print(predecessor.val)
    #
    # runningpredecessor = None
    # predecessor = None
    # findPredecesor(root, 7)
    # print(predecessor.val)
    # runningpredecessor = None
    # predecessor = None
    # findPredecesor(root, 15)
    # print(predecessor.val)

    class Prob:
        predecessor = None
        runningpredecessor = None

        def clear(cls):
            cls.predecessor = None
            cls.runningpredecessor = None

    prob = Prob()
    findPredecesor(root, 12, prob)
    print(prob.predecessor.val)

    prob.clear()

    findPredecesor(root, 15, prob)
    print(prob.predecessor.val)

main()