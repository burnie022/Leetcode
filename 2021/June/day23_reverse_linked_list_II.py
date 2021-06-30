"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the
list from position left to position right, and return the reversed list.

Example 1: VIEW EXAMPLE PIC: reverse_linked_list_II_ex1.jpg
    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]
Example 2:
    Input: head = [5], left = 1, right = 1
    Output: [5]

Constraints:
    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if right == left:
            return head
        node_vals = []
        curr = 1
        node = head
        while curr < left:
            curr += 1
            node = node.next

        left_node = node
        while curr <= right:
            curr += 1
            node_vals.append(node.val)
            node = node.next

        for val in node_vals[::-1]:
            left_node.val = val
            left_node = left_node.next

        return head



if __name__ == "__main__":
    obj = Solution()
    tests = [

    ]

    for t in tests:
        print(t)
        print(obj.reverseBetween(*t), end="\n\n")
