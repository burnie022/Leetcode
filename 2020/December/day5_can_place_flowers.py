"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

def canPlaceFlowers(flowerbed, n: int) -> bool:
    if n == 0:
        return True
    flowerbed = [0] + flowerbed + [0]
    flowers = count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            count += 1
            if count == 3:
                count = 1
                flowers += 1
                if flowers == n:
                    return True
        else:
            count = 0
    return False


# Test cases

tests = [
    ([1,0,0,0,1], 1),
    ([1,0,0,0,1], 2),
    ([0,0,0,0,0], 3),
    ([0,0,1,0,0], 2),
    ([0,1,0,0,0], 2),
    ([0,1,0,0,0], 1),
    ([0,1,1,1], 0)
]

for t in tests:
    print(canPlaceFlowers(*t))
