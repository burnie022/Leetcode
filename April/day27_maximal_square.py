mat = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","1"]]
    #[["1","0","1","0","0"],["0","0","0","1","1"],["0","0","0","1","1"],["0","0","0","0","1"]]
    #[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]


def maximalSquare(matrix):
    max_square = 0
    if any("1" in sub_mat for sub_mat in matrix):
        max_square = 1
    else:
        return 0

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if int(matrix[i][j]):
                area = 1 + min(int(matrix[i - 1][j]), int(matrix[i][j - 1]), int(matrix[i - 1][j - 1]))
                matrix[i][j] = area
                if area > max_square:
                    max_square = area

    print(matrix)
    return max_square * max_square


print(maximalSquare(mat))
