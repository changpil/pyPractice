"""
Write a function which takes as input an integer n and returns all distinct binary trees with n nodes
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def allBinaryTrees(n):
    if n < 0 :
        return []
    output = helper(n, 0, n-1)
    return output

def helper(n, start, end):
    if start > end:
        return [None]
    # if start < 0:
    #     return [None]
    # if end >= n:
    #     return [None]
    if start == end:
        newNode = TreeNode(start)
        return [newNode]

    list = []

    for top in range(start, end + 1):
        leftNodeList = helper(n, start, top - 1)
        rightNodeList = helper(n, top + 1, end)

        for l in leftNodeList:
            for r in rightNodeList:
                newNode = TreeNode(top)
                newNode.left = l
                newNode.right = r
                list.append(newNode)

        rightNodeList = helper(n, start, top - 1)
        leftNodeList = helper(n, top + 1, end)
        for l in leftNodeList:
            for r in rightNodeList:
                newNode = TreeNode(top)
                newNode.left = l
                newNode.right = r
                list.append(newNode)

    return list

def printTree(n):
        lines, _, _, _ = _printTree(n)
        print("\n".join(lines))


def _printTree(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # No child.
    if node.right is None and node.left is None:
        line = str(node.val)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.right is None:
        lines, n, p, x = _printTree(node.left)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.left is None:
        lines, n, p, x = _printTree(node.right)
        s = str(node.val)
        u = len(s)
        #        first_line = s + x * '_' + (n - x) * ' '
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _printTree(node.left)
    right, m, q, y = _printTree(node.right)
    s = '%s' % node.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
                 '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
                  (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

def printNodes(n):
    if n == None:
        return
    print(n.val, end="")
    printNodes(n.left)
    printNodes(n.right)

listNodes = allBinaryTrees(3)
for t in listNodes:
    printNodes(t)
    print(end = " ")
print()
for t in listNodes:
    printTree(t)
    printNodes(t)
    print()

print()
# listNodes = allBinaryTrees(4)
# for t in listNodes:
#     printTree(t)
#     print(end = " ")
