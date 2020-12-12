class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

from collections import deque

def traverse(root):
    result = []
    queue = deque()
    queue.append(root)
    level = 0
    while queue:
        sizeOfLevel = len(queue)
        levelOrder = deque()
        foo = None
        if level%2 == 0:
            foo = levelOrder.append
        else:
            foo = levelOrder.appendleft

        for _ in range(sizeOfLevel):
            tmp = queue.pop()
            foo(tmp.val)
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)

        result.append(list(levelOrder))
        level += 1
    return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()