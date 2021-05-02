"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each
number sorted in non-decreasing order.

Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].
Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.
"""
from typing import List


# Easy solution that doesn't take into account sorted nature of nums
def sortedSquaresOneLiner(nums: List[int]) -> List[int]:
    return sorted(i ** 2 for i in nums)


# this code creates a new list of nums sorted with all n in nums positve and then squares them
def sortedSquares(nums: List[int]) -> List[int]:
    i, j = len(nums) - 1, 0
    sorted_abs_nums = []
    while i >= j:
        # if nums[i] < 1:
        #     while j <= i:
        #         sorted_abs_nums.append(-nums[j])
        #         j += 1
        # elif nums[j] > -1:
        #     while j <= i:
        #         sorted_abs_nums.append((nums[i]))
        #         i -= 1
        if abs(nums[i]) >= abs(nums[j]):
            sorted_abs_nums.append(nums[i]**2)
            i -= 1
        else:
            sorted_abs_nums.append(nums[j]**2)
            j += 1

    return sorted_abs_nums[::-1]

# Test cases

tests = [
[-4,-1,0,3,10],
[-7,-3,2,3,11],
[ -7, -1, 0, 1, 2, 3, 4, 5, 7],
[ -7, -1, 0, 1, 2, 3, 4, 5, 7, 8]
]

for t in tests:
    print(sortedSquares(t), end="\n\n")

