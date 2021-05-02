"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when
viewed from a distance. Now suppose you are given the locations and height of all the buildings as
shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings
collectively (Figure B).

!!!! VIEW SAVED PICTURES skyline1.jpg AND skyline2.jpg IN NOVEMBER FOLDER FOR EXAMPLE 1 !!!!!

Buildings Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi],
where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively,
and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as:
[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of
[ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint
of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely
used to mark the termination of the skyline, and always has zero height. Also, the ground in between any
two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:
[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
"""
from collections import deque

class Max_MonoQueue:
    def __init__(self):
        self.deq = deque([])

    def insert(self, index, height):
        if not self.deq:
            self.deq.append((index, height))
        else:
            for i, d in enumerate(self.deq):
                if d[1] <= height:
                    self.deq.insert(i, (index, height))
                    break
            else:
                self.deq.append((index,height))

    def remove(self, index, height):
        self.deq.remove((index, height))

    def get_tallest_building_height(self):
        if self.deq:
            return self.deq[0][1]
        return 0


class Solution:
    def getSkyline(self, buildings):
        skyline = []
        x_vals = {}
        height_dict = {}
        queue = Max_MonoQueue()
        building_set = set()
        for i in range(len(buildings)):
            s, e, h = buildings[i]
            x_vals[s] = x_vals.get(s, []) + [i]
            x_vals[e] = x_vals.get(e, []) + [i]
            height_dict[i] = h

        for x in sorted(x_vals.keys()):
            for building in x_vals[x]:
                if building not in building_set:
                    queue.insert(building, height_dict[building])
                    building_set.add(building)
                else:
                    queue.remove(building, height_dict[building])
                    building_set.remove(building)
            tallest = queue.get_tallest_building_height()
            if not skyline:
                skyline.append((x, tallest))
            else:
                if tallest == skyline[-1][1]:
                    continue
                skyline.append((x, tallest))

        return skyline


# Test cases
s = Solution()
tests = [
[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
    [[1, 4, 5], [3, 5, 4], [4, 8, 7], [7, 10, 7], [11, 13, 4], [13, 14, 4]],
[[1, 4, 5], [2, 5, 4], [7, 8, 8], [7, 10, 7], [11, 13, 4], [13, 18, 4], [15, 17, 6]]

]

for t in tests:
    print(s.getSkyline(t))
