"""You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest
version of your product fails the quality check. Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the
following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function
to find the first bad version. You should minimize the number of calls to the API.

Example:
    Given n = 5, and version = 4 is the first bad version.

    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true

    Then 4 is the first bad version. """

# My approach uses a simple binary search. I've created my own implementation of the  firstBadVersion API
# lo gets incremented up one until lo == hi, this is where the isBadVersion first returns True
def firstBadVersion(n):
    def isBadVersion(v):
        bad_version = 10
        if v >= bad_version:
            return True
        return False

    hi = n
    lo = 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if isBadVersion(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo


print(firstBadVersion(8))