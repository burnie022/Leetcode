"""
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all
right subtree node values. If a node does not have a left child, then the sum of the left subtree node values
is treated as 0. The rule is similar if there the node does not have a right child.

Example 1:
    Input: root = [1,2,3]
    Output: 1
    Explanation:
    Tilt of node 2 : |0-0| = 0 (no children)
    Tilt of node 3 : |0-0| = 0 (no children)
    Tile of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child,
    so sum is 3)
    Sum of every tilt : 0 + 0 + 1 = 1
Example 2:
    Input: root = [4,2,9,3,5,null,7]
    Output: 15
    Explanation:
    Tilt of node 3 : |0-0| = 0 (no children)
    Tilt of node 5 : |0-0| = 0 (no children)
    Tilt of node 7 : |0-0| = 0 (no children)
    Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right
    child, so sum is 5)
    Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
    Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10;
    right subtree values are 9 and 7, which sums to 16)
    Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15
Example 3:
    Input: root = [21,7,14,1,1,2,2,3,3]
    Output: 9

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -1000 <= Node.val <= 1000
Hint #1
Don't think too much, this is an easy problem. Take some small tree as an example.
Hint #2
Can a parent node use the values of its child nodes? How will you implement it?
Hint #3
May be recursion and tree traversal can help you in implementing.
Hint #4
What about postorder traversal, using values of left and right childs?
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findTilt(root: TreeNode) -> int:
    if not root:
        return 0

    def get_sums(node):
        val = node.val
        left_tot, left_diff_sum, right_tot, right_diff_sum = 0, 0, 0, 0
        if node.left:
            left_tot, left_diff_sum = get_sums(node.left)
        if node.right:
            right_tot, right_diff_sum = get_sums(node.right)

        return (val + left_tot + right_tot), (abs(left_tot - right_tot) + left_diff_sum + right_diff_sum)

    return get_sums(root)[1]


# Test cases

node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.right = TreeNode(3)

node2 = TreeNode(4)
node2.left = TreeNode(2)
node2.right = TreeNode(9)
node2.left.left = TreeNode(3)
node2.left.right = TreeNode(5)
node2.right.right = TreeNode(7)

node3 = TreeNode(21)
node3.left = TreeNode(7)
node3.right = TreeNode(14)
node3.left.left = TreeNode(1)
node3.left.right = TreeNode(1)
node3.right.left = TreeNode(2)
node3.right.right = TreeNode(2)
node3.left.left.left = TreeNode(3)
node3.left.left.right = TreeNode(3)

node4 = None

node5 = TreeNode(1)

print(findTilt(node5))
