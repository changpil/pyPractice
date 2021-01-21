# How Many Binary Search Trees With n Nodes
# How Many Binary Search Trees With n Nodes?
#
#
#
# Write a function that returns the number of distinct binary search trees that can be constructed with n nodes.
#
# For the purpose of this exercise, do solve the problem using recursion first even if you see some non-recursive approaches.

# def how_many_BSTs(n):
#     arr = [i for i in range(n)]
#     n = helper(arr)
#     return n
#
# def helper(arr):
#     if len(arr) == 1:
#         return 1
#     total= 0
#     for i in range(len(arr)):
#         left, right = 0, 0
#         if not (0 < i < len(arr)):
#             left = helper(arr[:i])
#             right = helper(arr[i + 1:])
#         else:
#             if len(arr[:i]) == len(arr[i + 1:]):
#                 left = helper(arr[:i])
#             #elif len(arr[:i]) < len(arr[i + 1:]):
#             #    right = helper(arr[i + 1:])
#             else:
#                 left = max(helper(arr[:i]), helper(arr[i + 1:]))
#         total += left + right
#     return total

# def how_many_BSTs(n):
#     arr = [i for i in range(n)]
#     return helper(arr, 0, len(arr) - 1)
#
# def helper(arr, i, j):
#     if i >= j:
#         return 0
#     total = 0
#     for mid in range(i , j +1):
#         l = helper (arr,i, mid -1 )
#         r = helper(arr, mid +1, j)
#         total += l + r + 1
#     return total

# Complete the function below.

def how_many_BSTs(n):
    memo = dict()
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    T(n, memo)
    return memo[n]

# # num of element for tree
def T(n, memo):
    if n in memo:
        return memo[n]

    result = 0
    for i in range(1, n+1):
        result += T(i - 1, memo) * T(n - i, memo)
    memo[n] = result
    return memo[n]



print(f"1: {how_many_BSTs(1)}")
print(f"2: {how_many_BSTs(2)}")
print(f"3: {how_many_BSTs(3)}")  # 5
print(f"4: {how_many_BSTs(4)}")  # 14
print(f"5: {how_many_BSTs(5)}")  # 42


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def allBinarySearchTrees(n):
    if n < 0 :
        return []
    output = helper(n, 0, n-1)
    return output

def helper(n, start, end):
    if start > end:
        return [None]

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
    return list

def printNodes(n):
    if n == None:
        return
    print(n.val, end="")
    printNodes(n.left)
    printNodes(n.right)


listNodes = allBinarySearchTrees(3)
for t in listNodes:
    printNodes(t)
    print(end=" ")

print()
listNodes = allBinarySearchTrees(4)
for t in listNodes:
    printNodes(t)
    print(end="  ")

print()
listNodes = allBinarySearchTrees(5)
for t in listNodes:
    printNodes(t)
    print(end="  ")


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


print()
listNodes = allBinarySearchTrees(3)
for t in listNodes:
    printTree(t)
    print()

print()
listNodes = allBinarySearchTrees(4)
for t in listNodes:
    printTree(t)
    print()