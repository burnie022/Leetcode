"""
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to
move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You
 an apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the
grid boundary. Since the answer can be very large, return it modulo 109 + 7.

Example 1: VIEW PIC: out_of_boundary_paths_ex1.png
    Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
    Output: 6

Example 2: VIEW PIC: out_of_boundary_paths_ex2.png
    Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
    Output: 12

Constraints:
    1 <= m, n <= 50
    0 <= maxMove <= 50
    0 <= startRow < m
    0 <= startColumn < n

Hint #1
    WIll traversing every path is feasible? There are many possible paths for a small matrix. Try to optimize it.
Hint #2
    Can we use some space to store the number of paths and update them after every move?
Hint #3
    One obvious thing: the ball will go out of the boundary only by crossing it. Also, there is only one possible way
    the ball can go out of the boundary from the boundary cell except for corner cells. From the corner cell, the ball
    can go out in two different ways. Can you use this thing to solve the problem?
"""


class Solution:

    # this solution uses a 3d list and a bottom up approach for DP
    def findPaths(self, rows: int, cols: int, maxMove: int, startRow: int, startColumn: int) -> int:
        paths = ((-1, 0), (1, 0), (0, 1), (0, -1))
        memo = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(maxMove + 1)]

        for move in range(1, maxMove+1):
            for row in range(rows):
                for col in range(cols):
                    for a, b in paths:
                        memo[move][row][col] += memo[move-1][row+a][col+b] \
                            if 0 <= row + a < rows and 0 <= col + b < cols else 1

        return memo[maxMove][startRow][startColumn] % (10 ** 9 + 7)



    # # Brute force DFS with a lot of redundant recalculation (SLOW)
    # def findPathsBruteForce(self, rows: int, cols: int, maxMove: int, startRow: int, startColumn: int) -> int:
    #     paths = ((-1, 0), (1, 0), (0, 1), (0, -1))
    #
    #     def dfs(row=startRow, col=startColumn, moves=maxMove):
    #         if not 0 <= row < rows or not 0 <= col < cols:
    #             return 1
    #
    #         total = 0
    #         moves -= 1
    #         for a, b in paths:
    #             next_row, next_col = row + a, col + b
    #             if next_row + moves >= rows or next_row - moves < 0 or \
    #                 next_col + moves >= cols or next_col - moves < 0:
    #                 total += dfs(row + a, col + b, moves)
    #
    #         return total
    #
    #     return dfs() % (10 ** 9 + 7)



if __name__ == "__main__":
    obj = Solution()
    tests = [
        (2,2,2,0,0),
        (1,3,3,0,1),
        (8,8,5,2,2),
        (8, 8, 7, 2, 2),
        (8, 8, 9, 2, 2),
        (8, 8, 15, 2, 2),
        (4,4,12,2,2),
        (8,8,1,4,4),
        (8, 8, 25, 4, 4),
        (8, 8, 20, 4, 2),
        (8, 8, 35, 4, 4),
        (2, 50, 25, 1, 4),
        (50, 2, 25, 4, 1),
        (8, 8, 50, 4, 4),

    ]

    for t in tests:
        # print(t)
        for i in t:
            print(i)
        # print(obj.findPaths(*t), end="\n\n")

