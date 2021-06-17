""" n-queens_2_ex1.jpg
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each
other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
    Input: n = 4
    Output: 2
    Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:
    Input: n = 1
    Output: 1

Constraints:
    1 <= n <= 9
"""
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        self.possible_boards = 0
        self.n = n
        new_board = [[0 for _ in range(n)] for _ in range(n)]

        self.check_rows(new_board)

        return self.possible_boards

    def check_rows(self, board):
        if all(board[0]):
            return
        if len(board) == 1:
            self.possible_boards += 1
            return

        for col in range(self.n):
            if board[0][col] == 0:
                lower_rows = [row[:] for row in board[1:]]
                lower_rows = self.fill_diagonals_and_down(lower_rows, col)
                self.check_rows(lower_rows)

    def fill_diagonals_and_down(self, board, col):
        l, r = col - 1, col + 1
        for row in range(len(board)):
            board[row][col] = 1
            if l >= 0:
                board[row][l] = 1
                l -= 1
            if r < self.n:
                board[row][r] = 1
                r += 1

        return board



        # c = col - 1
        # for r in range(len(board)):
        #     if c < 0:
        #         break
        #     board[r][c] = 1
        #     c -= 1
        #
        # c = col + 1
        # for r in range(len(board)):
        #     if c == self.n:
        #         break
        #     board[r][c] = 1
        #     c += 1
        #
        # for r in range(len(board)):
        #     board[r][col] = 1
        #
        # return board




    # def check_rows(self, row, board):
    #     if all(board[row]):
    #         return
    #     if row == len(board) - 1:
    #         self.possible_boards += 1
    #         return
    #
    #     for col in range(self.n):
    #         if board[row][col] == 0:
    #             lower_rows = board[row+1:]
    #             # possible_board = board.copy()
    #             new_board = []
    #             # board_copy = [row for row in board]
    #             new_board.extend(board)
    #             # self.check_col(board_copy, row, col)
    #             new_board = self.fill_diagonals_and_down(new_board, row, col)
    #             self.check_rows(row + 1, new_board)
    #
    #             # possible_board = self.fill_diagonals_and_down(possible_board,row,col)
    #             # for r in possible_board:
    #             #     print(r)
    #             # print("")
    #             # self.check_rows(row+1, possible_board)
    #
    # def check_col(self, board, row, col):
    #     board = self.fill_diagonals_and_down(board, row, col)
    #     for r in board:
    #         print(r)
    #     print("")
    #     self.check_rows(row + 1, board)
    #
    #
    # def fill_diagonals_and_down(self, board, row, col):
    #     board = board[:]
    #     board[row][col] = 2
    #     c = col - 1
    #     for r in range(row+1, len(board)):
    #         if c < 0:
    #             break
    #         board[r][c] = 1
    #         c -= 1
    #
    #     c = col + 1
    #     for r in range(row+1, len(board)):
    #         if c == self.n:
    #             break
    #         board[r][c] = 1
    #         c += 1
    #
    #     for r in range(row+1, len(board)):
    #         board[r][col] = 1
    #
    #     return board


# Test cases
obj = Solution()
tests = [
    1,2,3,4,5,6,7,8,9
]

for t in tests:
    print(t)
    print(obj.totalNQueens(t), end="\n\n")

# print(all([1,2,1,1,-1,-10]))
