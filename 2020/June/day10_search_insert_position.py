"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it
would be if it were inserted in order.
You may assume no duplicates in the array.
Example 1:
    Input: [1,3,5,6], 5
    Output: 2
Example 2:
    Input: [1,3,5,6], 2
    Output: 1
Example 3:
    Input: [1,3,5,6], 7
    Output: 4
Example 4:
    Input: [1,3,5,6], 0
    Output: 0
"""
import bisect

def searchInsert(nums, target: int):
    return bisect.bisect_left(nums, target)

# For testing
tests = [([1,3,5,6], 5),
         ([1,3,5,6], 2),
         ([1,3,5,6], 7),
         ([1,3,5,6], 0)]
for n, t in tests:
    print(n, ",", t, ", index:", searchInsert(n, t))
