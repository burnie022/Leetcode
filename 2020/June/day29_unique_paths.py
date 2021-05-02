"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
 Start |       |       |       |       |       |
_______________________________________________________
       |       |       |       |       |       |
_______________________________________________________
       |       |       |       |       |       | Finish
_______________________________________________________

Above is a 7 x 3 grid. How many possible unique paths are there?

Example 1:
    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Right -> Down
    2. Right -> Down -> Right
    3. Down -> Right -> Right
Example 2:
    Input: m = 7, n = 3
    Output: 28
Constraints:
    1 <= m, n <= 100
    It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
"""

def uniquePaths(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    rows, cols = n, m
    table = [[1 for j in range(cols)] for i in range(rows)]

    for row in range(1, rows):
        for col in range(1, cols):
            table[row][col] = table[row - 1][col] + table[row][col - 1]

    # for row in table:
    #     print(row)

    return table[-1][-1]


# For testing

tests = [(7,7)]

for m, n in tests:
    print(uniquePaths(m, n))
