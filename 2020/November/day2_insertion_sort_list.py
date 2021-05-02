"""
Sort a linked list using insertion sort.
A graphical example of insertion sort. The partial sorted list (black) initially contains
 only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place
into the sorted list

Algorithm of Insertion Sort:
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs
within the sorted list, and inserts it there. It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertionSortList(head: ListNode) -> ListNode:
    if not head: return head
    start = ListNode(head.val, head)
    current = start

    def insertion_sort(temp_node):
        node = start
        while node.next:
            if node.next.val >= temp_node.val:
                temp_node.next = node.next
                node.next = temp_node
                break
            else:
                node = node.next

    while current.next:
        if current.next.val < current.val:
            temp = current.next
            current.next = temp.next
            insertion_sort(temp)
        else:
            current = current.next

    return start.next

# Here I first copy the vals into an array, sort array using built in sorted() method, then reassign the vals
# back into the linked list. Much faster run time.
def insertion_sort_using_array(head):
    if not head:
        return head
    nums = []
    curr = head
    while curr:
        nums.append(curr.val)
        curr = curr.next

    nums = sorted(nums)
    curr = head
    for n in nums:
        curr.val = n
        curr = curr.next

    return head


# Test cases

node = ListNode(4)
node.next = ListNode(2)
node.next.next = ListNode(1)
node.next.next.next = ListNode(3)

node2 = ListNode(-1)
node2.next = ListNode(5)
node2.next.next = ListNode(3)
node2.next.next.next = ListNode(4)
node2.next.next.next.next = ListNode(0)

# curr = insertionSortList(node2)
curr = insertion_sort_using_array(node2)

while curr:
    print(curr.val)
    curr = curr.next