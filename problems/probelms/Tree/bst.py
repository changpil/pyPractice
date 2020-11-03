class Node:
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.left = None
        self.right = None

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

    @staticmethod
    def print(node):
        if node == None:
            return
        q = list()
        q.insert(0, (1, node))
        level = 1
        while len(q):
            nl, node = q.pop()
            if nl != level:
                print("{:50}".format(("---level " + str(level)).rjust(20," ")))
                level += 1
            print(node.key, end=" ")
            if node.left != None:
                q.insert(0, (level+1, node.left))
            if node.right != None:
                q.insert(0, (level+1, node.right))
        print("{:50}".format(("---level " + str(level)).rjust(20," ")))

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
print(BST.isBST(bst.root))
BST.print(bst.root)
print(BST.height(bst.root))
print(BST.isBalanced(bst.root))