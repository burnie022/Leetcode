"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped
to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""


# This first solution belongs to someone from leetcode. My DFS solution below works but hits a max recursion error
# before being accepted by Leetcode
""" This person wrote:
In this problem we need to understand, what exactly surrouned by 'X' means. It actually means that if we start from
'O' at the border, and we traverse only 'O', only those 'O' are not surrouned by 'X'. So the plan is the following:

Start dfs or bfs from all 'O', which are on the border.
When we traverse them, let us color them as 'T', temporary color.
Now, when we traverse all we wanted, all colors which are not 'T' need to renamed to 'X' and all colors which are 'T'
need to be renamed to 'O', and that is all!
Compexity: time complextiy is O(mn), where m and n are sizes of our board. Additional space complexity can also go
upto O(mn) to keep stack of recursion.
"""
from itertools import product

def solve2(board):
    if len(board) < 3 or len(board[0]) < 3:
        return
    rows, cols = len(board), len(board[0])

    def dfs(row, col):
        if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != "O":
            return
        board[row][col] = 'T'

        dir = [[row + 1, col], [row - 1, col], [row, col - 1], [row, col + 1]]
        for x, y in dir:
            dfs(x, y)

    for row in range(0, rows):
        dfs(row, 0)
        dfs(row, cols - 1)

    for col in range(0, cols):
        dfs(0, col)
        dfs(rows - 1, col)

    for row, col in product(range(rows), range(cols)):
        board[row][col] = "X" if board[row][col] != "T" else "O"

    return board


# DFS solution that I came up with. Uses more memory and gets a gets max recursion error when working with huge board
# lengths on leetcode. Works fine on my machine.
def solve(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if len(board) < 3 or len(board[0]) < 3:
        print("No changes")
        return

    checked = set()
    current_set = set()

    def dfs(row, col):
        if board[row][col] == "X" or (row, col) in current_set:
            return True

        current_set.add((row, col))
        if row in [0, len(board) - 1] or col in [0, len(board[0]) - 1]:
            return False

        dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        return all(dfs(row + a, col + b) for a,b in dir)


    for row in range(1, len(board) - 1):
        for col in range(1, len(board[0]) - 1):
            if board[row][col] == "O" and (row, col) not in checked:
                if dfs(row, col):
                    for r,c in current_set:
                        board[r][c] = "X"
                    current_set.clear()
                else:
                    checked.update(current_set)
                    current_set.clear()



# For testing
    return board

tests = ([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
         [["X","X","X","X"],["X","O","O","X"]],
         [["X","X","X"],["X","O","X"],["X","X","X"]],
         [["X","X"],["X","O"],["X","X"]],
         [["X","X","X","X","X","X","X"],["X","O","O","X","O","O","X"],["X","X","O","X","X","O","X"],
          ["X","O","O","O","O","O","X"],["X","O","O","X","X","O","X"],["X","O","O","O","X","O","X"],
          ["X","X","X","X","O","X","X"]],
         [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]],
         [["O","X","X","X","X"],["X","O","O","O","X"],["X","O","O","O","X"],["X","O","O","O","X"],["X","X","O","X","O"]],
         [["O","X","X","X","X"],["X","O","O","O","X"],["X","O","O","O","X"],["X","O","O","O","X"],["X","O","X","X","O"]],
         [["O","X","X","X","X"],["X","O","O","O","X"],["X","O","O","O","O"],["X","O","O","O","X"],["X","X","X","X","O"]],
         [["O", "X", "X", "X", "X", "X", "O", "O"], ["O", "O", "O", "X", "X", "X", "X", "O"],
          ["X", "X", "X", "X", "O", "O", "O", "O"],
          ["X", "O", "X", "O", "O", "X", "X", "X"], ["O", "X", "O", "X", "X", "X", "O", "O"],
          ["O", "X", "X", "O", "O", "X", "X", "O"],
          ["O", "X", "O", "X", "X", "X", "O", "O"], ["O", "X", "X", "X", "X", "O", "X", "X"]]
         )

for b in tests:
    print(solve2(b))

# print(solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],
#   ["X","X","O","X","O"]]))

"""
[["O","X","X","X","X","X","O","O"],["O","O","O","X","X","X","X","O"],["X","X","X","X","O","O","O","O"],
["X","O","X","O","O","X","X","X"],["O","X","O","X","X","X","O","O"],["O","X","X","O","O","X","X","O"],
["O","X","O","X","X","X","O","O"],["O","X","X","X","X","O","X","X"]]

output:
[["O","X","X","X","X","X","O","O"],["O","O","O","X","X","X","X","O"],["X","X","X","X","O","O","O","O"],
["X","X","X","X","O","X","X","X"],["O","X","X","X","X","X","O","O"],["O","X","X","X","X","X","X","O"],
["O","X","X","X","X","X","O","O"],["O","X","X","X","X","O","X","X"]]

expected:
[["O","X","X","X","X","X","O","O"],["O","O","O","X","X","X","X","O"],["X","X","X","X","O","O","O","O"],
["X","X","X","O","O","X","X","X"],["O","X","X","X","X","X","O","O"],["O","X","X","X","X","X","X","O"],
["O","X","X","X","X","X","O","O"],["O","X","X","X","X","O","X","X"]]

"""