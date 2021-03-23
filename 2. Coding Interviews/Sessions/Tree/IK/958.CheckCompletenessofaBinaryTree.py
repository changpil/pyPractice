import collections
# def isCompleteTree(root):
#     q = collections.deque()
#     if root:
#         q.append(root)
#     while q:
#         for _ in range(len(q)):
#             node = q.popleft()
#             if node == None:
#                 if not isCompleteTree(q):
#                     return False
#                 else:
#                     return True
#             q.append(node.left)
#             q.append(node.right)
#
#     return True
#
#
def isCompleteTree(q):
    for i in range(len(q)):
        if q[i] != None:
            return False
    return True

def isCompleteTree(root):
    q = collections.deque()
    if root:
        q.append((1, root))
    expectedid = 1
    while q:
        for _ in range(len(q)):
            id, node = q.popleft()
            if id != expectedid:
                return False
            else:
                expectedid += 1
            if node.left:
                q.append((id*2, node.left))
            if node.right:
                q.append((id*2+1, node.right))
    return True