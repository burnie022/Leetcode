"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2
Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1
Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

Constraints:
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums contains distinct values sorted in ascending order.
    -10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo


# My old (interesting) solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     if target in nums:
    #         return nums.index(target)
    #     else:
    #         return sorted(nums+[target]).index(target)


if __name__ == "__main__":
    obj = Solution()
    tests = [

    ]

    for t in tests:
        print(t)
        print(obj(t), end="\n\n")
