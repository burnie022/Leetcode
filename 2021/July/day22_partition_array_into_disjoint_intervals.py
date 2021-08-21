"""
Given an array nums, partition it into two (contiguous) subarrays left and right so that:
    - Every element in left is less than or equal to every element in right.
    - left and right are non-empty.
    - left has the smallest possible size.

Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

Example 1:
    Input: nums = [5,0,3,8,6]
    Output: 3
    Explanation: left = [5,0,3], right = [8,6]

Example 2:
    Input: nums = [1,1,1,0,6,12]
    Output: 4
    Explanation: left = [1,1,1,0], right = [6,12]

Note:
    2 <= nums.length <= 30000
    0 <= nums[i] <= 10^6
    It is guaranteed there is at least one way to partition nums as described.
"""
from typing import List
from collections import Counter
import heapq


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        r_min = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            r_min.append(min(r_min[-1], nums[i]))
        r_min = r_min[::-1]

        left_max = nums[0]
        for i in range(len(nums) - 1):
            left_max = max(left_max, nums[i])
            if left_max <= r_min[i+1]:
                return i + 1


# Works using heapq and Counter but is slower and unnecessarily more complex than the above solution
    def partitionDisjointHeap(self, nums: List[int]) -> int:
        counter = Counter(nums)
        left_max = nums[0]
        heap = nums[:]
        heapq.heapify(heap)

        for i in range(len(nums) - 2):
            left_max = max(left_max, nums[i])
            counter[nums[i]] -= 1
            while not counter[heap[0]]:
                heapq.heappop(heap)
            if left_max <= heap[0]:
                return i + 1

        return len(nums) - 1


if __name__ == "__main__":
    obj = Solution()
    tests = [
        [5, 0, 3, 8, 6],
        [1, 1, 1, 0, 6, 12],
        [8, 9, 18, 6, 2, 8, 12, 10, 15, 18, 4, 16, 11, 19, 20],
        [3, 9, 6, 14, 20, 4, 4, 7, 3, 20, 12, 17, 15, 5, 19],
        [3,3,3, 2, 1, 3, 7,8,9, 3],
        [3, 1, 3, 1, 4, 4, 5, 7, 8, 7, 10, 10, 3, 9, 3],
        [2,2],
        [2,1,2],
        [1,2,3],

    ]

    for t in tests:
        print(t)
        print(obj.partitionDisjoint(t), end="\n\n")

