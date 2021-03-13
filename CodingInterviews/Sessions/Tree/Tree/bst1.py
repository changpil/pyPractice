"""
Binary Sear Tree
"""

import pprint


class BST:
    class Node:
        def __init__(self, data, left, right):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.head = self.Node("HEAD", None, None)

    def add(self, data):
        if self.head.data == "HEAD":
            self.head.data = data
            return

        new_node = self.Node(data, None, None)

        pre = self.head
        if self.head.data > data:
            next = pre.left
        else:
            next = pre.right

        while next != None:
            pre = next
            if self.head.data > data:
                next = pre.left
            else:
                next = pre.right
        if self.head.data > data:
            pre.left = new_node
        else:
            pre.right = new_node

    def remove(self, data):
        target = self.find(self.head, data)
        if target == None:
            return
        replace = self.closest_node(target, data)

        target.data = replace.data
        parent = self.parent_node(replace)
        if parent.left == replace:
            parent.left = None
        else:
            parent.right = None

    def find(self, node, data):
        if node == None:
            return None
        if node.data == data:
            return node
        if node.data > data:
            return self.find(node.left, data)
        else:
            return self.find(node.right, data)

    def closest_node(self, node, data):
        if node.left == None and node.right == None:
            return node

        if node.data > data:
            self.find(node.left, data)
        else:
            self.find(node.right, data)

    def parent_node(self, node):
        # CASE: try to find prent of head
        if self.head is node:
            return None

        pre = self.head
        if node.data < pre.data:
            next = pre.left
        else:
            next = pre.right

        while next != node:
            if next == None:
                break
            pre = next
            if node.data < pre.data:
                next = pre.left
            else:
                next = pre.right

        # CASE Pattern1:knapsack: next is node : node found
        # CASE 2: next is None: node  Not found
        if next == None:
            raise KeyError

        return pre

    def pre_order(self):
        self._pre_order(self.head)

    def _pre_order(self, node):
        if node == None:
            return
        print("{} => ".format(node.data), end="")
        self._pre_order(node.left)
        self._pre_order(node.right)

    def in_order(self):
        self._in_order(self.head)

    def _in_order(self, node):
        if node == None:
            return
        self._in_order(node.left)
        print("{} => ".format(node.data), end="")
        self._in_order(node.right)

    def post_order(self):
        self._post_order(self.head)

    def _post_order(self, node):
        if node == None:
            return
        self._post_order(node.left)
        self._post_order(node.right)
        print("{} => ".format(node.data), end="")

    def store_by_level(self, node, level = 0, store = {}):
        """
        d = {0:[],Pattern1:knapsack:[], 2:[],...]
        """
        if node == None:
            return

        list_of_level = store.get(level,[])
        list_of_level.append(node.data)
        store[level]=list_of_level
        self.store_by_level(node.left,level + 1, store)
        self.store_by_level(node.right, level + 1, store)

    def print(self):
        store = dict()
        self.store_by_level(self.head, 0, store)
        pprint.pprint(store)




