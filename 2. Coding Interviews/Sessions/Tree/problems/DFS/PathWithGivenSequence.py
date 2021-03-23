# Problem Statement #
# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
#

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  return _find_path(root, sequence, 0)

def _find_path(root, arr, i):
    if root.left == None and root.right == None:
        if len(arr) -1 == i and root.val == arr[i]:
            return True
        else:
            return False

    if i >= len(arr):
        return False

    if root.val != arr[i]:
        return False

    l, r = False, False

    if root.left:
        l = _find_path(root.left, arr, i+1)
    if root.right:
        r = _find_path(root.right, arr, i+1)

    return l or r



def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("IK has path sequence: " + str(find_path(root, [1, 0, 2])))
  print("IK has path sequence: " + str(find_path(root, [1, 1, 6])))
  print("IK has path sequence: " + str(find_path(root, [1, 1, 8])))

main()