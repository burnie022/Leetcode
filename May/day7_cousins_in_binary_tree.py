"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        def traverse(node, x, y):
            if node.val == x or node.val == y:
                return 1
            left, right = False, False
            if node.left:
                left = traverse(node.left, x, y)
            if node.right:
                right = traverse(node.right, x, y)

            if left is True or right is True:
                return True

            if left or right:
                if left and right:
                    # print("left:", left, "right:", right)
                    if left == right and left > 1:
                        return True
                    return False
                elif left:
                    return left + 1
                elif right:
                    return right + 1

            return False

        flag = traverse(root, x, y)
        return True if flag is True else False

# For testing
obj = Solution()

node = TreeNode(6)
node.left = TreeNode(3)
node.right = TreeNode(5)
node.left.left = TreeNode(7)
node.left.right = TreeNode(8)
node.right.left = TreeNode(1)
node.right.right = TreeNode(4)

print(obj.isCousins(node, 8, 1))