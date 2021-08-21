"""
Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is
no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.

Example 1: VIEW PIC: max_sum_grid_ex1.jpg
    Input: matrix = [[1,0,1],[0,-2,3]], k = 2
    Output: 2
    Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than
        k (k = 2).
Example 2:
    Input: matrix = [[2,2,-1]], k = 3
    Output: 3

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -100 <= matrix[i][j] <= 100
    -10^5 <= k <= 10^5

Follow up: What if the number of rows is much larger than the number of columns?
"""
from typing import List
import bisect


# A Leetcode solution
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        max_sum = float("-inf")

        for i in range(cols):
            sums = [0] * rows
            for j in range(i, cols):
                curr = [0]
                tot = 0
                for r in range(rows):
                    sums[r] += matrix[r][j]
                    tot += sums[r]
                    index = bisect.bisect_left(curr, tot - k)
                    if 0 <= index < len(curr):
                        max_sum = max(max_sum, tot - curr[index])
                    bisect.insort(curr, tot)

        return max_sum

#
do not commit until you have your own solution
#