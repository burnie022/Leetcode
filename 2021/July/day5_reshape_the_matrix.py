"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different
size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted
reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as
they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output
the original matrix.

Example 1:
    Input: mat = [[1,2],[3,4]], r = 1, c = 4
    Output: [[1,2,3,4]]
Example 2:
    Input: mat = [[1,2],[3,4]], r = 2, c = 4
    Output: [[1,2],[3,4]]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    -1000 <= mat[i][j] <= 1000
    1 <= r, c <= 300

Hint #1
    Do you know how 2d matrix is stored in 1d memory? Try to map 2-dimensions into one.
Hint #2
    M[i][j]=M[n*i+j] , where n is the number of cols. This is the one way of converting 2-d indices into one 1-d index.
    Now, how will you convert 1-d index into 2-d indices?
Hint #3
    Try to use division and modulus to convert 1-d index into 2-d indices.
Hint #4
    M[i] => M[i/n][n%i] Will it result in right mapping? Take some example and check this formula.
"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        mat = [item for li in mat for item in li]
        return [mat[col: col+c] for col in range(0, r*c, c)]


if __name__ == "__main__":
    obj = Solution()
    tests = [
        ([[1,2],[3,4]], 1, 4),
        ([[1,2],[3,4]], 2, 4),
        ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 25, 1),
        ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 1, 25),
        ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 2, 10),
        ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 3, 9),
    ]

    for t in tests:
        print(t)
        print(obj.matrixReshape(*t), end="\n\n")


    def gen_matrix(r, c):
        mat = [i for i in range(1, (r*c) + 1)]
        return [mat[col: col + c] for col in range(0, r * c, c)]

    # m = gen_matrix(9, 6)
    # # for r in m:
    # #     print(r)
    # print(m)