"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [2,1,3]
    Output: true
Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1
"""
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def bfs(node, smaller=-math.inf, bigger=math.inf):
            if not node:
                return True
            if smaller >= node.val or bigger <= node.val:
                return False
            return bfs(node.left, smaller, node.val) and bfs(node.right, node.val, bigger)

        return bfs(root)




# Test cases
from leetcode_tree_builder import deserialize

s = Solution()
tests = [
    "[2,1,3]",
    "[5,1,4,null,null,3,6]",
    "[2,1,4,null,null,3,6]",
    "[2,1,4,null,null,2,6]",
    "[1,0,4,null,null,2,6,null, 3]",
    "[1,0,7,null,null,2,8,null, 3]",
    "[1,0,7,null,null,2,8,null,3,null,null,null,4,null,5,null,7]"

]

for t in tests:
    print(t)
    print(s.isValidBST(deserialize(t)))
