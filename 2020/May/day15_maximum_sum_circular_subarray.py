"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of
C.
Here, a circular array means the end of the array connects to the beginning of the array.
(Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a
subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

Example 1:
    Input: [1,-2,3,-2]
    Output: 3
    Explanation: Subarray [3] has maximum sum 3
Example 2:
    Input: [5,-3,5]
    Output: 10
    Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:
    Input: [3,-1,2,-1]
    Output: 4
    Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:
    Input: [3,-2,2,-3]
    Output: 3
    Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:
    Input: [-2,-3,-1]
    Output: -1
    Explanation: Subarray [-1] has maximum sum -1
Note:
    -30000 <= A[i] <= 30000
    1 <= A.length <= 30000
"""

def maxSubarraySumCircular(A) -> int:
    if len(A) == 1:
        return A[0]
    if all(n < 0 for n in A):
        return max(A)

    min_sum, max_sum = A[0], A[0]
    rmin, rmax = A[0], A[0]
    for i in range(1, len(A)):
        rmin = min(rmin + A[i], A[i])
        rmax = max(rmax + A[i], A[i])

        min_sum = min(min_sum, rmin)
        max_sum = max(max_sum, rmax)

    return max(sum(A) - min_sum, max_sum)


# For testing
lists = [[2], [1, -9, -1, 3, 2], [1,2,3,4],
         [1,-2,3,-2],
         [5,-3,5],
         [-9, 2, 2, 3, -1],
         [1, -9, -1, 3, 2],
         [-1, -9, -1, 3, 2],
         [3,-1,2,-1],
         [3,-2,2,-3],
         [-2,-3,-1],
         [-2,-3,0],
         [-2,-3,1]]

for li in lists:
    print(li, ":", maxSubarraySumCircular(li))

