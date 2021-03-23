import collections
# def levelOrder(root):
#
#     queue = collections.deque()
#     if root:
#         queue.append((0, root))
#     result = []
#
#     while queue:
#         level, node = queue.popleft()
#         if node.left:
#             queue.append((level + 1, node.left))
#         if node.right:
#             queue.append((level + 1, node.right))
#         if len(result) == level:
#             result.append([node.val])
#         else:
#             result[level].append(node.val)
#     return result
# Better Approach
def levelOrder(root):
    queue = collections.deque()
    if root:
        queue.append(root)
    result = []
    while queue:
        levels = []
        levelLength = len(queue)
        for _ in range(levelLength):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            levels.append(node.val)
        result.append(levels)
    return list(result)
