"""
There is a special square room with mirrors on each of the four walls.  Except for the
southwest corner, there are receptors on each of the remaining corners, numbered 0, 1,
and 2.

The square room has walls of length p, and a laser ray from the southwest corner first
meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the
ray will meet a receptor eventually.)



Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left
wall.

Note:
    1 <= p <= 1000
    0 <= q <= p
"""
from fractions import Fraction
import fractions
def mirrorReflection(p: int, q: int) -> int:
    if not q:
        return 0
    frac = fractions.Fraction(q, p)
    q, p = frac.numerator, frac.denominator
    if p % q == 0:
        multiple = p / q
        if multiple % 2 != 0:
            return 0 if (multiple * q/p) % 2 == 0 else 1
        return 2
    if p % 2 != 0:
        return 0 if (q*p) % 2 == 0 else 1
    return 2


# Test cases
tests = [
    (2,1),
    (4,3),
    (6,2),
    (6,0),
    (5,5),
    (3,2),
    (8,1),
    (4,1),
    (6,1),
    (6,5),
    (12, 6),
    (18, 12),
    (4,3),
    (8,7),
    (9,8),
    (18,12),
    (3,2),
    (900, 87)
]

for t in tests:
    print(t)
    print(mirrorReflection(*t), end="\n\n")
