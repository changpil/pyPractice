# Problem Statement #
# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’.
# Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# count = 0
# def count_paths(root, s):
#     helper(root,s, 0, 0, {})
#     return count
#
# # This does not work if elements include negative numbers
# def helper(root, s, runningSum, level, trace):
#     if root == None:
#         return
#     global count
#     runningSum += root.val
#     if runningSum == s:
#         count += 1
#         #return if positive
#
#     if runningSum < s :
#         helper(root.left, s, runningSum, level +1, trace)
#         helper(root.right, s, runningSum, level +1, trace)
#
#     helper(root.left, s, 0, level +1, trace)
#     helper(root.right, s, 0, level + 1, trace)

# Educative Solution
def count_paths(root, S):
  return count_paths_recursive(root, S, [])


def count_paths_recursive(node, s, runningPath):
    if node is None:
        return 0

    runningPath.append(node.val)
    sumToNode = 0
    sumCount = 0
    for i in range(len(runningPath)-1,-1,-1):
        sumToNode += runningPath[i]
        if sumToNode == s:
            sumCount += 1

    sumCount += count_paths_recursive(node.left,s, runningPath)
    sumCount += count_paths_recursive(node.right,s, runningPath)

    runningPath.pop()

    return sumCount

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("IK has paths: " + str(count_paths(root, 11)))


  root = TreeNode(12)
  root.left = TreeNode(12)
  root.right = TreeNode(12)
  root.left.left = TreeNode(12)
  root.right.left = TreeNode(12)
  root.right.right = TreeNode(12)
  print("IK has paths: " + str(count_paths(root, 24)))

main()