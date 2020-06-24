"""
Given a complete binary tree, count the number of nodes.
Note:
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level
are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Example:
    Input:
            1
           / \
          2   3
         / \  /
        4  5 6

    Output: 6
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countNodes(root: TreeNode) -> int:
    count = 0

    def dfs(node):
        nonlocal count
        count += 1
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)

    if root:
        dfs(root)

    return count


# For testing

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.left = TreeNode(6)

print(countNodes(node))

"""
[1,2,3,4,5,6]
"""
