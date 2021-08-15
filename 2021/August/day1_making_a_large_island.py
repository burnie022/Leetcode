"""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.

Example 1:
    Input: grid = [[1,0],[0,1]]
    Output: 3
    Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:
    Input: grid = [[1,1],[1,0]]
    Output: 4
    Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:
    Input: grid = [[1,1],[1,1]]
    Output: 4
    Explanation: Can't change any 0 to 1, only one island with area = 4.

Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 500
    grid[i][j] is either 0 or 1.
"""
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        islands = {0: 0}
        dir = [(1,0), (-1,0), (0,1), (0,-1)]
        island, max_size = 2, 0

        def dfs(row, col, i):
            if not 0 <= row < len(grid) or not 0 <= col < len(grid) or grid[row][col] != 1:
                return
            grid[row][col] = i
            islands[i] += 1
            for r, c in dir:
                dfs(row + r, col + c, i)

        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] == 1:
                    islands[island] = 0
                    dfs(r, c, island)
                    island += 1

        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] == 0:
                    neighbors = set()
                    size = 1
                    for a, b in dir:
                        if 0 <= row + a < len(grid) and 0 <= col + b < len(grid):
                            neighbors.add(grid[row + a][col + b])
                    for n in neighbors:
                        size += islands[n]
                    max_size = max(max_size, size)

        return max(max_size, *islands.values())

if __name__ == "__main__":
    obj = Solution()
    tests = [
        [[1, 0], [0, 1]],
        [[1, 1], [1, 0]],
        [[1, 1], [1, 1]],
        [[0,0,0,0,0,0],
         [0,1,1,1,1,0],
         [0,1,0,1,1,0],
         [0,1,0,1,1,0],
         [0,1,1,1,1,0],
         [0,0,0,0,0,0]],
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],],
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    ]

    for t in tests:
        print(t)
        print(obj.largestIsland(t), end="\n\n")
