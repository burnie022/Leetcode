"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned
into two subsets such that the sum of elements in both subsets is equal.

Example 1:
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:
    Input: nums = [1,2,3,5]
    Output: false
    Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

class Solution:
    def canPartition(self, nums) -> bool:
        total = sum(nums)
        if total % 2 != 0 or len(nums) < 2:
            return False
        if all(i == nums[0] for i in nums):
            return True
        self.found = False
        dp_memo = set()
        nums = list(reversed(sorted(nums)))

        def dfs(remainder, nums):
            if remainder == 0:
                self.found = True
                return
            if self.found or remainder < 0 or not nums or (remainder, len(nums)) in dp_memo:
                return
            dp_memo.add((remainder, len(nums)))
            dfs(remainder, nums[1:])
            dfs(remainder - nums[0], nums[1:])

        dfs(int(total / 2), nums)
        return self.found


# Test cases
s = Solution()

tests = [
    [1, 5, 11, 5],
    [1, 2, 3, 5],
    [8, 3, 5, 6, 8, 2, 4, 5, 1, 6, 10, 3, 6, 7],
    [8, 3, 5, 6, 8, 2, 4, 5, 1, 6, 10, 3, 6, 6],
    [5, 3, 10, 12, 2, 6, 4, 1, 5, 6, 3, 9, 4, 4, 8, 2, 4, 10, 2, 6],
    [5, 3, 10, 12, 17, 2, 6, 4, 1, 5, 6, 3, 9, 4, 4, 8, 13, 2, 4, 10, 2, 6],
    [5, 3, 10, 12, 2, 6, 4, 1, 15, 5, 6, 3, 9, 4, 4, 8, 2, 21, 4, 10, 2, 6],
    [5, 3, 10, 12, 2, 6, 4, 1, 5, 6, 3, 9, 4, 4, 8, 2, 4, 9, 13, 10, 2, 6],
    [5, 3, 10, 12, 2, 6, 4, 1, 5, 6, 3, 9, 4, 4, 8, 44, 12, 26, 40, 2, 4, 9, 13, 10, 2, 6],
    [4, 2, 4, 2],
    [100],
    [5, 5],
    [7, 2],
    [6, 4]
]

for t in tests:
    print(s.canPartition(t))
