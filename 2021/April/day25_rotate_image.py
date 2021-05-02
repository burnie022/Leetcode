"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT
allocate another 2D matrix and do the rotation.

Example 1:
    VIEW PIC rotate_image_ex1.jpg
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:
    VIEW PIC rotate_image_ex1.jpg
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
Example 3:
    Input: matrix = [[1]]
    Output: [[1]]
Example 4:
    Input: matrix = [[1,2],[3,4]]
    Output: [[3,1],[4,2]]

Constraints:
    matrix.length == n
    matrix[i].length == n
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start = 0
        n = len(matrix)
        while start <= n / 2:
            end = n - start - 1
            for i in range(start, end):
                # matrix[row][row+i], matrix[row+i][end], matrix[end][end-i], matrix[end-i][row] = \
                #     matrix[end-i][row], matrix[row][row+i], matrix[row+i][end], matrix[end][end-i]


                matrix[i][end], matrix[end][n-i-1], matrix[n-1-i][start], matrix[start][i] = \
                    matrix[start][i], matrix[i][end], matrix[end][n-1-i], matrix[n-1-i][start]

            start += 1

        for start in matrix:
            print(start)




# For testing

obj = Solution()

tests = [
[[1,2,3],[4,5,6],[7,8,9]],
[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
[[1,2],[3,4]],
[[1]],
[[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
[16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
[31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45],
[46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
[61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75],
[76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
[91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105],
[106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
[121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135],
[136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150],
[151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165],
[166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180],
[181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195],
[196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
[211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225]],
    [[1, 2, 3, 4, 5, 6],
[7, 8, 9, 10, 11, 12],
[13, 14, 15, 16, 17, 18],
[19, 20, 21, 22, 23, 24],
[25, 26, 27, 28, 29, 30],
[31, 32, 33, 34, 35, 36]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
[13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
[37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
[49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
[61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72],
[73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
[85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96],
[97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108],
[109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
[121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132],
[133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144]]
]

for matrix in tests:
    # print(matrix)
    obj.rotate(matrix)
    print("")


def matrix_generator(n):
    matrix = []
    i = 1
    for row in range(n):
        r = []
        for col in range(n):
            r.append(i)
            i += 1
        matrix.append(r)
    return matrix

matrix = matrix_generator(12)

# for row in matrix:
#     print(f"{row},")

