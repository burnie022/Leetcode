"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).



Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.


Constraints:

n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        changes = 0
        if nums[0] > nums[1]:
            nums[0] = nums[1]
            changes += 1

        a = b = nums[0]
        if len(nums) > 2:
            for i in range(1, len(nums) - 1):
                if nums[i] < a:
                    if changes:
                        return False
                    if nums[i] >= b:
                        a = b = nums[i]
                        changes += 1
                    elif nums[i+1] >= a:
                        changes += 1
                    else:
                        return False
                else:
                    a, b = nums[i], a

            if nums[-1] < nums[-2] and changes:
                print("caught the end")
                return False

        return True




# Test cases
obj = Solution()
tests = [
[4,2,3],
[4,2,1],
[1],
[1,2,3,3,3,3,3,3,2],
[4,2,2,2,2,2,3,1],
[1,2,3,3,3,3,3,3,2],
[1,2,3,3,8,3,3,3,3],
[1,2,3,3,-12,3,3,3,3],
[1,2,3,3,3,5,3,3,3],
[1,2,3,3,8,9,3,3,3],
[1,2,3,3,-12, 1,3,3,3,3],
[1,2,3,3,3,5,4,3,3],
[1,2,3,3,-12,3,3,3,3,1],


]


for t in tests:
    print(t)
    # print(obj.checkPossibility(t), end="\n\n")
