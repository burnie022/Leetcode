"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.
Example 1:
    Input: 16
    Output: true
Example 2:
    Input: 14
    Output: false
"""

def isPerfectSquare(num: int) -> bool:
    lo = 0
    hi = num

    if num == 1:
        return True

    while lo < hi:
        mid = lo + ((hi - lo) // 2)
        if mid * mid > num:
            hi = mid
        else:
            if mid * mid == num:
                return True
            lo = mid + 1

    return False

# For testing
while True:
    x = input()
    print(isPerfectSquare(int(x)))