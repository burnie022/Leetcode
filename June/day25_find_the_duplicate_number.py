"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least
one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
Example 1:
    Input: [1,3,4,2,2]
    Output: 2
Example 2:
    Input: [3,1,3,4,2]
    Output: 3
Note:
    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.
"""


# My solution is suboptimal, trying to follow the constraints and creating a (1/2)n^2 solution that still does
# not satisfy the O(n^2) constaint. A much more intuitive approach would be to use a set, but that would break the
# constant space, O(1), constraint. The given solution on LC is Floyd's Tortoise and Hare algorithm, which I will
# include below my solution


def findDuplicate(nums) -> int:
    i = 0

    while i < len(nums) - 1:
        if nums[i] in nums[i + 1:]:
            return nums[i]
        i += 1


# Optimal solution below
"""
Floyd's Tortoise and Hare (Cycle Detection)
Intuition

The idea is to reduce the problem to Linked List Cycle II:

Given a linked list, return the node where the cycle begins.

First of all, where does the cycle come from? Let's use the function f(x) = nums[x] to construct the sequence: x,
nums[x], nums[nums[x]], nums[nums[nums[x]]], ....

Each new element in the sequence is an element in nums at the index of the previous element.

If one starts from x = nums[0], such a sequence will produce a linked list with a cycle.

The cycle appears because nums contains duplicates. The duplicate node is a cycle entrance.


Floyd's algorithm consists of two phases and uses two pointers, usually called tortoise and hare.

In phase 1, hare = nums[nums[hare]] is twice as fast as tortoise = nums[tortoise]. Since the hare goes fast, it would
be the first one who enters the cycle and starts to run around the cycle. At some point, the tortoise enters the cycle
as well, and since it's moving slower the hare catches the tortoise up at some intersection point. Now phase 1 is over,
and the tortoise has lost.

To compute the intersection point, let's note that the hare has traversed twice as many nodes as the tortoise, i.e.
2d(\text{tortoise}) = d(\text{hare})2d(tortoise)=d(hare), that means

2(F + a) = F + nC + a2(F+a)=F+nC+a, where nn is some integer.
Hence the coordinate of the intersection point is F + a = nCF+a=nC.

In phase 2, we give the tortoise a second chance by slowing down the hare, so that it now moves with the speed of
tortoise: tortoise = nums[tortoise], hare = nums[hare]. The tortoise is back at the starting position, and the hare
starts from the intersection point.
The tortoise started from zero, so its position after FF steps is FF.
The hare started at the intersection point F + a = nCF+a=nC, so its position after F steps is nC + FnC+F, that is the
same point as FF.
So the tortoise and the (slowed down) hare will meet at the entrance of the cycle.

class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
        
        
Complexity Analysis

Time complexity : O(n)

For detailed analysis, refer to Linked List Cycle II.

Space complexity : O(1)

For detailed analysis, refer to Linked List Cycle II.

Analysis and solution written by: @emptyset
"""
