"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced
BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.

Example 1: VIEW EXAMPLE PIC convert_sorted_list_to_binary_search_tree_ex1.jpg
    Input: head = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:
    Input: head = []
    Output: []
Example 3:
    Input: head = [0]
    Output: [0]
Example 4:
    Input: head = [1,3]
    Output: [3,1]

Constraints:
    The number of nodes in head is in the range [0, 2 * 104].
    -10^5 <= Node.val <= 10^5
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, vals=None):
        self.val = None
        self.left = None
        self.right = None
        self.balance_vals(vals)

    def balance_vals(self, vals):
        if vals:
            mid = int(len(vals) / 2)
            self.val = vals[mid]

            if vals[:mid]:
                self.left = TreeNode(vals[:mid])
            if vals[mid + 1:]:
                self.right = TreeNode(vals[mid + 1:])


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        if vals:
            return TreeNode(vals)


# Test cases

obj = Solution()
tests = [
    [-10, -3, 0, 5, 9],
    [-10, -3, 0, 5, 9, 10],
    [-10, -3, 0, 5, 9, 10, 15, 19],
    [-10, -3, 0, 5, 9, 10, 15, 19, 20],
    [-10, -3, 0, 5, 9, 10, 15, 19, 20, 21, 24, 28],
    [-10, -3, 0, 5, 9, 10, 15, 19, 20, 21, 24, 28, 29],
    [],
    [0],
    [1, 3],
]


def make_list_nodes(vals):
    head = ListNode(vals[0])
    i = 1
    node = head
    while i < len(vals):
        node.next = ListNode(vals[i])
        node = node.next
        i += 1

    return head


for t in tests:
    print(t)
    # head = make_list_nodes(t)
    # obj.sortedListToBST(make_list_nodes(t))


# from random import randint
# li = []
# i = -10000
# while len(li) < 8000 and i < 10001:
#     if randint(1, 4) == 1:
#         li.append(i)
#     i += 1
# print(li)

