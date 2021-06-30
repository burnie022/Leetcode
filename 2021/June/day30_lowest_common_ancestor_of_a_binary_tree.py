"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1: VIEW EXAMPLE PIC: lowest_common_ancestor_binary_tree_ex1.png
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.

Example 2: VIEW EXAMPLE PIC: lowest_common_ancestor_binary_tree_ex2.png
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA
    definition.

Example 3:
    Input: root = [1,2], p = 1, q = 2
    Output: 1

Constraints:
    The number of nodes in the tree is in the range [2, 10^5].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the tree.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def get_path_to_node(node, target):
            if not node:
                return
            if node == target:
                return [target.val]
            path = get_path_to_node(node.left, target)
            if not path:
                path = get_path_to_node(node.right, target)
            return [node.val] + path if path else None


        path_p = get_path_to_node(root,p)
        path_q = get_path_to_node(root, q)

        i = 0
        node = root
        while True:
            if i < min(len(path_p), len(path_q)) - 1 and path_p[i+1] == path_q[i+1]:
                if node.left and node.left.val == path_p[i+1]:
                    node = node.left
                else:
                    node = node.right
                i += 1
            else:
                return node


if __name__ == "__main__":
    obj = Solution()
    tests = [

    ]

    for t in tests:
        print(t)
        print(obj.lowestCommonAncestor(*t), end="\n\n")

