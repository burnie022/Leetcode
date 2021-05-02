"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true
Example 2:
    Input: nums = [2,5,6,0,0,1,2], target = 3
    Output: false
Follow up:
    This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
    Would this affect the run-time complexity? How and why?
"""

def search(nums, target: int) -> bool:
    return target in nums

# Test cases
tests = [
    ([2,5,6,0,0,1,2], 0),
    ([2,5,6,0,0,1,2], 3),
    ([7,8,9,0,1,2,3,4,5,6], 10),
    ([2,3,4,5,6,7,8,9,0,1], 0),
    ([6,7,8,8,9,9,0,0,1,2,2,3,4,4,5], 9),
    ([6,7,8,8,9,9,9,0,0,1,2,2,3,4,4,5,5], 2)
]

for n, t in tests:
    print(search(n, t))

