"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list
is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.

Example 1:
    Input: head = [1,0,1]
    Output: 5
    Explanation: (101) in base 2 = (5) in base 10
Example 2:
    Input: head = [0]
    Output: 0
Example 3:
    Input: head = [1]
    Output: 1
Example 4:
    Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
    Output: 18880
Example 5:
    Input: head = [0,0]
    Output: 0

Constraints:
    The Linked List is not empty.
    Number of nodes will not exceed 30.
    Each node's value is either 0 or 1.
Hint #1
Traverse the linked list and store all values in a string or array. convert the values obtained to decimal value.
Hint #2
You can solve the problem in O(1) memory using bits operation. use shift left operation ( << ) and or operation ( | ) to get the decimal value in one operation.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getDecimalValue(head):
    nums = [str(0)]

    while head:
        nums.append(str(head.val))
        head = head.next

    return int("".join(nums), 2)


# Test cases

node = ListNode(1)
node.next = ListNode(0)
node.next.next = ListNode(1)

node2 = ListNode(1)
node2.next = ListNode(0)
node2.next.next = ListNode(0)
node2.next.next.next = ListNode(1)
node2.next.next.next.next = ListNode(0)
node2.next.next.next.next.next = ListNode(0)
node2.next.next.next.next.next.next = ListNode(1)
node2.next.next.next.next.next.next.next = ListNode(1)
node2.next.next.next.next.next.next.next.next = ListNode(1)
node2.next.next.next.next.next.next.next.next.next = ListNode(0)
node2.next.next.next.next.next.next.next.next.next.next = ListNode(0)
node2.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
node2.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
node2.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
node2.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)

node3 = ListNode(0)

node4 = ListNode(1)

node5 = ListNode(0)
node5.next = ListNode(0)


print(getDecimalValue(node5))
