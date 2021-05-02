"""
Given the coordinates of four points in 2D space, return whether the four points could
construct a square.
The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
    Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
    Output: True

Note:
All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""

def validSquare(p1, p2, p3, p4) -> bool:
    if len({tuple(p1), tuple(p2), tuple(p3), tuple(p4)}) < 4:
        # print(len({tuple(p1), tuple(p2), tuple(p3), tuple(p4)}))
        return False

    distances = set()
    def get_dist(a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** (1 / 2)

    for a, b in ((p1, p4), (p1, p2), (p1, p3), (p2, p3), (p3, p4), (p4, p2)):
        distances.add(get_dist(a, b))

    return len(distances) == 2




# Test cases

points = [
    ([0, 0], [1, 1], [1, 0], [0, 1]),
    ([0, 0], [1, 1], [1, 0], [1, 1]),
    ([0, 0], [1, 1], [2, 2], [3, 3]),
    ([0, 0], [1, 1], [1, -1], [0, 2]),
    ([0, 0], [3, 3], [3, 0], [0, 3]),
    ([0, 0], [0, 0], [1, 1], [0, 0])
]

for pt in points:
    a, b, c, d = pt
    print(f"{a}, {b}, {c}, {d}")
    print(validSquare(a, b, c, d))
    print("")



