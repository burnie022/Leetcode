"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.
Example:
    Input: [1,2,3]
        1
       / \
      2   3
    Output: 25
    Explanation:
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.
    Therefore, sum = 12 + 13 = 25.
Example 2:
    Input: [4,9,0,5,1]
        4
       / \
      9   0
     / \
    5   1
    Output: 1026
    Explanation:
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path 4->9->1 represents the number 491.
    The root-to-leaf path 4->0 represents the number 40.
    Therefore, sum = 495 + 491 + 40 = 1026.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumNumbers(root) -> int:

    def get_leaf_nums(node, num):
        if not node:
            return []
        if node.left or node.right:
            num = num + str(node.val)
            left = get_leaf_nums(node.left, num)
            right = get_leaf_nums(node.right, num)
            return left + right
        else:
            return [num + str(node.val)]

    leaf_nums = get_leaf_nums(root, "")
    return sum(int(i) for i in leaf_nums) if leaf_nums else 0


# For testing

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)

print(sumNumbers(node))

node_two = TreeNode(4)
node_two.left = TreeNode(9)
node_two.right = TreeNode(0)
node_two.left.left = TreeNode(5)
node_two.left.right = TreeNode(1)

print(sumNumbers(node_two))

node_three = TreeNode(3)

print(sumNumbers(node_three))

print(sumNumbers(TreeNode(1)))

print(sumNumbers(None))
