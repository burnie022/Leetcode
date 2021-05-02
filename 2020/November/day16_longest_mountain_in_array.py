"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties
hold:

    B.length >= 3
    There exists some 0 < i < B.length - 1 such that:
        B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.
Return 0 if there is no mountain.

Example 1:
    Input: [2,1,4,7,3,2,5]
    Output: 5
    Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:
    Input: [2,2,2]
    Output: 0
    Explanation: There is no mountain.

Note:
    0 <= A.length <= 10000
    0 <= A[i] <= 10000

Follow up:
    Can you solve it using only one pass?
    Can you solve it in O(1) space?
"""

def longestMountain(A) -> int:
    if len(A) < 3:
        return 0
    max_len = 0
    climb, desc = 0, 0

    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            if desc:
                max_len = max(max_len, climb + desc + 1)
                climb, desc = 0, 0
            climb += 1
        elif A[i] < A[i - 1]:
            if climb:
                desc += 1
        else:
            if desc:
                max_len = max(max_len, climb + desc + 1)
            climb, desc = 0, 0

    if desc:
        max_len = max(max_len, climb + desc + 1)

    return max_len



# Test cases

tests = [
    [2,1,4,7,3,2,5],
    [2,2,2],
    [2,1,4, 4,7,3,2,5],
    [],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7,6],
    [2,1,2,3,4,5,6,7,6,9],
    [7,6,5,4,3,2,1,2],
    [6,7,6,5,4,3,2,1,2],
    [4,5,3,2,6,5,8,9,2,5,7,5,2,1,3,5,7,8,6,5,3,5,5,7,8,5,3,1,0]
]

for t in tests:
    print(t)
    print(longestMountain(t), end="\n\n")
