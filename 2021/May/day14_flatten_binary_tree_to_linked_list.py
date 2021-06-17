"""
Given the root of a binary tree, flatten the tree into a "linked list":
    The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the
        list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1: VIEW PIC: flatten_binary_tree_ex1.jpg
    Input: root = [1,2,5,3,4,null,6]
    Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:
    Input: root = []
    Output: []
Example 3:
    Input: root = [0]
    Output: [0]

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
Hint #1
    If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order
    traversal.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root:
            if root.left and root.right:
                self.append_right_node_to_end(root.left, root.right)
            if root.left:
                root.right = root.left
            root.left = None
            self.flatten(root.right)

    def append_right_node_to_end(self, node, new_node):
        while node.right:
            node = node.right
        node.right = new_node




# Test cases