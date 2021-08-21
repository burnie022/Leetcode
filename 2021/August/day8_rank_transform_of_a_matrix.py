"""
Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

The rank is an integer that represents how large an element is compared to other elements. It is calculated using the
following rules:

    The rank is an integer starting from 1.
    If two elements p and q are in the same row or column, then:
        If p < q then rank(p) < rank(q)
        If p == q then rank(p) == rank(q)
        If p > q then rank(p) > rank(q)
    The rank should be as small as possible.

It is guaranteed that answer is unique under the given rules.

Example 1: VIEW EXAMPLE PIC: rank_transform_ex1.jpg
    Input: matrix = [[1,2],[3,4]]
    Output: [[1,2],[2,3]]
    Explanation:
        The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
        The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
        The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
        The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both
            matrix[0][1] and matrix[1][0] are rank 2.
Example 2: VIEW EXAMPLE PIC: rank_transform_ex2.jpg
    Input: matrix = [[7,7],[7,7]]
    Output: [[1,1],[1,1]]
Example 3: VIEW EXAMPLE PIC: rank_transform_ex3.jpg
    Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
    Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
Example 4: VIEW EXAMPLE PIC: rank_transform_ex4.jpg
    Input: matrix = [[7,3,6],[1,4,5],[9,8,2]]
    Output: [[5,1,4],[1,2,3],[6,3,1]]

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 500
    -10^9 <= matrix[row][col] <= 10^9

Hint #1
    Sort the cells by value and process them in increasing order.
Hint #2
    The rank of a cell is the maximum rank in its row and column plus one.
Hint #3
    Handle the equal cells by treating them as components using a union-find data structure.
"""
from typing import List
from bisect import bisect_left


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        rank = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        min_row, min_col = [row[:] for row in matrix], \
                           [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]

        # for i in range(len(min_row)):
        #     min_row[i] = sorted(min_row[i])
        # for i in range(len(min_col)):
        #     min_col[i] = sorted(min_col[i])


        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                s = set(min_row[row])
                s.update(min_col[col])
                s = sorted(s)
                i = bisect_left(s, matrix[row][col])
                rank[row][col] = i + 1

        # for r in range(len(matrix)):
        #     for c in range(len(matrix[0])):
        #         rank[r][c] = 1 + (matrix[r][c] - rank[r][c])

        for row in rank:
            print(f"    {row}")
        return rank

no good

    def matrixRankTransformLC(self, matrix: List[List[int]]) -> List[List[int]]:
        rank = [0] * (len(matrix) + len(matrix[0]))
        result = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        vals = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] not in vals:
                    vals[matrix[i][j]] = [(i,j)]
                else:
                    vals[matrix[i][j]].append((i,j))

        def find(p):
            if p != parent[p]:
                parent[p] = find(parent[p])
            return parent[p]

        for k in sorted(vals):
            parent = list(range(len(matrix) + len(matrix[0])))

            for i, j in vals[k]:
                a, b = find(i), find(len(matrix) + j)
                parent[a] = b
                rank[b] = max(rank[a], rank[b])

            seen = set()
            for i, j in vals[k]:
                a = find(i)
                if a not in seen:
                    rank[a] += 1
                seen.add(a)
                rank[i] = rank[len(matrix) + j] = result[i][j] = rank[a]

        return result


if __name__ == "__main__":
    obj = Solution()
    tests = [
        [[1, 2], [3, 4]],
        [[7, 7], [7, 7]],
        [[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]],
        [[7, 3, 6], [1, 4, 5], [9, 8, 2]],
    ]

    for t in tests:
        print(t)
        # print(obj.matrixRankTransformLC(t), end="\n\n")
