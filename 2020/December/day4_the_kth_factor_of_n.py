"""
Given two positive integers n and k.
A factor of an integer n is defined as an integer i where n % i == 0.
Consider a list of all factors of n sorted in ascending order, return the kth factor in this list
or return -1 if n has less than k factors.

Example 1:
    Input: n = 12, k = 3
    Output: 3
    Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
Example 2:
    Input: n = 7, k = 2
    Output: 7
    Explanation: Factors list is [1, 7], the 2nd factor is 7.
Example 3:
    Input: n = 4, k = 4
    Output: -1
    Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
Example 4:
    Input: n = 1, k = 1
    Output: 1
    Explanation: Factors list is [1], the 1st factor is 1.
Example 5:
    Input: n = 1000, k = 3
    Output: 4
    Explanation: Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000].

Constraints:
    1 <= k <= n <= 1000
Hint #1
    The factors of n will be always in the range [1, n].
Hint #2
    Keep a list of all factors sorted. Loop i from 1 to n and add i if n % i == 0. Return the kth
    factor if it exist in this list.
"""

def kthFactor(n: int, k: int) -> int:
    if k == 1:
        return 1
    if k >= n:
        return -1
    upper_limit = int(n / 2) if n % 2 == 0 else int(n / 3)
    factor = 1
    for i in range(2, upper_limit + 1):
        if n % i == 0:
            factor += 1
            if factor == k:
                return i
    return n if factor + 1 == k else -1


# Test cases

tests = [
    (12, 3),
    (7, 2),
    (4, 4),
    (1, 1),
    (1000, 3),
    (999, 8)
]

for t in tests:
    print(f"n: {t[0]}, k: {t[1]}, kth factor: {kthFactor(*t)}", end="\n\n")
