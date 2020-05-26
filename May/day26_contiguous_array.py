"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""

def findMaxLength(nums) -> int:
    max_len, tot = 0, 0
    dict_nums = {0: 0}

    for i in range(len(nums)):
        tot = tot + 1 if nums[i] == 1 else tot - 1
        #print(tot)
        if dict_nums.get(tot) is not None:
            max_len = max(max_len, 1 + i - dict_nums[tot])
        else:
            dict_nums[tot] = i + 1
        #print(dict_nums)

    return max_len

n = [0,1]
tests = [[0,1], [0,1,0], [1,1,1,1,0,1,0,1,0], [1,1,1,1,0,1,0,1,0,0],
         [1], [], [1,1,1,1,0,1,0,1,0,0,1,0,0,1,0], [1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,0]]
for t in tests:
    print(findMaxLength(t))
