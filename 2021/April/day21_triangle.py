"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i
on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
    Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11
    Explanation: The triangle looks like:
       2
      3 4
     6 5 7
    4 1 8 3
    The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:
    Input: triangle = [[-10]]
    Output: -10

Constraints:
    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -104 <= triangle[i][j] <= 104

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""
import random
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        lower = triangle.pop()

        while triangle:
            upper = triangle.pop()
            for i in range(len(upper)):
                upper[i] += min(lower[i], lower[i+1])
            lower = upper

        return lower[0]


# For testing

def triangle_maker(n, min_num=-10, max_num=10):
    tri = []
    i = 1
    while i < n + 1:
        row = []
        for _ in range(i):
            row.append(random.randint(min_num, max_num))
        tri.append(row)
        i += 1

    return tri


# print(triangle_maker(200, -10000, 10000))

tests = [
    [[2],[3,4],[6,5,7],[4,1,8,3]],
    [[-10]],
[[1], [-8, -10], [-8, 1, -1], [10, -1, -4, -1], [-1, 8, -9, -8, -10], [-10, -3, -9, -1, -1, -6], [-6, 0, 5, 1, 5, -4, 8], [-7, 1, 5, 8, 7, 2, 8, -5]]

]

sol = Solution()

for t in tests:
    # print(t)
    print(sol.minimumTotal(t))



