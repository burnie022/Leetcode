"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that
i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.
Example 2:
    Input: nums = [5,4,3,2,1]
    Output: false
    Explanation: No triplet exists.
Example 3:
    Input: nums = [2,1,5,0,4,6]
    Output: true
    Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""
from typing import List
import math

def increasingTriplet(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False

    small, mid = nums[0], math.inf
    for n in nums[1:]:
        if n < small:
            small = n
        elif n < mid:
            mid = n
        else:
            return True
    return False



# Test cases

tests = [
    [1,2,3,4,5],
    [5,4,3,2,1],
    [2,1,5,0,4,6],
    [3,2,4,1,5],
    [1],
    [1,2],
    [1,2,1],
    [1,2,3],
    [2,5,3,4,5],
    [2,5,3,4],
    [9,8,7,6,5,6,5,4,3,4,3,2,1,2],
    [9,8,7,6,5,6,5,4,3,4,3,2,1,5],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [5,6,0]
]

for t in tests:
    print(t)
    print(increasingTriplet(t))