# Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?
#
# Example 1:
#
# Input: 2
# Output: List containing root nodes of all structurally unique BSTs.
# Explanation: Here are the 2 structurally unique BSTs storing all numbers from 1 to 2:
#
# Example 2:
#
# Input: 3
# Output: List containing root nodes of all structurally unique BSTs.
# Explanation: Here are the 5 structurally unique BSTs storing all numbers from 1 to 3:


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def nodeToString(node):
    if node == None:
        return ""
    s = str(node.val)

    s += nodeToString(node.left)
    s += nodeToString(node.right)

    return s

def find_unique_trees(n):
  return helper(1, n)

def helper(start, end):
    if start == end :
        return [TreeNode(start)]

    if start > end:
        return [None]

    result = []

    for mid in range(start, end + 1):
        nodelefts = helper(start, mid -1)
        noderights = helper(mid + 1, end)

        for nodeleft in nodelefts:
            for noderight in noderights:
                node = TreeNode(mid)
                node.left = nodeleft
                node.right = noderight
                result.append(node)
    return result

def main():
  print("Total trees: ")
  nodes  = find_unique_trees(2)
  for node in nodes:
      print(nodeToString(node))


  print("Total trees: ")
  nodes  = find_unique_trees(3)
  for node in nodes:
      print(nodeToString(node))

main()