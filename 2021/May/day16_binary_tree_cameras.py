"""
Given a binary tree, we install cameras on the nodes of the tree.
Each camera at a node can monitor its parent, itself, and its immediate children.
Calculate the minimum number of cameras needed to monitor all nodes of the tree.

Example 1: VIEW PIC: bst_cameras_01_ex1.png
    Input: [0,0,null,0,0]
    Output: 1
    Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2: VIEW PIC: bst_cameras_01_ex2.png
    Input: [0,0,null,0,null,0,null,null,0]
    Output: 2
    Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Note:
    The number of nodes in the given tree will be in the range [1, 1000].
    Every node has value 0.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.cameras = 0
        def count_cameras(node):
            if not root:
                return 2
            a = count_cameras(node.left)
            b = count_cameras(node.right)
            if a == 1 or b == 1:
                self.cameras += 1
                return 0
            return 2 if a == 0 or b == 0 else 1

        if count_cameras(root) == 1:
            self.cameras += 1
        return self.cameras


# Test cases
tests = [
"""    
[0,0,null,0,0]
[0,0,null,0,null,0,null,null,0]
[0,0,null,0,null,0,null,null,0,0]
[0]
[0,0,null,0,null,0,null,null,0,0]
[0,null,0,null,0,null,0,null,0,null,0]
[0,0,0,0,0,null,0]
[0,0,0,0,0,null,0,null,0,null, 0,0,null,0,0,0,0,0,0]
[0,0,0,null,null,0,null,null,0]
[0,0,0,0,null,0,null,null,0,0]
[0,0,0,null,0,0,null,null,0] 
[0,0,0,null,null,null,0] 
"""
]
