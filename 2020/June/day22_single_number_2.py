"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once.
Find that single one.
Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
    Input: [2,2,3,2]
    Output: 3
Example 2:
    Input: [0,1,0,1,0,1,99]
    Output: 99
"""
import collections

def singleNumber(nums) -> int:
    count = collections.Counter(nums)
    for num, c in count.items():
        if c == 1:
            return num

# For testing
tests = (
[2,2,3,2],
[0,1,0,1,0,1,99],
    [8,3,3,3]
)
for t in tests:
    print(singleNumber(t))
