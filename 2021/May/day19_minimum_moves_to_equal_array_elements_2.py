"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment or decrement an element of the array by 1.

Example 1:
    Input: nums = [1,2,3]
    Output: 2
    Explanation:
        Only two moves are needed (remember each move increments or decrements one element):
            [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:
    Input: nums = [1,10,2,9]
    Output: 16

Constraints:
    n == nums.length
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
"""
from typing import List
import statistics


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = int(statistics.median(nums))
        print("median: ", median)
        total_moves = sum(abs(median - num) for num in nums)

        return total_moves


# Test cases
obj = Solution()

tests = [
[1,2,3],
[1,10,2,9],
    [1, 99, 99, 99, 99, 99],
[1, 99, 99, 99, 99, 99, 99],
    [1, 99, 99],
    [1, 1, 1, 1, 1, 1, 1, 1, 99],
[1, 1, 1, 1, 1, 1, 1, 1, 99, 99],
[1, 1, 99],
    [1, 1, 1],
    [1],
    [2],
    [2, 1],
    [2, 2],
    [-1, 98, 99],
[-1, 98, 99, 100],
]

for t in tests:
    print(t)
    print(obj.minMoves2(t), end="\n\n")


# from random import randint
# def generate_test(length=100, pos_range=100, neg_range=-100):
#     li = []
#     for _ in range(length):
#         li.append(randint(neg_range, pos_range))
#     return li
#
# print(generate_test(99991, 11000, -11000))

