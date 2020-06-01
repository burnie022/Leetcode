"""
Invert a binary tree.
Example:
    Input:
         4
       /   \
      2     7
     / \   / \
    1   3 6   9

    Output:
         4
       /   \
      7     2
     / \   / \
    9   6 3   1

Trivia:
    This problem was inspired by this original tweet by Max Howell:
        Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary
        tree on a whiteboard so f*** off.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def invert(root):
            if not root:
                return
            temp = None
            if root.left and root.right:
                temp = root.left
                root.left = root.right
                root.right = temp
            elif root.left:
                root.right = root.left
                root.left = None
            elif root.right:
                root.left = root.right
                root.right = None

            invert(root.left)
            invert(root.right)

        invert(root)
        return root

