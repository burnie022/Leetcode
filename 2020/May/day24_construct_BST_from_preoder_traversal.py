
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstFromPreorder(preorder) -> TreeNode:
    if not preorder:
        return preorder

    def splitlist(tosplit):
        l, r = [], []
        for i in range(1, len(tosplit)):
            if tosplit[i] < tosplit[0]: l += [tosplit[i]]
            else: r += [tosplit[i]]
        return l, r

    def buildBST(node, vals):
        l, r = splitlist(vals)
        print(l, r)
        if l:
            node.left = TreeNode(l[0])
            buildBST(node.left, l)
        if r:
            node.right = TreeNode(r[0])
            buildBST(node.right, r)

    head = TreeNode(preorder[0])
    buildBST(head, preorder)
    return head


myl = [8,5,1,7,10,12]
bstFromPreorder(myl)