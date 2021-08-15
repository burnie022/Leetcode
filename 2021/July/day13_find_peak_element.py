"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return
the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:
    Input: nums = [1,2,1,3,5,6,4]
    Output: 5
    Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where
        the peak element is 6.

Constraints:
1 <= nums.length <= 1000
    -2^31 <= nums[i] <= 2^31 - 1
    nums[i] != nums[i + 1] for all valid i.
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + ((hi - lo) // 2)
            if mid + 1 <= hi and nums[mid+1] > nums[mid]:
                lo = mid + 1
            elif mid - 1 >= lo and nums[mid-1] > nums[mid]:
                hi = mid
            else:
                return mid
        return lo


if __name__ == "__main__":
    obj = Solution()
    tests = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [1,2,3,4,5,6],
        [6, 5, 4, 3, 2, 1],
        [1,2,3,4,5,6,1],
        [1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 1],
        [3, 4, 5, 6, 1, 2],
        [4, 5, 6, 1, 2, 3],
        [5, 6, 1, 2, 3, 4],
        [6, 1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 1],
        [3, 4, 5, 1, 2],
        [4, 5, 1, 2, 3],
        [5, 1, 2, 3, 4],
        [1, 2, 3, 4, 5],

    ]

    for t in tests:
        print(t)
        # print(obj.findPeakElement(t), end="\n\n")
