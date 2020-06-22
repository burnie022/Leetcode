"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon
consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room
and must fight his way through the dungeon to rescue the princess.
The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0
or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each
step.
Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.
For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal
path RIGHT-> RIGHT -> DOWN -> DOWN.

 _____________________________
|  -2 (K) |   -3    |   3     |
|   -5    |  -10    |   1     |
|   10    |   30    |  -5 (P) |
 _____________________________

Note:
The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the
princess is imprisoned.
"""


def calculateMinimumHP(dungeon) -> int:
    if len(dungeon) == 1 and len(dungeon[0]) == 1 and dungeon[-1][-1] > 0:
        return 1

    if dungeon[-1][-1] < 1:
        dungeon[-1][-1] = -dungeon[-1][-1] + 1
    else:
        dungeon[-1][-1] = 1

    for row in reversed(range(len(dungeon))):
        for col in reversed(range(len(dungeon[0]))):
            # print(row, col)
            if row == len(dungeon) - 1:
                if col == len(dungeon[0]) - 1:
                    continue
                dungeon[row][col] = dungeon[row][col + 1] - dungeon[row][col]
            elif col == len(dungeon[0]) - 1:
                dungeon[row][col] = dungeon[row + 1][col] - dungeon[row][col]
            else:
                dungeon[row][col] = min(dungeon[row][col + 1] - dungeon[row][col],
                                        dungeon[row + 1][col] - dungeon[row][col])

            if dungeon[row][col] < 1:
                dungeon[row][col] = 1

    # for row in dungeon:
    #     print(row)

    return dungeon[0][0]

# For testing

tests = ([[-2,-3,3],[-5,-10,1],[10,30,-5]],
         [[1,-3,3],[0,-2,0],[-3,-3,-3]],
         [[2,3,3],[5,10,1],[10,30,5]],
         [[-3,-3],[6,10],[-5,-5]],
         [[8,-3,3],[-5,10,1],[10,30,-5]],
         [[-1,-3,3],[-5,10,1],[-10,-30,-5]],
         [[-1],[-5],[-1]],
         [[-1, -1, 1]],
         [[0]],
         [[1,-3,3],[0,-2,0],[-3,-3,-3]],
         [[100]],
         [[100, 20]],
            [[-200]],
        [[-3,5]],
[[-3,-55]],
[[-3,55]],
[[-3,5]],
[[-3,-55]],
[[-3,-55],[-3,55]],
         )
for t in tests:
    print(calculateMinimumHP(t))


"""
[[-2,-3,3],[-5,-10,1],[10,30,-5]]
[[2,3,3],[5,10,1],[10,30,5]]
[[-3,-3],[6,10],[-5,-5]]
[[8,-3,3],[-5,10,1],[10,30,-5]]
[[8,-3,3],[-5,10,1],[-10,-30,-5]]
[[-1, -1, 1]]
[[-1],[-5],[-1]]
[[0]]
[[1,-3,3],[0,-2,0],[-3,-3,-3]]
[[100]]
[[100, 20]]
[[-200]]
[[-3,5]]
[[-3,-55]]
[[-3,55]]
[[-3,5]]
[[-3,-55]]
[[-3,-55],[-3,55]]
[[100, 120]]

"""
