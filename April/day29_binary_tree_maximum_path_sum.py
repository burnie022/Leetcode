"""Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree
along the parent-child connections. The path must contain at least one node and does not need to go through
the root.
Example 1:
    Input: [1,2,3]

           1
          / \
         2   3

    Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]

       -10
       / \
      9  20
        /  \
       15   7

    Output: 42
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_val = root.val

        def findMaxPath(node):
            left = findMaxPath(node.left) if node.left else None
            right = findMaxPath(node.right) if node.right else None

            local_max = max(x for x in [left, right, node.val] if x is not None)
            sum = node.val
            if left:
                sum += left
            if right:
                sum += right
            local_max = max(local_max, sum)

            nonlocal max_val
            if local_max > max_val:
                max_val = local_max

            if right or left:
                branch_sum = node.val + max(x for x in [left, right] if x is not None)
                if branch_sum > node.val:
                    return branch_sum
                else:
                    return node.val
            else:
                return node.val

        sum_plus_root = findMaxPath(root)
        if sum_plus_root > max_val:
            max_val = sum_plus_root

        return max_val


# For my testing
obj = Solution()
node = TreeNode(1)
node.left = TreeNode(-2)
node.right = TreeNode(3)
# node.right.left = TreeNode(-2)
# node.right.right = TreeNode(3)

# print(node.val)
# print(node.left.val)
# print(node.right.val)

print("Max path Sum: ")
print(obj.maxPathSum(node))
