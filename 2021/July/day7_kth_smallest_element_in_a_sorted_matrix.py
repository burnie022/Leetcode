"""
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest
element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example 1:
    Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    Output: 13
    Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:
    Input: matrix = [[-5]], k = 1
    Output: -5

Constraints:
    - n == matrix.length
    - n == matrix[i].length
    - 1 <= n <= 300
    - -10^9 <= matrix[i][j] <= 10^9
    - All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
    - 1 <= k <= n^2
"""
from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        matrix = [row[::-1] for row in matrix]
        heap = [(row.pop(), i) for i, row in enumerate(matrix)]
        heapq.heapify(heap)

        for _ in range(k-1):
            row = heapq.heappop(heap)[1]
            if matrix[row]:
                heapq.heappush(heap, (matrix[row].pop(), row))

        return heapq.heappop(heap)[0]


# The solution below also works well but apparently ran slightly slower on leetcode. I expected it to run faster since
# this solution does not reverse the rows of the matrix and doesn't pop from the rows but it didn't.

        # cols = [1 for _ in range(len(matrix))]
        # heap = [(matrix[row][0], row) for row in range(len(matrix))]
        # heapq.heapify(heap)
        #
        # for _ in range(k-1):
        #     row = heapq.heappop(heap)[1]
        #     if cols[row] != len(matrix):
        #         heapq.heappush(heap, (matrix[row][cols[row]], row))
        #         cols[row] += 1
        #
        # return heapq.heappop(heap)[0]


# Solution below works well using Timsort (python's built in sorted algorithm). Faster than the above solutions.
# According to a user on leetcode:"The difference is that Timsort implemented in Python is capable of taking advantage
#     of existing partial orderings. Moving sorted data in bulk is always faster than comparing and moving individual
#     data elements, due to modern hardware architecture. Time complexity is the same because merging n sorted arrays
#     of size n is still O(n^2 * log n) in the worst case."

    def kthSmallestSorted(self, matrix: List[List[int]], k: int) -> int:
        return list(sorted(n for row in matrix for n in row))[k-1]


if __name__ == "__main__":
    obj = Solution()
    tests = [
        ([[1,5,9],[10,11,13],[12,13,15]], 8),
        ([[1,5,9],[10,11,13],[12,13,15]], 1),
        ([[1,5,9],[10,11,13],[12,13,15]], 2),
        ([[1,5,9],[10,11,13],[12,13,15]], 3),
        ([[1,5,9],[10,11,13],[12,13,15]], 4),
        ([[1,5,9],[10,11,13],[12,13,15]], 5),
        ([[1,5,9],[10,11,13],[12,13,15]], 6),
        ([[1,5,9],[10,11,13],[12,13,15]], 7),
        ([[1,5,9],[10,11,13],[12,13,15]], 9),
        ([[-5]], 1)
    ]

    for t in tests:
        print(t[0])
        print(t[1])
        print(obj.kthSmallest(*t), end="\n\n")
        # print(obj.kthSmallestSorted(*t), end="\n\n")
