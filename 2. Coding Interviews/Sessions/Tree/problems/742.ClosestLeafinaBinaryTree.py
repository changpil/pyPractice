"""
Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.

Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)

Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
Example 2:

Input:
root = [1], k = 1
Output: 1

Explanation: The nearest leaf node is the root node itself.
Example 3:

Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
"""

import collections
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findClosestLeaf(self, root, k):
    queue = collections.deque()
    queue.append(root)
    parents = {root.val:None}
    kNode = None
    while queue:
        node = queue.popleft()
        if node.val == k:
            kNode = node
        if node.left:
            parents[node.left.val] = node
            queue.append(node.left)
        if node.right:
            parents[node.right.val] = node
            queue.append(node.right)
    minLevel = minLeafLevel(kNode)
    parentlevel = 2
    parentNodes = []
    target = k
    while parents[target] != None:
        pNode = parents[target]
        if pNode.left and pNode.left.val == target and pNode.right:
            parentNodes.append(pNode.right)
        elif pNode.right and pNode.right.val == target and pNode.left:
            parentNodes.append(pNode.left)
        target = pNode.val

    for node in parentNodes:
        tmpl, tmpv = minLeafLevel(node)
        tmpl += parentlevel
        if minLevel[0] > tmpl:
            minLevel = (tmpl, tmpv)
        parentlevel += 1
    return minLevel[1]

def minLeafLevel(node):
    level = 0
    queue = collections.deque()
    queue.append(node)
    while queue:
        levelNodes = len(queue)
        for _ in range(levelNodes):
            node = queue.popleft()
            if node.left == None and node.right == None:
                return level, node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1

