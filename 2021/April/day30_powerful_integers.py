"""
Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or
equal to bound.
An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.
You may return the answer in any order. In your answer, each value should occur at most once.

Example 1:
    Input: x = 2, y = 3, bound = 10
    Output: [2,3,4,5,7,9,10]
    Explanation:
        2 = 20 + 30
        3 = 21 + 30
        4 = 20 + 31
        5 = 21 + 31
        7 = 22 + 31
        9 = 23 + 30
        10 = 20 + 32
Example 2:
    Input: x = 3, y = 5, bound = 15
    Output: [2,4,6,8,10,14]

Constraints:
    1 <= x, y <= 100
    0 <= bound <= 106
"""
from typing import List
import math


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound < 2:
            return []
        p_nums = set()
        x_m, y_m = [], []
        if x > 1:
            for i in range(math.ceil(math.log(bound, x))):
                x_m.append(x**i)
        else:
            x_m.append(1)
        if y > 1:
            for j in range(math.ceil(math.log(bound, y))):
                y_m.append(y**j)
        else:
            y_m.append(1)
        for i in x_m:
            for j in y_m:
                n = i + j
                if n > bound:
                    break
                p_nums.add(n)
        return list(p_nums)


# Test cases
obj = Solution()
tests = [
    (2, 3, 10),
    (3, 5, 15),
    (12, 15, 10000),
    (2, 1, 10),
]

for x, y, b in tests:
    print(f"{x}\n{y}\n{b}")
    print(obj.powerfulIntegers(x, y, b), end="\n\n")

