"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to
target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Constraints:
    3 <= nums.length <= 10^3
    -10^3 <= nums[i] <= 10^3
    -10^4 <= target <= 10^4
"""
from typing import List
from bisect import bisect_left


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        self.closest = None
        diff = 10000

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                n = target - (nums[i] + nums[j])
                k = bisect_left(nums, n, j + 1)
                if k < len(nums) and nums[k] == n:
                    return target

                a = nums[i] + nums[j] + nums[k] if k < len(nums) else nums[i] + nums[j] + nums[-1]
                b = nums[i] + nums[j] + nums[k - 1] if k > j + 1 else a
                c = a if abs(target - a) < abs(target - b) else b
                if abs(target - c) < diff:
                    diff += -diff + abs(target - c)
                    self.closest = c

        return self.closest


if __name__ == "__main__":
    obj = Solution()
    tests = [
        ([-1,2,1,-4], 1),
        ([23, 49, 20, -33, -26, 48, 46, -49, 22, 15, 1, -21, 13, -5, 17, 20, -21, 17, 33, 22, 42, 33, 21, -27, -50], 8),
        ([23, 49, 20, -33, -26, 48, 46, -49, 22, 15, 1, -21, 13, -5, 17, 20, -21, 17, 33, 22, 42, 33, 21, -27, -50], 105),
        ([23, 49, 20, -33, -26, 48, 46, -49, 22, 15, 1, -21, 13, -5, 17, 20, -21, 17, 33, 22, 42, 33, 21, -27, -50], -99),
        ([23, 49, 20, -33, -26, 48, 46, -49, 22, 15, 1, -21, 13, -5, 17, 20, -21, 17, 33, 22, 42, 33, 21, -27, -50], 118),
        ([23, 49, 20, -33, -26, 48, 46, -49, 22, 15, 1, -21, 13, -5, 17, 20, -21, 17, 33, 22, 42, 33, 21, -27, -50], -89),
        ([23, 49, 20, -33, -26, 48, 46, -49, 22, 15, 1, -21, 13, -5, 17, 20, -21, 17, 33, 22, 42, 33, 21, -27, -50], 500),
        ([23, 49, 20, -33, -26, 48, 46, -49, 22, 15, 1, -21, 13, -5, 17, 20, -21, 17, 33, 22, 42, 33, 21, -27, -50], -508),
        ([-1,0,1,1,55], 3)
    ]

    for t in tests:
        print(t[0])
        print(t[1])
        print(obj.threeSumClosest(*t), end="\n\n")

    # from random import randint
    # print([randint(-50, 50) for _ in range(25)])
