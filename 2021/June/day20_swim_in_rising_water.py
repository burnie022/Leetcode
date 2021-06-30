"""
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another
4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim
infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:
    Input: [[0,2],[1,3]]
    Output: 3
    Explanation:
        At time 0, you are in grid location (0, 0).
        You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

        You cannot reach point (1, 1) until time 3.
        When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:
    Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    Output: 16
    Explanation:
         0  1  2  3  4
        24 23 22 21  5
        12 13 14 15 16
        11 17 18 19 20
        10  9  8  7  6

        The final route is marked in bold.
        We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

Note:
    2 <= N <= 50.
    grid[i][j] is a permutation of [0, ..., N*N - 1].
Hint #1
    Use either Dijkstra's, or binary search for the best time T for which you can reach the end if you only step on
    squares at most T.
"""
from typing import List
import heapq


# Uses Dijkstra's algorithm
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        water = [[-1 for _ in range(len(grid))] for _ in range(len(grid))]
        water[0][0], n = grid[0][0], len(grid)
        direction = ((-1, 0), (1, 0), (0, 1), (0, -1))

        while water[-1][-1] == -1:
            t, row, col = heapq.heappop(heap)
            for a, b in direction:
                if 0 <= row + a < n and 0 <= col + b < n and water[row+a][col+b] == -1:
                    next_t = max(t, grid[row+a][col+b])
                    water[row+a][col+b] = next_t
                    heapq.heappush(heap, (next_t, row+a, col+b))

        return water[-1][-1]


if __name__ == "__main__":
    obj = Solution()
    tests = [
        [[0, 2], [1, 3]],
        [[3, 0], [1, 2]],
        [[3, 0], [2, 1]],
        [[2, 3], [0, 1]],
        [[1, 2], [3, 0]],
        [[4,5,6],[0,1,7],[2,3,8]],
        [[8, 7, 6], [0, 1, 5], [2, 3, 4]],
        [[0, 7, 6], [8, 1, 5], [2, 3, 4]],

    ]

    for t in tests:
        print(t)
        print(obj.swimInWater(t), end="\n\n")


    # For generating test cases
    # from random import shuffle
    #
    # def gen(n):
    #     l = [i for i in range(n*n)]
    #     shuffle(l)
    #     return [[l[j] for j in range(i*n, (i*n)+n)] for i in range(n)]
    #
    # for _ in range(5):
    #     print(gen(50))
    # # for row in gen(9):
    # #     print(row)
