"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes. Only nodes itself may be changed.

Example 1: SEE EXAMPLE PIC
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]
Example 2:
    Input: head = []
    Output: []
Example 3:
    Input: head = [1]
    Output: [1]

Constraints:
    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = ListNode(0, head)
        front = head.next
        while node.next:
            if node.next.next:
                prev = node.next
                node.next = node.next.next
                prev.next = node.next.next
                node.next.next = prev
                node = node.next.next
            else:
                break
        return front


# Test cases

# Tested and accepted on leatcode
