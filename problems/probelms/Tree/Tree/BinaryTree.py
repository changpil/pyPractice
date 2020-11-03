import queue

class BinaryTree:
    class Node:
        def __init__(self, obj, left=None, right=None):
            self.obj=obj
            self.left=left
            self.right=right

    def __init__(self, obj, left=None, right=None):
        self.head = self.Node(obj,left, right)

    def add_left(self, obj):
        self.head = self.Node(obj,self.head, None)

    def add_right(self, obj):
        self.head = self.Node(obj, None, self.head)

    def __str__(self):
        return self.tree()

    @staticmethod
    def pre_order(node):
        if node is None:
            return
        print(node.obj)
        BinaryTree.pre_order(node.left)
        BinaryTree.pre_order(node.right)

    @staticmethod
    def in_order(node):
        if node is None:
            return
        BinaryTree.in_order(node.left)
        print(node.obj,end="")
        BinaryTree.in_order(node.right)

    def add(self, obj):
        q = queue.Queue()
        q.put(self.head)
        while not q.empty():
            temp = q.get()
            if temp.left == None:
                temp.left = BinaryTree.Node(obj)
            else:
                q.add(temp.left)

            if temp.right == None:
                temp.right = BinaryTree.Node(obj)
            else:
                q.add(temp.right)

    def remove(self, obj):
        pass

    def height(self):
        pass

    def printGivenLevel(self, level):
        pass

    def print(self):
        q = queue.Queue()
        q.put(self.head)
        while not q.empty():
            temp = q.get()
            print(temp.obj,end="")
            if temp.left is not None:
                q.put(temp.left)
            if temp.right is not None:
                q.put(temp.right)


bt =  BinaryTree("a")
bt.head.left = BinaryTree.Node("b")
bt.head.right = BinaryTree.Node("c")
bt.head.left.left = BinaryTree.Node("d")
bt.head.left.right = BinaryTree.Node("e")
bt.head.right.left = BinaryTree.Node("f")
bt.head.right.right = BinaryTree.Node("g")
BinaryTree.in_order(bt.head)
print()
bt.print()