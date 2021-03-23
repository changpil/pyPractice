# Templeate
### Tree BFS
```
def bfs(root):
    q = collections.deque()
    q.append(root)
    while q:
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

def bfs(root):
    q = collections.deque()
    q.append(root)
    while q:
        numnodes = len(q)
        for _ in range(numnodes):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            result.append(node.val)
``` 

### Graph BFS
```
def bfs(graph, source):
    visited = set()
    q = collections.deque()
    q.append(source)
    visited.add(source)
    while q:
        for neighbor in adjlist[source]:
            if neighbor not in visited:
                q.append(neighbor)
```


### Session 1
102. Binary Tree Level Order Traversal (medium)
107. Binary Tree Level Order Traversal II (easy)
429. N-ary Tree Level Order Traversal (easy)
103. Binary Tree Zigzag Level Order Traversal (medium)
637. Average of Levels in Binary Tree (easy)
515. Find Largest Value in Each Tree Row (medium)
199. Binary Tree Right Side View (medium)
111. Minimum Depth of Binary Tree (easy)
104. Maximum Depth of Binary Tree (easy)
559. Maximum Depth of N-ary Tree (easy)
1161. Maximum Level Sum of a Binary Tree (medium) 
965. Univalued Binary Tree (easy)
993. Cousins in Binary Tree (easy)
116. Populating Next Right Pointers in Each Node (medium)
623. Add One Row to Tree (medium)
662. Maximum Width of Binary Tree (medium)
958. Check Completeness of a Binary Tree (medium)
101. Symmetric Tree (easy)

### Tree DFS template
```buildoutcfg

def dfs(node):
    if node.left:
        dfs(node.left)
    if node.right:
        dfs(node.right)    
        
```
Handle a null tree as a special case outside of DFS code...

```buildoutcfg
def dfs (root):
    if not root:
        return
    def foo(node):
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right) 
    foo(root) 
```
Add a base case to the recursion (if the node is a leaf node).
```buildoutcfg
def dfs (root):
    if not root:
        return
    def foo(node):
        if node.left == None and node.right == None:
        # Base case answer generated here
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right) 
    foo(root)  
```

Alternate template that allows DFS to be called on a null node
```buildoutcfg
def dfs(node):
    if not node:
        return
        
    dfs(node.left)
    dfs(node.right
```

### BFS allPathsOfABinaryTree
```buildoutcfg
def allPathsOfABinaryTree(root):
    if not root:
        return []
    result = []
    q = collections.deque((root, [])])
    while q:
        node, slate = q.popleft()
        slate = slate + [node.val]
        if node.left == None and node.right == None:
            result.append(slate)
            continue
        if node.left:
            q.append((node.left, slate))
        if node.right:
            q.append((node.right, slate))
            
    return result
    
    
         
```


### Top-Down DFS allPathsOfABinaryTree
```buildoutcfg
def allPathsOfABinaryTree(root):
    if not root:
        return []
        
    result = []
    def dfs(node, slate):
        slate.append(node.val)
        
        if node.left == None and node.right == None:
            result.append(slate.copy())
            
        if node.left:
            dfs(node.left, slate)
        if node.right:
            dfs(node.right, slate)
    dfs(root, [])
    return result
```
### Bottom-Up DFS
```buildoutcfg

def find_height(root):
    if not root:
        return 0
    def dfs(node):
        if len(node.chilren) == 0:
            return 0
        nodeheight = 0
        for child in node.children:
            nodeheight = max(nodeheight, 1 + dfs(child))
        return nodeheight
    return dfs(root)
        
```
### Session 2
112. Path Sum (easy)
113. Path Sum II (medium)
298. Binary Tree Longest Consecutive Sequence (medium)
437. Path Sum III (easy)
226. Invert Binary Tree (easy)
559. Maximum Depth of N-ary Tree (easy)
543. Diameter of Binary Tree (easy)
250. Count Univalue Subtrees (medium)
236. Lowest Common Ancestor of a Binary Tree (medium)
98. Validate Binary Search Tree (medium)
687. Longest Univalue Path (easy)


### Session 3
513. Find Bottom Left Tree Value (medium)
314. Binary Tree Vertical Order Traversal (medium)
987. Vertical Order Traversal of a Binary Tree (medium)
545. Boundary of Binary Tree (medium)
156. Binary Tree Upside Down (medium)
110. Balanced Binary Tree (easy)
98. Validate Binary Search Tree (medium)
333. Largest BST Subtree (medium)
687. Longest Univalue Path (easy)
124. Binary Tree Maximum Path Sum (hard)
##### Top-down DFS
100. Same Tree (easy)
101. Symmetric Tree (easy)
116. Populating Next Right Pointers in Each Node (medium)
117. Populating Next Right Pointers in Each Node II (medium)
617. Merge Two Binary Trees (easy)
##### Bottom-up DFS
543. Diameter of Binary Tree
250. Count Univalue Subtrees (medium)
236. Lowest Common Ancester of a Binary Tree (medium)



### Session 4
563. Binary Tree Tilt (easy)
156. Binary Tree Upside Down (medium)
426. Convert Binary Search Tree to Sorted Doubly Linked List (medium)
230. Kth Smallest Element in a BST (medium)
114. Flatten Binary Tree to Linked List (medium)
144. Binary Tree Preorder Traversal (medium)
94. Binary Tree Inorder Traversal (medium)
145. Binary Tree Postorder Traversal (hard)
173. Binary Search Tree Iterator (medium)


### Session 5
108. Convert Sorted Array to Binary Search Tree (easy)
109. Convert Sorted List to Binary Search Tree (medium)
extra. Merge two BTSs
105. Construct Binary Tree from Preorder and Inorder Traversal
1008. Construct Binary Search Tree from Preorder Traversal (medium)
106. Construct Binary Tree from Inorder an Postorder Traversal (medium)
449. Serialize and Deserialize BST (medium)
297. Serialize and Deserialize Binary Tree (hard)
109. Convert Sorted List to Binary Search Tree (medium)


