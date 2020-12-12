
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def tree_right_view(root):
    result = []
    queue = deque()
    queue.append(root)

    while queue:
        size = len(queue)
        tmp = None
        for i in range(size):
            tmp = queue.popleft()
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)

        result.append(tmp)

    return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')


main()






