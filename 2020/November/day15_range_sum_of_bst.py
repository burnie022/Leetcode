"""
Given the root node of a binary search tree, return the sum of values of all nodes
with a value in the range [low, high].
Example 1:
    Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    Output: 32
Example 2:
    Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    Output: 23
Constraints:
    The number of nodes in the tree is in the range [1, 2 * 104].
    1 <= Node.val <= 105
    1 <= low <= high <= 105
    All Node.val are unique.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.total = 0

        def dfs(node):
            if not node:
                return
            if low <= node.val <= high:
                self.total += node.val

            if node.val > low:
                dfs(node.left)

            if node.val < high:
                dfs(node.right)

        dfs(root)
        return self.total


# Test cases
from leetcode_tree_builder import deserialize

s = Solution()

tests = (
    ("[10,5,15,3,7,null,18]", 7, 15),
    ("[10,5,15,3,7,13,18,1,null,6]", 6, 10),
    ("[10,5,15,3,7,13,18,1,null,6]", 1, 5)

)
for t in tests:
    root = deserialize(t[0])
    print(s.rangeSumBST(root, t[1], t[2]), end="\n\n")
