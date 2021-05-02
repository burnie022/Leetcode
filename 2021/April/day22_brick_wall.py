"""
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the
same height but different width. You want to draw a vertical line from the top to the bottom and cross the least
bricks.
The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick
in this row from left to right.
If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how
to draw the line to cross the least bricks and return the number of crossed bricks.
You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously
cross no bricks.

Example:
    Input: [[1,2,2,1],
            [3,1,2],
            [1,3,2],
            [2,4],
            [3,1,2],
            [1,3,1,1]]

    Output: 2

    Explanation: View brick_wall_ex1.png

Note:
    The width sum of bricks in different rows are the same and won't exceed INT_MAX.
    The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number
        of bricks of the wall won't exceed 20,000.
"""
from typing import List
import random


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        start_positions = {}

        for row in wall:
            start_pos = 1 + row[0]
            for brick in row[1:]:
                start_positions[start_pos] = start_positions.get(start_pos, 0) + 1
                start_pos += brick

        return len(wall) - max(start_positions.values()) if start_positions else len(wall)


# Test cases

obj = Solution()

def wall_maker(height=10, length_mult_25=1, length_mult_100= 1):
    r = (([1, 2, 3, 4, 5, 3, 3, 2, 2] * length_mult_25) if length_mult_100 == 1 else
         ([1, 2, 3, 4, 5, 3, 3, 2, 2, 9, 7, 8, 6, 4, 2, 9, 7, 8, 6, 4, 9, 7, 8, 6, 4, 1] * length_mult_100))
    wall = []
    for i in range(height):
        s = r[:]
        random.shuffle(s)
        wall.append(s)

    return wall

# print(wall_maker(500, 1, 10))

tests = [
    [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]],
[[2, 2, 3, 4, 2, 3, 5, 1, 3], [5, 2, 3, 4, 1, 3, 3, 2, 2], [1, 3, 2, 4, 3, 3, 2, 2, 5], [2, 2, 4, 3, 1, 2, 5, 3, 3], [1, 3, 2, 3, 5, 2, 3, 4, 2], [2, 2, 3, 5, 3, 4, 2, 1, 3], [3, 2, 2, 5, 4, 2, 1, 3, 3], [2, 3, 2, 2, 1, 4, 3, 5, 3], [1, 5, 4, 3, 3, 2, 3, 2, 2], [3, 3, 1, 3, 2, 2, 4, 2, 5]],
[[2, 4, 2, 5, 1, 3, 3, 3, 2], [2, 3, 4, 1, 3, 2, 2, 3, 5], [2, 3, 4, 3, 2, 3, 2, 5, 1], [4, 3, 2, 3, 1, 2, 2, 3, 5], [1, 2, 4, 5, 2, 3, 3, 3, 2], [1, 3, 2, 2, 3, 2, 3, 5, 4], [2, 5, 3, 3, 3, 2, 2, 1, 4], [3, 5, 2, 3, 2, 2, 1, 4, 3], [5, 3, 2, 2, 3, 3, 1, 4, 2], [5, 3, 3, 2, 1, 2, 4, 2, 3]],
[[100000000],[100000000],[100000000]]

]

for t in tests:
    print(t)
    # print(obj.leastBricks(t))


