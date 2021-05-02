"""
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.
You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
While moving from building i to building i+1 (0-indexed),
    If the current building's height is greater than or equal to the next building's height, you do not need a ladder
        or bricks.
    If the current building's height is less than the next building's height, you can either use one ladder or
        (h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

Example 1:
    VIEw EXAMPLE PIC: furthest_building_you_can_reach_ex1.gif
    Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
    Output: 4
    Explanation: Starting at building 0, you can follow these steps:
        - Go to building 1 without using ladders nor bricks since 4 >= 2.
        - Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
        - Go to building 3 without using ladders nor bricks since 7 >= 6.
        - Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
    It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

Example 2:
    Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
    Output: 7
Example 3:
    Input: heights = [14,3,19,3], bricks = 17, ladders = 0

Output: 3

Constraints:
    1 <= heights.length <= 105
    1 <= heights[i] <= 106
    0 <= bricks <= 109
    0 <= ladders <= heights.length
Hint #1
    Assume the problem is to check whether you can reach the last building or not.
Hint #2
    You'll have to do a set of jumps, and choose for each one whether to do it using a rope or bricks. It's always
        optimal to use ropes in the largest jumps.
Hint #3
    Iterate on the buildings, maintaining the largest r jumps and the sum of the remaining ones so far, and stop
        whenever this sum exceeds b.
"""
from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        index = 0

        while index < len(heights) - 1:
            diff = heights[index+1] - heights[index]
            if diff <= 0:
                index += 1
                continue

            if len(heap) < ladders:
                heapq.heappush(heap, diff)
            elif ladders and diff > heap[0]:
                bricks -= heapq.heappushpop(heap, diff)
            else:
                bricks -= diff

            if bricks < 0:
                break

            index += 1

        return index


# For testing
obj = Solution()

tests = [
    ([4,2,7,6,9,14,12], 5, 1),
    ([4,12,2,7,3,18,20,3,19], 10, 2),
    ([14,3,19,3], 17, 0),
    ([15, 15, 10, 16, 30, 8, 11, 12, 22, 16, 19, 27, 28, 12, 20, 18, 13, 7, 23, 16, 12, 15, 26, 26, 7, 30, 20, 3, 12, 18, 28, 17, 19, 3, 6, 14, 17, 2, 9, 28, 10, 24, 20, 3, 2, 12, 22, 20, 27, 20, 8, 18, 24, 15, 5, 1, 26, 29, 5, 27, 27, 17, 8, 22, 26, 20, 16, 6, 9, 4, 9, 18, 3, 16, 1, 15, 16, 12, 17, 19, 14, 21, 20, 19, 9, 17, 13, 5, 15, 11, 18, 5, 19, 2, 25, 8, 16, 3, 11, 2], 25, 8),
    ([13, 22, 29, 2, 30, 28, 20, 4, 9, 29, 5, 12, 10, 11, 29, 17, 3, 8, 6, 8, 21, 19, 14, 29, 30, 15, 9, 19, 16, 30, 18, 10, 12, 14, 29, 25, 9, 6, 16, 15, 23, 28, 20, 18, 25, 3, 24, 21, 12, 6, 21, 8, 9, 8, 9, 25, 4, 30, 25, 4, 15, 7, 15, 10, 25, 16, 7, 15, 7, 19, 7, 2, 26, 1, 1, 28, 25, 19, 25, 26, 16, 6, 18, 20, 2, 23, 15, 16, 11, 2, 3, 28, 1, 16, 25, 8, 24, 14, 20, 13], 20, 7),
    ([2, 6, 12, 17, 7, 22, 17, 6, 20, 13, 13, 2, 12, 30, 26, 8, 27, 12, 17, 9, 15, 12, 21, 8, 23, 9, 11, 19, 29, 27, 15, 27, 23, 21, 7, 20, 25, 2, 9, 7, 18, 5, 21, 24, 17, 28, 14, 14, 21, 27, 24, 10, 27, 4, 26, 14, 3, 21, 19, 2, 22, 22, 9, 9, 15, 15, 29, 18, 23, 28, 14, 4, 29, 25, 26, 7, 14, 29, 30, 1, 13, 3, 3, 19, 19, 4, 12, 15, 3, 1, 3, 16, 29, 15, 16, 3, 19, 16, 23, 12], 18,7),
    (
    [15, 15, 10, 16, 30, 8, 11, 12, 22, 16, 19, 27, 28, 12, 20, 18, 13, 7, 23, 16, 12, 15, 26, 26, 7, 30, 20, 3, 12, 18,
     28, 17, 19, 3, 6, 14, 17, 2, 9, 28, 10, 24, 20, 3, 2, 12, 22, 20, 27, 20, 8, 18, 24, 15, 5, 1, 26, 29, 5, 27, 27,
     17, 8, 22, 26, 20, 16, 6, 9, 4, 9, 18, 3, 16, 1, 15, 16, 12, 17, 19, 14, 21, 20, 19, 9, 17, 13, 5, 15, 11, 18, 5,
     19, 2, 25, 8, 16, 3, 11, 2], 35, 11),
    ([13, 22, 29, 2, 30, 28, 20, 4, 9, 29, 5, 12, 10, 11, 29, 17, 3, 8, 6, 8, 21, 19, 14, 29, 30, 15, 9, 19, 16, 30, 18,
      10, 12, 14, 29, 25, 9, 6, 16, 15, 23, 28, 20, 18, 25, 3, 24, 21, 12, 6, 21, 8, 9, 8, 9, 25, 4, 30, 25, 4, 15, 7,
      15, 10, 25, 16, 7, 15, 7, 19, 7, 2, 26, 1, 1, 28, 25, 19, 25, 26, 16, 6, 18, 20, 2, 23, 15, 16, 11, 2, 3, 28, 1,
      16, 25, 8, 24, 14, 20, 13], 28, 10),
    ([2, 6, 12, 17, 7, 22, 17, 6, 20, 13, 13, 2, 12, 30, 26, 8, 27, 12, 17, 9, 15, 12, 21, 8, 23, 9, 11, 19, 29, 27, 15,
      27, 23, 21, 7, 20, 25, 2, 9, 7, 18, 5, 21, 24, 17, 28, 14, 14, 21, 27, 24, 10, 27, 4, 26, 14, 3, 21, 19, 2, 22,
      22, 9, 9, 15, 15, 29, 18, 23, 28, 14, 4, 29, 25, 26, 7, 14, 29, 30, 1, 13, 3, 3, 19, 19, 4, 12, 15, 3, 1, 3, 16,
      29, 15, 16, 3, 19, 16, 23, 12], 28, 7),

]

for h, b, l in tests:
    # print(h)
    # print(b)
    # print(l)
    print(obj.furthestBuilding(h, b, l))


# import random
#
# def generate_heights(length, tallest):
#     buildings = []
#     for _ in range(length):
#         buildings.append(random.randint(1, tallest))
#     return buildings
#
# for i in range(1):
#     print(generate_heights(50000, 5000))
