"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target
value.
If target is not found in the array, return [-1, -1].
Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
Example 3:
    Input: nums = [], target = 0
    Output: [-1,-1]

Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        nums = [nums[0]-1] + nums + [nums[-1]+1]
        result = []

        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + int((hi - lo) / 2)
            # print(f"lo: {lo}, mid: {mid}, hi: {hi}")
            if nums[mid] < target and nums[mid + 1] == target:
                result.append(mid)
                break
            elif nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1

        # print("finished first loop")
        if len(result) == 0:
            return [-1, -1]

        lo = result[0]
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + int((hi - lo) / 2)
            if nums[mid] > target and nums[mid-1] == target:
                result.append(mid - 2)
                return result
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        # return result


        # lo = result[0]
        # hi = len(nums) - 2
        # while lo <= hi:
        #     mid = lo + int((hi - lo) / 2)
        #     if nums[mid] > target and nums[mid-1] == target:
        #         result.append(mid - 2)
        #         return result
        #     elif nums[mid] > target:
        #         hi = mid - 1
        #     else:
        #         lo = mid + 1
        #
        # return result


# For testing
obj = Solution()
tests = [
    ([5,7,7,8,8,10], 8),
    ([5,7,7,8,8,10], 6),
    ([], 0),
    ([5,7,8,8,10], 7),
    ([1,2,3,4,5,6,7,8,9], 2),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
    ([1, 2,2,2, 3, 4, 5, 6, 7, 8, 9], 2),
    ([1, 2,2, 3, 4, 5, 6, 7, 8, 9], 2),
    ([1, 2,2,2,2, 3, 4, 5, 6, 7, 8, 9], 2),
    ([1, 2,2,2,2,2, 3, 4, 5, 6, 7, 8, 9], 2),
    ([1], 1)


]

for n, t in tests:
    print(n)
    print(t)
    print(obj.searchRange(n, t), end="\n\n")


# from random import randint
# def gen_sorted_repeating_nums(length):
#     li = []
#     i = -10
#     while len(li) < length:
#         li = li + ([i] * randint(0, 5))
#         i += 1
#     return li
#
# lengths = [500, 500, 601, 601, 601, 601, 601, 1001, 1001, 1001, 1001]
# for l in lengths:
#     print(gen_sorted_repeating_nums(l))



