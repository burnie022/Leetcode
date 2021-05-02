"""
You are given two non-empty linked lists representing two non-negative integers. The
most significant digit comes first and each of their nodes contain a single digit. Add
the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0
itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is
not allowed.

Example:
    Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 8 -> 0 -> 7
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

    def get_num(node, num=0):
        if not node:
            return num
        num = (num * 10) + node.val
        return get_num(node.next, num)

    num = str(get_num(l1) + get_num(l2))

    head = ListNode()
    start = head
    while num != "":
        head.next = ListNode(int(num[0]))
        head = head.next
        num = num[1:]

    return start.next


# Test cases

def make_linked_list(node, num):
    node.val = int(num[0])
    if num[1:] == "":
        return
    else:
        node.next = ListNode()
        make_linked_list(node.next, num[1:])

tests = [(7243, 564),
         (18, 90),
         (1, 1001),
         (0, 11),
         (0, 0),
         (0, 80)

        ]

for n1, n2 in tests:
    l1, l2 = ListNode(), ListNode()
    print("")
    make_linked_list(l1, str(n1))
    make_linked_list(l2, str(n2))

    node = addTwoNumbers(l1, l2)

    while node:
        print(node.val, end="")
        node = node.next
    print("")

