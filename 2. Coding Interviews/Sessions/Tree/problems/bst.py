class Stack:
    def __init__(self):
        self.s = list()
    def push(self, item):
        self.s.append(item)
    def pop(self):
        return self.s.pop()
    def size(self):
        return len(self.s)
    def top(self):
        return self.s[-1]
    def isEmpty(self):
        return True if len(self.s) == 0 else False
    def __str__(self):
        s = ("-" * 5 + " stack " + "-" * 5 + "\n")
        for i in range(len(self.s)):
            s += f" --> {self.s[i]}"
        s += "\n" + "-" * 20 + "\n"
        return s

class Node:
    def __init__(self, val, data = None, left =None, right = None, parent= None ):
        self.val = val
        self.data = data
        self.left = left
        self.right = right

    # Iterative
    def add_node(self, val, data = None, left = None, right = None, parent= None):
        cur, parent = self, None
        while cur:
            parent = cur
            if val <= cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if val <= parent.val:
            parent.left = Node(val,parent=parent)
        else:
            parent.right = Node(val, parent=parent)

    def find_closest_left(self):
        if self.left == None:
            None, None
        cur, parent = self.left, self
        while cur.right:
            parent = cur
            cur= cur.right
        return parent, cur

    def find_closest_right(self):
        if self.right == None:
            None, None
        cur, parent = self.right, self
        while cur.left:
            parent = cur
            cur= cur.left
        return parent, cur

    # Iterative
    def delete_node(self, val):
        cur, parent  = self, None
        while cur:
            if cur.val == val:
                break
            parent = cur
            if val <= cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if cur == None:
            return False

        if cur.left == None and cur.right == None:
            if id(parent.left) == id(cur):
                parent.left = None
            else:
                parent.right = None
        elif cur.left == None and cur.right!= None:
            if id(parent.left) == id(cur):
                parent.left = cur.right
            else:
                parent.right = cur.right
        elif cur.left != None and cur.right == None:
            if id(parent.left) == id(cur):
                parent.left = cur.left
            else:
                parent.right = cur.left
        else:
            if parent == None or id(parent.left) == id(cur):
                tmp_p, tmp = cur.find_closest_left()
                cur.val, tmp.val = tmp.val, cur.val
                if id(tmp_p.left) == id(cur):
                    tmp_p.left = None
                else:
                    tmp_p.right = None
            else:
                tmp_p, tmp = cur.find_closest_right()
                cur.val, tmp.val = tmp.val, cur.val
                if id(tmp_p.left) == id(cur):
                    tmp_p.left = None
                else:
                    tmp_p.right = None
        return True

    def recursive_add_node(self, val):
        pass

    def recursive_remove_node(self):
        pass

    def __str__(self):
        return f"{self.val}"
class BST:
    def __init__(self, val = None):
        if val == None:
            self.root = None
        else:
            self.root = Node(val)

    def add(self, val):
        if self.root == None:
            self.root = Node(val)
            return
        self.root.add_node(val)

    def delete(self, val):
        if self.root == None:
            return
        if self.root.val == val and self.root.left == None and self.root.right == None:
            self.root = None
            return
        self.root.delete_node(val)

    def search(self, val):
        cur = self.root
        while cur:
            if val == cur.val:
                return True
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def in_order(self):
        cur = self.root
        s = Stack()
        _str = ""
        while cur or not s.isEmpty():
            if cur:
                s.push(cur)
                cur = cur.left
            else:
                cur = s.pop()
                _str += f"{cur.val} "
                cur = cur.right
        return _str

    def pre_order(self):
        cur = self.root
        s = Stack()
        _str = ""
        while cur or not s.isEmpty():
            if cur:
                _str += f"{cur.val} "
                if cur.right:
                    s.push(cur.right)
                cur = cur.left
            else:
                cur = s.pop()
        return _str

    def post_order(self):
        s1 = Stack()
        s2 = Stack()
        _str = ""
        s1.push(self.root)
        while not s1.isEmpty():
            node = s1.pop()
            s2.push(node)
            if node.left:
                s1.push(node.left)
            if node.right:
                s1.push(node.right)

        while not s2.isEmpty():
            _str += f"{s2.pop().val} "
        return _str

    def __str__(self):
        lines, _, _, _ = self._display_aux(self.root)
        return "\n".join(lines)

    def _display_aux(self, node):
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
            lines, n, p, x = self._display_aux(node.left)
            s = str(node.val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            final_lines = [first_line, second_line] + shifted_lines
            return final_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = str(node.val)
            u = len(s)
            #        first_line = s + x * '_' + (n - x) * ' '
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            final_lines = [first_line, second_line] + shifted_lines
            return final_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
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

bst = BST()
bst.add(50)
bst.add(25)
bst.add(75)
#bst.add(Pattern1:knapsack)
bst.add(30)
bst.add(60)
bst.add(90)
bst.add(100)
bst.add(200)
print(bst)

# bst.delete(200)
# print(bst)
# bst.delete(90)
# print(bst)
#
# bst.add(55)
# print(bst)
# bst.delete(60)
# print(bst)
#
# bst.delete(25)
# print(bst)
#
# bst.delete(75)
# print(bst)

# print(bst.search(50))
# bst.delete(50)
# print(bst)
#
# print(bst.search(50))
#
# print(bst.in_order())
# print(bst.pre_order())
# print(bst.post_order())