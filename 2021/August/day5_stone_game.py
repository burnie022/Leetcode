"""
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has
a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either
the beginning or the end of the row.  This continues until there are no more piles left, at which point the person
with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

Example 1:
    Input: piles = [5,3,4,5]
    Output: true
    Explanation:
        Alex starts first, and can only take the first 5 or the last 5.
        Say he takes the first 5, so that the row becomes [3, 4, 5].
        If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
        If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
        This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

Constraints:
    2 <= piles.length <= 500
    piles.length is even.
    1 <= piles[i] <= 500
    sum(piles) is odd.
"""
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        total = sum(piles)

        def play_game(i=0, j=len(piles)-1, score=0, turn=True):
            if (i, j) in memo:
                return memo[(i,j)]
            if i == j:
                score += piles[i]
                return score > total / 2
            a = play_game(i+1, j, score+piles[i] if turn else score-piles[i], not turn)
            b = play_game(i, j-1, score+piles[j] if turn else score-piles[j], not turn)
            memo[(i, j)] = not a or not b
            return memo[(i, j)]

        a = play_game()
        # for i, j in memo.items():
        #     print(i, j)
        return not a


if __name__ == "__main__":
    obj = Solution()
    tests = [
        [5, 3, 4, 5],
        [343, 309, 416, 277, 431, 108, 341, 3, 483, 116, 189, 265, 216, 226, 110, 478, 326, 363, 132, 235],
        [305, 409, 22, 487, 229, 67, 7, 397, 138, 47, 161, 115, 177, 243, 155, 496, 85, 428, 66, 239],
        [311, 287, 256, 55, 123, 126, 50, 458, 285, 103, 384, 232, 497, 226, 10, 238, 25, 190, 60, 159],
        [182, 337, 401, 224, 479, 429, 389, 432, 492, 268, 329, 277, 79, 9, 404, 210, 84, 77, 38, 473],
        [439, 273, 160, 164, 343, 232, 348, 321, 433, 410, 408, 148, 53, 489, 230, 155, 144, 421, 215, 407],
        [135, 383, 363, 89, 73, 410, 356, 326, 275, 336, 302, 236, 288, 331, 433, 321, 83, 4, 330, 237],
        [378, 359, 350, 42, 204, 195, 360, 29, 363, 95, 53, 338, 426, 187, 20, 390, 263, 494, 330, 469],

    ]

    for t in tests:
        print(t)
        # print(obj.stoneGame(t), end="\n\n")

    # from random import randint
    # def gen_test(length):
    #     l = [randint(1, 499) for _ in range(length)]
    #     if sum(l) % 2 == 0:
    #         l[-1] += 1
    #     return l
    #
    # print(gen_test(20))

