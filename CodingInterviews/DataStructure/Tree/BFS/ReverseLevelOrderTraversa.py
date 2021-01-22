from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = deque()
    queue = deque()
    if root == None:
        return result
    queue.append(root)

    while queue:
        sizeOfLevel = len(queue)
        levelarr = []
        for _ in range(sizeOfLevel):
            tmp = queue.popleft()
            levelarr.append(tmp.val)
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)

        result.appendleft(levelarr)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()