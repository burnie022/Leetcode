"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the
first bad version. You should minimize the number of calls to the API.

Example 1:
    Input: n = 5, bad = 4
    Output: 4
    Explanation:
        call isBadVersion(3) -> false
        call isBadVersion(5) -> true
        call isBadVersion(4) -> true
        Then 4 is the first bad version.

Example 2:
    Input: n = 1, bad = 1
    Output: 1

Constraints:
    1 <= bad <= n <= 2^31 - 1
"""
from typing import List


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(n):
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1
        lo, hi = 1, n - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            curr_is_bad, next_is_bad = isBadVersion(mid), isBadVersion(mid + 1)
            if not curr_is_bad and next_is_bad:
                return mid + 1
            elif curr_is_bad:
                hi = mid
            else:
                lo = mid + 1

# The above solution works, but here's a better more efficient solution I'd previously written:
#     def firstBadVersion(self, n):
#         hi = n
#         lo = 1
#         while lo < hi:
#             mid = lo + (hi - lo) // 2
#             if isBadVersion(mid):
#                 hi = mid
#             else:
#                 lo = mid + 1
#
#         return lo


if __name__ == "__main__":
    obj = Solution()
    tests = [

    ]

    for t in tests:
        print(t)
        print(obj(t), end="\n\n")
