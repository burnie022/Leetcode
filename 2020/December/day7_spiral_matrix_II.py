"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in
spiral order.

Example 1:
    VIEW PIC FOR THIS EXAMPLE spiral_matt_II.jpg IN DECEMBER FOLDER

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
    Input: n = 1
    Output: [[1]]

Constraints:
1 <= n <= 20
"""
import numpy as np


def generateMatrix(n: int):
    matrix = np.array([[0 for _ in range(n)] for _ in range(n)])
    k = 1
    for row in range(int(n/2) + 1):
        for _ in range(4):
            for col in range(n):
                if matrix[row][col] == 0:
                    matrix[row][col] = k
                    k += 1
            matrix = np.flip(matrix, 1).transpose()

    return matrix


# Test cases

for i in range(1, 8):
    m = generateMatrix(i)
    for row in m:
        print(row)
    print("")

