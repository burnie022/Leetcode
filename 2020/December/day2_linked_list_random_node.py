"""
Given a singly linked list, return a random node's value from the linked list. Each node must
have the same probability of being chosen.
Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve
this efficiently without using extra space?

Example:
    // Init a singly linked list [1,2,3].
    ListNode head = new ListNode(1);
    head.next = new ListNode(2);
    head.next.next = new ListNode(3);
    Solution solution = new Solution(head);

    // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal
        probability of returning.
    solution.getRandom();
"""
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head: ListNode):
        self.vals = []

        while head:
            self.vals.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return self.vals[random.randint(0, len(self.vals) - 1)]


"""
The above solution yields an O(n) time complexity in its init function because it traverses the entire 
linked list to append every value to the vals list and an O(1) time complexity in the getRandom() function
due to it simply generating a random number and returning a value from the vals list by index.

While this is a quick solution, its space complexity is O(n), which doesn't satisfy the O(1) space complexity
from the follow up question

To satisfy the follow up question, we can use "Reservoir Sampling" to satisfy an O(1) space complexity for 
a linked list. For every listnode in the list, we can calculate the probability of it being chosen by 1 / n,
where n is the total number of listnodes seen so far. 
For example, At the first listnode, its probability of it being chosen is 1/1. The second's probability would 
be 1/2, the third's is 1/3, ... etc. So we can store a chose value when it's probability of being chosen is
less than or equal to 1/n ( <= 1/n). After choosing a random number rand_num, when rand_num <= 1/n, we can 
replace our chosen number.

This algorithm using Reservoir Sampling has been implemented below
"""

class Solution2:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        chosen_val = None
        node = self.head
        n = 1
        while node:
            rand_num = random.random()
            if rand_num <= 1 / n:
                chosen_val = node.val
            n += 1
            node = node.next
        return chosen_val

"""
This solution (Solution2) is slower than the first but uses just O(1) space, as requested by the follow up 
question by using Reservoir Sampling. 
The init() function uses O(1) time to simply assign self.head. getRandom() uses O(n) time because it must 
traverse the entire list and perform the probability operation for each node value at every call of the function.
However, this works when taking in values from almost endless data streams without needing to store
and append to extremely large lists.
"""

# test cases

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

s = Solution(head)
count = {1: 0, 2: 0, 3: 0}

s2 = Solution2(head)

for _ in range(30000):
    # print(s.getRandom())
    i = s2.getRandom()
    count[i] += 1

print(count)

