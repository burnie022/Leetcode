class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidSequence(root, arr) -> bool:
    if len(arr) == 1 and root.val == arr[0] and root.left is None and root.right is None:
        return True
    if len(arr) > 1 and root.val == arr[0]:
        leaf_check = False
        if root.left:
            leaf_check = isValidSequence(root.left, arr[1:])
        if root.right and not leaf_check:
            leaf_check = isValidSequence(root.right, arr[1:])
        return leaf_check
    # covers conditions - (root.val != arr[0]) - as well as - (root.left or root.right and len(arr) == 1)
    return False


# For my testing
seq = [1,1,1,0,1]
node = TreeNode(1)
node.left = TreeNode(1)
node.right = TreeNode(0)

node.left.left = TreeNode(0)
node.left.left.right = TreeNode(1)
node.left.right = TreeNode(1)
node.left.right.left = TreeNode(0)
node.left.right.right = TreeNode(1)

node.right.left = TreeNode(0)

print(isValidSequence(node, seq))
