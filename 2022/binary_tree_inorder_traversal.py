"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
    Input: root = [1,null,2,3]
    Output: [1,3,2]

Example 2:
    Input: root = []
    Output: []

Example 3:
    Input: root = [1]
    Output: [1]

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inorder_trav(node):
            l = inorder_trav(node.left) if node.left else []
            r = inorder_trav(node.right) if node.right else []
            return l + [node.val] + r

        return inorder_trav(root) if root else None


if __name__ == "__main__":
    obj = Solution()
    tests = [

    ]

    for t in tests:
        print(t)
        # print(obj(t), end="\n\n")
