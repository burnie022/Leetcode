"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
You must do it in place.

Example 1: VIEW EXAMPLE PIC: set_matrix_zeroes_ex1.jpg
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2: VIEW EXAMPLE PIC: set_matrix_zeroes_ex2.jpg
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1

Follow up:
    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
Hint #1
    If any cell of the matrix has a zero we can record its row and column number using additional memory. But if you
    don't want to use extra memory then you can manipulate the array instead. i.e. simulating exactly what the
    question says.
Hint #2
    Setting cell values to zero on the fly while iterating might lead to discrepancies. What if you use some other
    integer value as your marker? There is still a better approach for this problem with 0(1) space.
Hint #3
    We could have used 2 sets to keep a record of rows/columns which need to be set to zero. But for an O(1) space
    solution, you can use one of the rows and and one of the columns to keep track of this information.
Hint #4
    We can use the first cell of every row and column as a flag. This flag would determine whether a row or column
    has been set to zero.
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_col, first_row = not all(matrix[row][0] for row in range(len(matrix))), not all(matrix[0])

        if len(matrix) > 1 and len(matrix[0]) > 1:
            for row in range(1, len(matrix)):
                for col in range(1, len((matrix[0]))):
                    if matrix[row][col] == 0:
                        matrix[row][0] = 0
                        matrix[0][col] = 0

            for row in range(len(matrix)):
                for col in range(len((matrix[0]))):
                    if matrix[row][col] is None:
                        matrix[row][col] = 0

            for col in range(1, len((matrix[0]))):
                if matrix[0][col] == 0:
                    for row in range(1, len(matrix)):
                        matrix[row][col] = 0

            for row in range(1, len(matrix)):
                if matrix[row][0] == 0:
                    for col in range(1, len(matrix[0])):
                        matrix[row][col] = 0

        if first_col:
            for row in range(len(matrix)):
                matrix[row][0] = 0
        if first_row:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0


        # return matrix

# Second solution is good but was slightly slower on leetcode
    def setZeroesSol2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def set_cols_to_none(row):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][col] = None
                    set_rows_to_none(col)
                else:
                    matrix[row][col] = None

        def set_rows_to_none(col):
            for row in range(len(matrix)):
                if matrix[row][col] == 0:
                    matrix[row][col] = None
                    set_cols_to_none(row)
                else:
                    matrix[row][col] = None

        for row in range(len(matrix)):
            for col in range(len((matrix[0]))):
                if matrix[row][col] == 0:
                    matrix[row][col] = None
                    set_cols_to_none(row)
                    set_rows_to_none(col)

        for row in range(len(matrix)):
            for col in range(len((matrix[0]))):
                if matrix[row][col] is None:
                    matrix[row][col] = 0

        return matrix


if __name__ == "__main__":
    obj = Solution()
    tests = [
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
        [[0, 9, 6, 6, 3, 8, 7, 0, 6, 8, 5, 9, 9, 8, 8, 2, 8, 0, 8, 2, 2, 6, 0, 9, 4],
         [10, 0, 1, 4, 2, 5, 0, 1, 8, 5, 10, 1, 0, 5, 10, 5, 0, 6, 9, 6, 6, 3, 0, 0, 8],
         [8, 5, 1, 8, 10, 6, 9, 7, 3, 2, 8, 1, 9, 3, 1, 5, 10, 8, 4, 9, 3, 0, 4, 2, 2],
         [4, 3, 0, 7, 1, 2, 0, 8, 9, 9, 10, 3, 0, 4, 2, 8, 5, 9, 6, 6, 1, 9, 7, 5, 4],
         [9, 8, 6, 2, 2, 7, 6, 1, 9, 10, 5, 10, 6, 8, 10, 4, 0, 10, 9, 2, 10, 10, 2, 5, 6],
         [3, 9, 10, 10, 10, 9, 3, 3, 9, 5, 0, 9, 3, 2, 0, 9, 4, 6, 8, 0, 2, 7, 1, 4, 5],
         [1, 10, 6, 4, 10, 3, 5, 0, 5, 4, 6, 6, 2, 6, 5, 0, 9, 10, 1, 0, 2, 8, 9, 8, 9],
         [4, 1, 8, 7, 1, 2, 9, 8, 0, 4, 5, 5, 10, 0, 6, 6, 3, 5, 0, 9, 2, 3, 9, 2, 10],
         [1, 1, 2, 2, 9, 5, 5, 7, 9, 5, 10, 4, 4, 10, 6, 2, 2, 0, 2, 10, 9, 5, 7, 8, 10],
         [0, 1, 10, 8, 8, 8, 2, 0, 7, 10, 8, 10, 2, 10, 4, 9, 2, 5, 10, 2, 6, 0, 7, 2, 3],
         [8, 3, 0, 5, 4, 4, 2, 10, 1, 1, 1, 1, 8, 5, 8, 8, 8, 2, 8, 8, 2, 0, 0, 5, 10],
         [8, 5, 7, 8, 2, 10, 0, 2, 1, 5, 3, 8, 10, 0, 0, 1, 6, 1, 7, 7, 0, 7, 5, 2, 9],
         [0, 3, 10, 10, 5, 8, 9, 10, 3, 0, 9, 10, 10, 4, 9, 7, 2, 5, 0, 2, 7, 2, 6, 0, 3],
         [8, 10, 9, 6, 5, 0, 9, 2, 7, 1, 4, 9, 5, 1, 4, 7, 6, 7, 7, 8, 4, 7, 5, 8, 2],
         [4, 6, 2, 9, 9, 6, 0, 0, 6, 6, 10, 4, 6, 4, 7, 3, 3, 8, 8, 7, 2, 5, 0, 2, 3],
         [5, 9, 3, 9, 2, 5, 1, 10, 1, 9, 9, 2, 8, 7, 0, 6, 3, 10, 5, 4, 0, 5, 0, 10, 5],
         [7, 10, 4, 8, 3, 5, 5, 0, 10, 1, 7, 7, 7, 7, 1, 1, 1, 5, 2, 7, 5, 6, 5, 5, 7],
         [9, 9, 0, 4, 2, 5, 8, 1, 1, 9, 0, 4, 5, 5, 6, 0, 0, 4, 3, 1, 10, 6, 9, 9, 4],
         [8, 7, 7, 3, 4, 5, 7, 8, 8, 2, 3, 4, 3, 6, 0, 0, 1, 1, 9, 0, 0, 3, 4, 2, 1],
         [4, 8, 0, 7, 2, 2, 5, 7, 8, 3, 10, 2, 5, 5, 7, 10, 0, 2, 8, 2, 8, 2, 4, 9, 8]]
    ]

    for t in tests:
        print(t)
        m = obj.setZeroes(t)
        for r in m:
            print(r)
        print("")


    # from random import randint
    # def gen_test(rows, cols):
    #     m = []
    #     for _ in range(rows):
    #         row = []
    #         for _ in range(cols):
    #             row.append(randint(0,150))
    #         m.append(row)
    #     return m
    #
    # print(gen_test(200, 190))
