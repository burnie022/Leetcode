"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a
value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
    Input: root = [3,1,4,3,null,1,5]
    Output: 4
    Explanation: Nodes in blue are good.
    Root Node (3) is always a good node.
    Node 4 -> (3,4) is the maximum value in the path starting from the root.
    Node 5 -> (3,4,5) is the maximum value in the path
    Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
    Input: root = [3,3,null,4,2]
    Output: 3
    Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
    Input: root = [1]
    Output: 1
    Explanation: Root is considered as good.

Constraints:
    The number of nodes in the binary tree is in the range [1, 10^5].
    Each node's value is between [-10^4, 10^4].

Hint #1
    Use DFS (Depth First Search) to traverse the tree, and constantly keep track of the current path maximum.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, m):
            if not node:
                return 0
            n = max(node.val, m)
            return dfs(node.left, n) + dfs(node.right, n) + (node.val >= m)

        return dfs(root, root.val)


if __name__ == "__main__":
    obj = Solution()
    tests = [

    ]

    for t in tests:
        print(t)
        print(obj.goodNodes(t), end="\n\n")
