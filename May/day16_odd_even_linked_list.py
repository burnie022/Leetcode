class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_nodes = ListNode()
        even_nodes = ListNode()
        odd, even = odd_nodes, even_nodes
        node_counter = 1

        while head:
            if node_counter % 2 != 0: #odd nodes
                odd.next = head
                odd = odd.next

            else:  # even nodes
                even.next = head
                even = even.next

            node_counter += 1
            head = head.next

        even.next = None
        odd.next = even_nodes.next

        return odd_nodes.next

# For testing
obj = Solution()
n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n.next.next.next = ListNode(4)
n.next.next.next.next = ListNode(5)
n.next.next.next.next.next = ListNode(6)
n.next.next.next.next.next.next = ListNode(7)
n.next.next.next.next.next.next.next = ListNode(8)

new_head = obj.oddEvenList(n)
while new_head:
    print(new_head.val)
    new_head = new_head.next
