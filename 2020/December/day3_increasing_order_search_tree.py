"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node
in the tree is now the root of the tree, and every node has no left child and only one right child.

Example 1:
    Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
    Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:
    Input: root = [5,1,7]
    Output: [1,null,5,null,7]

Constraints:
    The number of nodes in the given tree will be in the range [1, 100].
    0 <= Node.val <= 1000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head = TreeNode()
        self.curr = head

        def add_right_node(right_node):
            if right_node:
                self.curr.right = TreeNode(right_node.val)
                self.curr = self.curr.right

        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            add_right_node(node)
            inorder_traversal(node.right)

        inorder_traversal(root)
        return head.right


# Test cases
from leetcode_tree_builder import deserialize

tests = [
    "[5,3,6,2,4,null,8,1,null,null,null,7,9]",
    "[5,3,6,1,4,null,8,null,2,null,null,7,9]",
    "[7,3,8,1,5,null,10,null,2,4,6,9,11]"
]
s = Solution()

for t in tests:
    root = deserialize(t)
    node = s.increasingBST(root)
    while node:
        print(node.val)
        if node.left:
            print("whoops")
        node = node.right
    print("")
