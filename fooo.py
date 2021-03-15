class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def bst(arr, i, j):
    if i > j:
        return None

    mid = (i + j) // 2

    n = Node(arr[mid])
    n.left = bst(arr, i, mid - 1)
    n.right = bst(arr, mid + 1, j)

    return n


def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.key, end= " ")
    inorder(root.right)


def merge(a, b):
    i, j = 0, 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1
    return c


l = [1,4, 5, 9]
r = [2, 8, 10]
l = merge(l, r)
print(l)
root = bst(l, 0, len(l) -1)
inorder(root)