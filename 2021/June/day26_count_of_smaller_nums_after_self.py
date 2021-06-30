"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where
counts[i] is the number of smaller elements to the right of nums[i].

Example 1:
    Input: nums = [5,2,6,1]
    Output: [2,1,1,0]
    Explanation:
        To the right of 5 there are 2 smaller elements (2 and 1).
        To the right of 2 there is only 1 smaller element (1).
        To the right of 6 there is 1 smaller element (1).
        To the right of 1 there is 0 smaller element.

Example 2:
    Input: nums = [-1]
    Output: [0]

Example 3:
    Input: nums = [-1,-1]
    Output: [0,0]

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
"""
from typing import List
from bisect import bisect_left
from collections import deque

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans, deq = [], deque([])

        for num in nums[::-1]:
            i = bisect_left(deq, num)
            deq.insert(i, num)
            ans.append(i)

        return ans[::-1]


if __name__ == "__main__":
    obj = Solution()
    tests = [
        [5, 2, 6, 1],
        [-1],
        [-1, -1],

    ]

    for t in tests:
        print(t)
        print(obj.countSmaller(t), end="\n\n")


# from random import randint
# def gen_test(length, max_n, min_n):
#     return [randint(min_n, max_n) for _ in range(length)]
# print(gen_test(100000, 5000, -5000))
