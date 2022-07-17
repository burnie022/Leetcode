"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
    Input: root = [1,2,2,3,4,4,3]
    Output: true

Example 2:
    Input: root = [1,2,2,null,3,null,3]
    Output: false

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check_nodes(a, b):
            if a is None and b is None:
                return True
            if (not a and b) or (a and not b) or a.val != b.val:
                return False
            return check_nodes(a.left, b.right) and check_nodes(a.right, b.left)

        return check_nodes(root.left, root.right)


if __name__ == "__main__":
    obj = Solution()
    tests = [

    ]

    for t in tests:
        print(t)
        print(obj(t), end="\n\n")
