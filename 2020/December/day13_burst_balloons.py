"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented
by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get
nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After
the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
    You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
    0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:
    Input: [3,1,5,8]
    Output: 167
    Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
                 coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
from typing import List


def maxCoins(nums: List[int]) -> int:
    if not nums: return 0
    dp = [[0 for i in range(len(nums))] for j in range(len(nums))]

    for i in range(len(nums)):
        if i == 0 or i == len(nums) - 1:
            pass

    return 1


# A leetcode solution by user xliu20
# time complexity is O(n^3)

def maxCoinsLeetcode(nums: List[int]) -> int:
    nums = [1] + nums + [1]
    dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 2, len(nums)):
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])

    return dp[0][len(nums) - 1]


# Test cases
tests = [
    [3,1,5,8],
    [3,2,4,1,6,5],
    []
]

for t in tests:
    print(maxCoinsLeetcode(t))
