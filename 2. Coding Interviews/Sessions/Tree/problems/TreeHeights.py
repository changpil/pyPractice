class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Bottom-Up
def getTreeHeight(node):
    # edges is heights
    if node.left == None and node.right == None:
        return 0
    left, right = 0, 0
    if node.left:
        left = getTreeHeight(node.left) + 1
    if node.right:
        right = getTreeHeight(node.right) + 1
    return max(left, right)

#Top-Down
def getTreeHeight2(node):
    height = [0]
    foo(node, 0, height)
    return height[0]

def foo(node, h, height):
    if node.left == None and node.right == None:
        #height[0] = max(height[0], h + 1)
        height[0] = max(height[0], h)
        return
    if node.left:
        foo(node.left, h+1, height)
    if node.right:
        foo(node.right, h+1, height)

import collections
def height(root):
    queue = collections.deque()
    queue.append(root)
    height = -1
    while queue:
        n = len(queue)
        height += 1
        while n:
            node = queue.popleft()
            left =  node.left
            right = node.right
            if left:
                queue.append(left)
            if right:
                queue.append(right)
            n -= 1
    return height

root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
print(getTreeHeight(root))
print(getTreeHeight2(root))