"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right,
level by level).

Example 1: VIEW PIC: binary_tree_level_order_traversal_ex1.jpg
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
Example 2:
    Input: root = [1]
    Output: [[1]]
Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""
from typing import  List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []

        def dfs(node, level=0):
            if len(levels) < level + 1:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)

        if root:
            dfs(root)

        return levels


# Test cases
from leetcode_tree_builder import deserialize, drawtree
obj = Solution()
tests = [
    "[3,9,20,null,null,15,7]",
    "[1]",

    # "[]", # This test case doesn't work with deserialize

    "[0,1,2,3,4,null,5]",
    "[0,1,2,3,4,null,5,null,6,null, 7,8,null,9,10,12,13,14,15]",
    "[0,1,2,null,null,3,null,null,4]",
    "[0,1,2,3,null,4,null,null,5,6]",
    "[0,1,2,null,3,4,null,null,5]",
    "[0,1,2,null,null,null,3]",
    "[1,2,5,3,4,null,6]",
]

for t in tests:
    print(t)
    print(obj.levelOrder(deserialize(t)), end="\n\n")



# trees = [
#     "[0,1,2,3,4,null,5,null,6,null, 7,8,null,9,10,12,13,14,15]",
#     "[1,2,5,3,4,null,6]"
# ]
# drawtree(deserialize(trees[1]))


# test = [
# "[0,0,0,0,0,null,0]",
# "[0,0,0,0,0,null,0,null,0,null, 0,0,null,0,0,0,0,0,0]",
# "[0,0,0,null,null,0,null,null,0]",
# "[0,0,0,0,null,0,null,null,0,0]",
# "[0,0,0,null,0,0,null,null,0] ",
# "[0,0,0,null,null,null,0] ",
# "[1,2,5,3,4,null,6]",
# ]
#
# for t in test:
#     num = 0
#     for i in range(len(t)):
#         if t[i] == "0":
#             t = t[:i] + str(num) + t[i+1:]
#             num +=1
#     print(f"\"{t}\",")
# # for t in test:
# #     print(f"\"{t}\",")


