"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
    Input: root = [3,1,4,null,2], k = 1
       3
      / \
     1   4
      \
       2
    Output: 1

Example 2:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
           5
          / \
         3   6
        / \
       2   4
      /
     1
    Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest
frequently? How would you optimize the kthSmallest routine?
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: TreeNode, k: int) -> int:
    kth_element = None

    def traverse(node, j=None):
        if node.left is None:
            j = j + 1 if j else 1
        elif node.left:
            j = traverse(node.left, j)
            if j is None:
                return
            else: j += 1

        if j == k:
            nonlocal kth_element
            kth_element = node.val
            return

        if node.right:
            j = traverse(node.right, j)

        return j

    traverse(root)
    return kth_element


# For testing
n = TreeNode(20)
n.left = TreeNode(8)
n.left.left = TreeNode(3)
n.left.right = TreeNode(16)
n.left.right.left = TreeNode(12)
n.left.right.right = TreeNode(18)

n.right = TreeNode(38)
n.right.left = TreeNode(30)
n.right.left.left = TreeNode(22)
n.right.left.right = TreeNode(32)
n.right.right = TreeNode(42)
n.right.right.right = TreeNode(50)

for i in range(1, 13):
    print(kthSmallest(n, i))
