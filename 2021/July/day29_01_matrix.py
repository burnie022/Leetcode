"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1: VIEW PIC: 01_matrix_ex1.jpg
    Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
    Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2: VIEW PIC 01_matrix_ex1.jpg
    Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
    Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 10^4
    1 <= m * n <= 10^4
    mat[i][j] is either 0 or 1.
    There is at least one 0 in mat.
"""
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist = [[10000 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    dist[row][col] = 0
                elif col > 0:
                    dist[row][col] = min(dist[row][col-1] + 1, dist[row][col])

        for row in range(len(mat)):
            for col in range(len(mat[0]) - 1, -1, -1):
                if mat[row][col] == 0:
                    dist[row][col] = 0
                elif col < len(mat[0]) - 1:
                    dist[row][col] = min(dist[row][col + 1] + 1, dist[row][col])

        for col in range(len(mat[0])):
            for row in range(len(mat)):
                if mat[row][col] == 0:
                    dist[row][col] = 0
                elif row > 0:
                    dist[row][col] = min(dist[row-1][col] + 1, dist[row][col])

        for col in range(len(mat[0])):
            for row in range(len(mat) - 1, -1, -1):
                if mat[row][col] == 0:
                    dist[row][col] = 0
                elif row < len(mat) - 1:
                    dist[row][col] = min(dist[row+1][col] + 1, dist[row][col])

        return dist


if __name__ == "__main__":
    obj = Solution()
    tests = [
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
        [[1, 1, 1], [1, 1, 1], [1, 1, 0]],
        [[1, 1, 1], [1, 1, 1], [0, 1, 1]],
        [[0, 1, 1], [1, 1, 1], [1, 1, 1]],
        [[1, 1, 0], [1, 1, 1], [1, 1, 1]],
        [[1,1,1,1,1,1,1,1,1,1,0]],
        [[0,1,1,1,1,1,1,1,1,1,1]],
        [[1,1,1,1,1,0,1,1,1,1,1,1]],
        [[1,0,0,0,0,0,0,0,0]],
        [[1,0,0,0,0,0,0,0,0,1]],
        [[1],[1],[1],[1],[1],[1],[1],[1],[0]],
        [[0],[1],[1],[1],[1],[1],[1],[1],[1]],
        [[1],[1],[0],[1],[1],[1],[1],[1],[1]],
        [[1],[1],[0],[1],[1],[1],[1],[1],[0]],
    ]

    # for t in tests:
    #     print(t)
    #     # print(obj.updateMatrix(t), end="\n\n")

    print([[1 for _ in range(100)] for _ in range(100)])
