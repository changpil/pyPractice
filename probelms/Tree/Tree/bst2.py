class Node:
    def __init__(self, key = None, item = None, left = None, right = None, parent = None):
        self.key = key
        self.item = item
        self.left = left
        self.right = right
        self.parent =parent

class BST:
    def __init__(self):
        self.root = None

    def add(self, key, item=None):
        a_node = Node(key, item)
        if self.root == None:
            self.root = a_node
            return

        p = self.root
        pp = self.root
        while pp:
            p = pp
            if pp.key < key:
                pp = pp.right
            else:
                pp = pp.left

        if p.key < key:
             p.right = a_node
        else:
            p.left = a_node

    def remove(self, key):

        p = self.root
        pp = self.root

        while pp and key != pp.key:
            p = pp
            if pp.key < key:
                pp = pp.right
            else:
                pp = pp.left

        if pp == None:
            return

        if pp.left == None and pp.right == None:
            if p.left and p.left.key == key:
                p.left = None
            else:
                p.right = None

        else:
            t= pp
            if t.left:
                target, p_target = self._rightmost(t.left, t)
                pp.key, pp.item = target.key, target.item
                p_target.left = None
            else:
                target, p_target = self._leftmost(t.right, t)
                pp.key, pp.item = target.key, target.item
                p_target.right = None

    def _leftmost(self, pp, p):
        while pp.left:
            p = pp
            pp = pp.left
        return pp, p

    def _rightmost(self, pp, p):
        while pp.right:
            p = pp
            pp = pp.right
        return pp, p

    ##Wong logic
    """
    @staticmethod
    def isBST(node):
        if node == None:
            return True
        key = node.key

        result = True
        if node.left and node.left.key > key:
            result = False
        if node.right and node.right.key < key:
            result = result and False
        return result and BST.isBST(node.left) and BST.isBST(node.right)
        """

    @staticmethod
    def isBST(node, leftkey = -10000, rightkey = 10000):
        if node == None:
            return True
        key = node.key

        result = True
        if not leftkey < key < rightkey:
            result = False
            return result

        if node.left:
            result = result and BST.isBST(node.left, leftkey, node.key)
        if node.right:
            result = result and BST.isBST(node.right, node.key, rightkey)

        return result

    @staticmethod
    def isBalanced(node):
        if node == None:
            return True

        if abs(BST.height(node.left) - BST.height(node.right)) > 1:
            return False

        return BST.isBalanced(node.left) and BST.isBalanced(node.right)

    @staticmethod
    def height(node):
        if node == None:
            return 0

        return 1 + max(BST.height(node.left), BST.height(node.right))

    @staticmethod
    def print(node):
        lines, _, _, _ = BST._display_aux(node)
        for line in lines:
            print(line)

    @staticmethod
    def _display_aux(node):
        """
        Returns list of strings, width, height,
        and horizontal coordinate of the root.
        """
        # No child.
        if node.right is None and node.left is None:
            line = str(node.key)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = BST._display_aux(node.left)
            s = str(node.key)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            final_lines = [first_line, second_line] + shifted_lines
            return final_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = BST._display_aux(node.right)
            s = str(node.key)
            u = len(s)
            #        first_line = s + x * '_' + (n - x) * ' '
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            final_lines = [first_line, second_line] + shifted_lines
            return final_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = BST._display_aux(node.left)
        right, m, q, y = BST._display_aux(node.right)
        s = '%s' % node.key
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

bst = BST()
bst.add(50)
bst.add(25)
bst.add(75)
bst.add(1)
bst.add(30)
bst.add(60)
bst.add(90)
bst.add(100)
bst.add(200)
#bst.root.right.left.key = 30
BST.print(bst.root)

print(f"Is BST?: {BST.isBST(bst.root)}")
print(f"height: {BST.height(bst.root)}")
print(f"Is Balanced?: {BST.isBalanced(bst.root)}")
