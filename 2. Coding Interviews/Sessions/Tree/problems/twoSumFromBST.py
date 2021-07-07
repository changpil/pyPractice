"""
This problem is a fun combination of the famous Two Sum problem combined with a binary search tree. Given the root of a binary search tree, and a target integer K, return true if there exist two nodes in the said tree whose sum equals K. If no pair fits this match, return false.

Say we are given this tree:

JAVASCRIPT
/***

  Input:
    5
   / \
  3   8
 /
1

***/
Each node is defined in the following manner:

JAVASCRIPT
class Node {
	constructor(val) {
		this.value = val;
		this.left = null;
		this.right = null;
	}
}
And thus the below setup and execution code should hold true:

JAVASCRIPT
const root = new Node(5);
root.left = new Node(3);
root.right = new Node(8);
root.left.left = new Node(1);

const target = 11;

twoSumFromBST(root, target);
// true because 3 + 8 = 11

Constraints
Number of vertices in the tree <= 100000
The values in the vertices will be between -100000 and 1000000
The target value will be between -100000 and 100000
Expected time complexity : O(n)
Expected space complexity : O(n)
"""

def twoSumFromBST(root, target):
    h = {}
    return traverse(root,h, target)

def traverse(node, h, target):
    if node == None:
        return
    left = traverse(node.left, h, target)
    need = target - node.val
    if need in h:
        return True
    else:
        h[node.val] = 0
    right =  traverse(node.right, h, target)
    if left or right:
        return True
    return False


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(19)
root.left.left = TreeNode(1)
root.right.left = TreeNode(15)
root.right.right = TreeNode(26)
print(twoSumFromBST(root, 20))
print(twoSumFromBST(root, 13))
print(twoSumFromBST(root, 15))



root = TreeNode(0)
root.left = TreeNode(-7)
root.right = TreeNode(19)
root.left.left = TreeNode(-11)
root.right.left = TreeNode(15)
root.right.right = TreeNode(26)
print(twoSumFromBST(root, 12))
print(twoSumFromBST(root, 0))
print(twoSumFromBST(root, 15))
