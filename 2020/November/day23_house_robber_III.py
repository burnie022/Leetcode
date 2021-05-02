"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area,
called the "root." Besides the root, each house has one and only one parent house. After a tour, the
smart thief realized that "all houses in this place forms a binary tree". It will automatically contact
the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
    Input: [3,2,3,null,3,null,1]

         3
        / \
       2   3
        \   \
         3   1

    Output: 7
    Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
    Input: [3,4,5,1,3,null,1]

         3
        / \
       4   5
      / \   \
     1   3   1

    Output: 9
    Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:

        def dfs(node):
            if not node:
                return 0, 0
            left_curr, left_prev = dfs(node.left)
            right_curr, right_prev = dfs(node.right)

            curr = left_curr + right_curr
            prev = left_prev + right_prev

            return max(curr, prev + node.val), curr

        return dfs(root)[0]




        # dp = [level_dict[i] for i in range(len(level_dict))]
        # if len(dp) == 1:
        #     return dp[0]
        # if len(dp) == 2:
        #     return max(dp[0], dp[1])
        #
        # dp[0] = level_dict[0]
        # dp[1] = max(level_dict[1], level_dict[0])
        #
        # for i in range(2, len(dp)):
        #     # dp[i] = max(dp[i] + dp[i - 2], dp[i - 1])
        #     dp[i] = max(dp[i] + dp[i-2],  dp[i-1])
        #     print(dp)




# Test cases
from leetcode_tree_builder import deserialize
s = Solution()

tests = [
    "[3,2,3,null,3,null,1]",
    "[3,4,5,1,3,null,1]",
    "[4,1,null,2,null,3]",
    # "[]",
    "[3]",
    "[3,2]",
    "[3,2,3]",
    "[3,2,4,5]",

]

for t in tests:
    print(t)
    print(s.rob(deserialize(t)), end="\n\n")


