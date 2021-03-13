"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

"""
import collections
def maxLevelSum(root):
    queue = collections.deque()
    if root:
        queue.append(root)
    level = 0
    maxi, maxlevel = root.val, 1
    while queue:
        levelLength = len(queue)
        level += 1
        total = 0
        for _ in range(levelLength):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            total += node.val
        if total > maxi:
            maxi, maxlevel = total, level
    return maxlevel