"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space is marked as 1 and 0 respectively in the grid.

Example 1:
    VIEW PIC: unique_paths_II_ex1.jpg
    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    Explanation: There is one obstacle in the middle of the 3x3 grid above.
        There are two ways to reach the bottom-right corner:
        1. Right -> Right -> Down -> Down
        2. Down -> Down -> Right -> Right
    Example 2:
        VIEW PIC: unique_paths_II_ex2.jpg
    Input: obstacleGrid = [[0,1],[0,0]]
    Output: 1

Constraints:
    m == obstacleGrid.length
    n == obstacleGrid[i].length
    1 <= m, n <= 100
    obstacleGrid[i][j] is 0 or 1.
Hint #1
    The robot can only move either down or right. Hence any cell in the first row can only be reached from the cell
    left to it. However, if any cell has an obstacle, you don't let that cell contribute to any path. So, for the
    first row, the number of ways will simply be
        if obstacleGrid[i][j] is not an obstacle
             obstacleGrid[i,j] = obstacleGrid[i,j - 1]
        else
             obstacleGrid[i,j] = 0
    You can do a similar processing for finding out the number of ways of reaching the cells in the first column.
Hint #2
    For any other cell, we can find out the number of ways of reaching it, by making use of the number of ways of
    reaching the cell directly above it and the cell to the left of it in the grid. This is because these are the
    only two directions from which the robot can come to the current cell.
Hint #3
    Since we are making use of pre-computed values along the iteration, this becomes a dynamic programming problem.
        if obstacleGrid[i][j] is not an obstacle
             obstacleGrid[i,j] = obstacleGrid[i,j - 1]  + obstacleGrid[i - 1][j]
        else
             obstacleGrid[i,j] = 0
"""
from typing import List

# My answers implement dynamic programming for O(n) time complexity and O(n) space complexity
# Both of the below functions work correctly and efficiently; The first works from the top-left to bottom-right,
# the second from bottom-right to top left.
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1 or (
                ((rows == 1 and any(obstacleGrid[0])) or (
                        cols == 1 and any(obstacleGrid[r][0] for r in range(rows))))):
            return 0
        if rows == 1 or cols == 1:
            return 1
        paths = [[0 for j in range(cols)] for i in range(rows)]
        paths[0][0] = 1
        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] != 1 and not (row == 0 and col == 0):
                    left = 0 if (col-1 < 0 or obstacleGrid[row][col-1]) else paths[row][col-1]
                    top = 0 if (row-1 < 0 or obstacleGrid[row-1][col]) else paths[row-1][col]
                    paths[row][col] = left + top

        # for row in paths:
        #     print(row)

        return paths[-1][-1]

    def uniquePathsWithObstaclesReversedTraversal(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1 or (
                ((rows == 1 and any(obstacleGrid[0])) or (
                        cols == 1 and any(obstacleGrid[r][0] for r in range(rows))))):
            return 0
        if rows == 1 or cols == 1:
            return 1
        paths = [[0 for j in range(cols)] for i in range(rows)]
        paths[-1][-1] = 1
        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                if obstacleGrid[row][col] == 1 or row == rows - 1 and col == cols -1:
                    continue
                right = 0 if (col+1 == cols or obstacleGrid[row][col+1]) else paths[row][col+1]
                bottom = 0 if (row+1 == rows or obstacleGrid[row+1][col]) else paths[row+1][col]
                paths[row][col] = right + bottom

        return paths[0][0]


# For testing
obj = Solution()

tests = [
[[0,0,0],[0,1,0],[0,0,0]],
[[0,1],[0,0]],
[[0,0,0,0],[0,1,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]],
[[0,0],[0,1]],
[[1,0],[0,0]],
    [[0,0,0,0]],
    [[0],[0],[0],[0]],
    [[0, 1, 0, 0]],
    [[0], [0], [1], [0]],
[[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1], [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1], [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0]],
]

for t in tests:
    # print(t)
    print(obj.uniquePathsWithObstacles(t))


# from random import randint
#
# def generate_grid(rows, cols):
#     grid = []
#     for row in range(rows):
#         new_row = []
#         for col in range(cols):
#             new_row.append(randint(0,3))
#         grid.append(new_row)
#     grid[0][0] = grid[-1][-1] = 0
#     for row in range(rows):
#         for col in range(cols):
#             if grid[row][col] > 1:
#                 grid[row][col] = 0
#
#     return grid
#
#
# print(generate_grid(80, 80))
