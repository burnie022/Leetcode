"""
Given the root of a binary tree, find the maximum value V for which there exist different
nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any child of A
is an ancestor of B.

Example 1:
    Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
    Output: 7
    Explanation: We have various ancestor-node differences, some of which are given below :
    |8 - 3| = 5
    |3 - 7| = 4
    |8 - 1| = 7
    |10 - 13| = 3
    Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
Example 2:
    Input: root = [1,null,2,null,0,3]
    Output: 3
Constraints:
    The number of nodes in the tree is in the range [2, 5000].
    0 <= Node.val <= 105
Hint #1
    For each subtree, find the minimum value and maximum value of its descendants.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxAncestorDiff(root: TreeNode) -> int:
    max_diff = 0

    def post_order_dfs(node):
        if not node.left and not node.right:
            return node.val, node.val

        nonlocal max_diff
        min_l, min_r, max_l, max_r = 100000, 100000, 0, 0
        if node.left:
            a, b = post_order_dfs(node.left)
            min_l, max_l = min(min_l, a, node.val), max(max_l, b, node.val)
            max_diff = max(max_diff, abs(node.val - a), abs(node.val - b))


        if node.right:
            a, b = post_order_dfs(node.right)
            min_r, max_r = min(min_r, a, node.val), max(max_r, b, node.val)
            max_diff = max(max_diff, abs(node.val - a), abs(node.val - b))

        return min(min_l, min_r), max(max_l, max_r)

    a, b = post_order_dfs(root)
    print(f"Min:{a}, Max:{b}")

    return max_diff

# Test cases

from leetcode_tree_builder import deserialize

# node1 = TreeNode(1)
# node1.right = TreeNode(2)
# node1.right.right = TreeNode(0)
# node1.right.right.left = TreeNode(3)

# node2 = TreeNode(4)
# node2.left = TreeNode(2)
# node2.right = TreeNode(9)
# node2.left.left = TreeNode(3)
# node2.left.right = TreeNode(5)
# node2.right.right = TreeNode(7)

# node3 = TreeNode(8)
# node3.left = TreeNode(3)
# node3.right = TreeNode(10)
# node3.left.left = TreeNode(1)
# node3.left.right = TreeNode(6)
# node3.right.right = TreeNode(14)
# node3.left.right.left = TreeNode(4)
# node3.left.right.right = TreeNode(7)
# node3.right.right.left = TreeNode(13)

node = deserialize('[8,3,10,1,6,null,14,null,null,4,7,13]')

node2 = deserialize('[1,null,2,null,0,3]')

node3 = deserialize('[8,3,10,1,6,8,14,null,5,null,2,4,7,13,null, 9, 3,5,null,null,4,0,1,null,null,0,1,null,2,1,null,1,0,5,4,null,8]')

# print(maxAncestorDiff(node2))

trees = (
    '[8,3,10,1,6,null,14,null,null,4,7,13]',
    '[1,null,2,null,0,3]',
    '[8,3,10,1,6,8,14,null,5,null,2,4,7,13,null, 9, 3,5,null,null,4,0,1,null,null,0,1,null,2,1,null,1,0,5,4,null,8]',
    '[8,3,10,13,6,8,14,null,53,null,12,4,7,13,null, 9, 3,5,null,null,4,10,1,null,null,10,1,null,2,1,null,1,10,5,4,null,8]',
    '[2,8]'

)

for tree in trees:
    print(maxAncestorDiff(deserialize(tree)))
