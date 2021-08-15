"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary
search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by
more than one.

Example 1: VIEW PIC: sorted_to_BST_ex1a.jpg
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted:
        VIEW PIC: sorted_to_BST_ex1b.jpg

Example 2: VIEW PIC: sorted_to_BST_ex2.jpg
    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in a strictly increasing order.
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def build_BST(node, start=0, end=len(nums)-1):
            mid = (end + start) // 2
            node.value = nums[mid]
            if start < mid:
                node.left = TreeNode()
                build_BST(node.left, start, mid - 1)
            if end > mid:
                node.right = TreeNode()
                build_BST(node.right, mid + 1, end)

        root = TreeNode()
        build_BST(root)
        return root


if __name__ == "__main__":
    obj = Solution()
    tests = [
        [-10, -3, 0, 5, 9],
        [1, 3]
    ]

    for t in tests:
        print(t)
        print(obj.sortedArrayToBST(t), end="\n\n")

