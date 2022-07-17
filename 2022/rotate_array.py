"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
        rotate 1 steps to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    Explanation:
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
    1 <= nums.length <= 10^5
    -2^31 <= nums[i] <= 2^31 - 1
    0 <= k <= 10^5

Follow up:
    Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?

"""
from typing import List


class Solution:
    # This solution uses O(1) extra memory
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_array_segment(arr, start, end):
            if arr:
                while end > start:
                    arr[start], arr[end] = arr[end], arr[start]
                    end -= 1
                    start += 1

        k %= len(nums)
        if k:
            reverse_array_segment(nums,0,len(nums) - 1)
            reverse_array_segment(nums,0,k - 1)
            reverse_array_segment(nums,k,len(nums) - 1)

            print(f"nums: {nums}")



   # This solution uses O(N) extra memory to create a new rotated array using list slicing
    def _rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k:
            nums = nums[-k:] + nums[:-k]

            print(nums)


if __name__ == "__main__":
    obj = Solution()
    tests = [
        ([1,2,3,4,5,6,7], 3),
        ([-1,-100,3,99], 2),
        ([1], 1),
        ([-1, -100, 3, 99], 3),
        ([-1, -100, 3, 99], 4),

    ]

    for t in tests:
        print(t[0])
        print(t[1])
        # print(obj.rotate(*t), end="\n\n")
