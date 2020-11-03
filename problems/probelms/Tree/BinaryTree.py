class Node:
    def __init__(self, key = None):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, item):
        if self.root == None:
            self.root = Node(item)
            return

        a_node = Node(item)
        q = list()
        q.insert(0, self.root)
        while len(q):
            node = q.pop()
            if node.left == None:
                node.left = a_node
                return
            elif node.right == None:
                node.right = a_node
                return
            if node.left != None:
                q.insert(0,node.left)
            if node.right != None:
                q.insert(0, node.right)

    def remove(self, item):
        if self.root == None:
            return False
        q = list()
        q.insert(0, self.root)

        while len(q):
            node = q.pop()
            if node.left.val == item:
                tmp = node.left.right
                node.left = node.left.left
                if tmp:
                    self.add(tmp)
                return
            elif node.right.val == item:
                tmp = node.right.left
                node.right = node.right.right
                if tmp:
                    self.add(tmp)
                return
            if node.left:
                q.insert(0,node.left)
            if node.right:
                q.insert(0, node.right)


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
            print(node.val, end=" ")
            if node.left != None:
                q.insert(0, (level+1, node.left))
            if node.right != None:
                q.insert(0, (level+1, node.right))
        print("{:50}".format(("---level " + str(level)).rjust(20," ")))



bt = BinaryTree()
bt.add("+")
bt.add("-")
bt.add("*")
bt.add("/")
bt.add("5")
bt.add("5")
bt.add("5")
bt.add("5")
bt.add("5")
BinaryTree.print(bt.root)
bt.remove("5")
print("-------bt")
BinaryTree.print(bt.root)