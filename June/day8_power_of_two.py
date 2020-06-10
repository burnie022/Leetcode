"""
Given an integer, write a function to determine if it is a power of two.
Example 1:
    Input: 1
    Output: true
    Explanation: 20 = 1
Example 2:
    Input: 16
    Output: true
    Explanation: 24 = 16
Example 3:
    Input: 218
    Output: false
"""
# import bisect

# def isPowerOfTwo(n: int):
#     mult = [2**i for i in range(0, int(n**(1/2)) + 1)]
#     a = bisect.bisect_left(mult, n)
#     return 2**a == n


# This function that checks bits is much faster than the above function
def isPowerOfTwoBitwise(n: int):
    b = bin(n)[2:]
    return b[0] == "1" and not "1" in b[1:]


# For testing

t = [i for i in range(0, 65)]
for n in t:
    b = isPowerOfTwoBitwise(n)
    print(n, ",", b)

print(131072, ",", isPowerOfTwoBitwise(131072))
"""
tests = [i for i in range(0, 65)]

print([2**i for i in range(0, 128)])
for i in tests:
    a = isPowerOfTwo(i)
    print("2^"+ str(a), "=", i, ",", 2**a == i)
    # print(i,",",a)
"""
#131072