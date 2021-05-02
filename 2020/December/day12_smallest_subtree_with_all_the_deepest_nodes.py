"""
Given the root of a binary tree, the depth of each node is the shortest distance to the root.
Return the smallest subtree such that it contains all the deepest nodes in the original tree.
A node is called the deepest if it has the largest depth possible among any node in the entire
tree.
The subtree of a node is tree consisting of that node, plus the set of all descendants of that
node.
Note: This question is the same as 1123:
https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

Example 1:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4]
    Output: [2,7,4]
    Explanation: We return the node with value 2, colored in yellow in the diagram.
    The nodes coloured in blue are the deepest nodes of the tree.
    Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the
    smallest subtree among them, so we return it.
Example 2:
    Input: root = [1]
    Output: [1]
    Explanation: The root is the deepest node in the tree.
Example 3:
Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes
2, 1 and 0 but the subtree of node 2 is the smallest.

Constraints:
    The number of nodes in the tree will be in the range [1, 500].
    0 <= Node.val <= 500
    The values of the nodes in the tree are unique.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        total_nodes_in_level = {}

        def get_height(node, level=1):
            if not node:
                return 0
            total_nodes_in_level[level] = total_nodes_in_level.get(level, 0) + 1
            get_height(node.left, level + 1)
            get_height(node.right, level + 1)

        get_height(root)
        self.height = max(total_nodes_in_level.keys())
        self.total = total_nodes_in_level[self.height]
        self.subtree_root = root

        def find_deepest_node_subtree(node, level = 1):
            if not node:
                return 0
            if level == self.height:
                if self.total == 1:
                    self.subtree_root = node
                    return 0
                return 1
            total_deepest = find_deepest_node_subtree(node.left, level + 1)
            total_deepest += find_deepest_node_subtree(node.right, level + 1)
            if total_deepest == self.total:
                self.subtree_root = node
                return 0
            return total_deepest

        find_deepest_node_subtree(root)
        return self.subtree_root


# Test cases
from leetcode_tree_builder import deserialize

tests = [
    "[3,5,1,6,2,0,8,null,null,7,4]",
    "[1]",
    "[0,1,3,null,2]",
    "[0,1,8,null,2, null,null,3,null,null,4,null,5]",
    "[3,5,1,6,2,0,8,null,null,7,4, null,null,9,null,null,10,null,null,11]",
    "[3,5,1,6,2,0,8,null,null,7,4, null,null,9,null,null,10,11,null,12,null, 13, 14, 15]"
]
s = Solution()

for t in tests:
    print(s.subtreeWithAllDeepest(deserialize(t)))

