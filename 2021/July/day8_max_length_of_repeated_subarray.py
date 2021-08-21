"""
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1:
    Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
    Output: 3
    Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:
    Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
    Output: 5

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 100
Hint #1
    Use dynamic programming. dp[i][j] will be the answer for inputs A[i:], B[j:].
"""
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums1) + 1)] for _ in range(len(nums2) + 1)]
        max_len = 0
        for r in range(len(nums2)):
            for c in range(len(nums1)):
                if nums1[c] == nums2[r]:
                    dp[r + 1][c + 1] = dp[r][c] + 1
                    max_len = max(max_len, dp[r + 1][c + 1])

        return max_len


# dp[r+1][c+1] = max(dp[r][c+1], dp[r+1][c], dp[r][c] + 1) \
#     if nums1[c] == nums2[r] else max(dp[r][c+1], dp[r+1][c])


if __name__ == "__main__":
    obj = Solution()
    tests = [
        ([1,2,3,2,1], [3,2,1,4,7]),
        ([0,0,0,0,0], [0,0,0,0,0]),
        ([1], [1]),
        ([1], [0]),
        ([0,1,1,1,1], [1,0,1,0,1]), # 21 / 55 test cases passed. Output: 3  Expected: 2
        ([0,1,2,0,1,2,3,1,4,5,6], [3,4,5,1,0,1,2,3,4]),
        ([0,1,2,0,1,2,3,1,4,5,6], [3,4,5,6,1,0,1,2,3,1,4]),
        ([0,1,2,0,1,2,3,1,4,5,6], [3,4,5,1,0,1,2,2,3,1,4,5,6]),
        ([0,1,2,0,1,2,3,1,4,5,6], [3,4,5,1,0,1,2,3,1,4,5,6]),
    ]

    for t in tests:
        print(t[0])
        print(t[1])
        # print(obj.findLength(*t), end="\n\n")
