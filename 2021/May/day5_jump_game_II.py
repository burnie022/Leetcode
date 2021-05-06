"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3
        steps to the last index.
Example 2:
    Input: nums = [2,3,0,1,4]
    Output: 2

Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps = 0
        pos = 0
        while nums[pos] + pos < len(nums) - 1:
            next_pos = furthest_jump = 0
            for i in range(pos+1, pos+nums[pos]+1):
                if nums[i] + i > furthest_jump:
                    next_pos, furthest_jump = i, nums[i] + i

            jumps += 1
            pos = next_pos

        return jumps if pos >= len(nums) - 1 else jumps + 1


# Test cases
obj = Solution()
tests = [
[2,3,1,1,4],
[2,3,0,1,4],
    [1],
    [1,1]

]

for t in tests:
    print(t)
    print(obj.jump(t), end="\n\n")


# from random import randint
# li = []
# for _ in range(950):
#     li.append(randint(0,1000))
# print(li)
