"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.



Example 1: VIEW PIC: pathsum2_ex1.jpg
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: [[5,4,11,2],[5,8,4,5]]

Example 2: VIEW PIC: pathsum2_ex2.jpg
    Input: root = [1,2,3], targetSum = 5
    Output: []

Example 3:
    Input: root = [1,2], targetSum = 0
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        paths = []

        def dfs(node, total, path):
            if not node.left and not node.right:
                if total + node.val == targetSum:
                    paths.append(path + [node.val])
            else:
                path = path + [node.val]
                if node.left:
                    dfs(node.left, total + node.val, path[:])
                if node.right:
                    dfs(node.right, total + node.val, path[:])

        dfs(root, 0, [])
        return paths


if __name__ == "__main__":
    obj = Solution()
    tests = [

    ]

    for t in tests:
        print(t[0])
        print(t[1])
        print(obj(*t), end="\n\n")
