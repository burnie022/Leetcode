"""
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you
get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to
a[l],a[l+1],...,a[r] for some (l,r).

Example 1:
    Input: nums = [4,2,4,5,6]
    Output: 17
    Explanation: The optimal subarray here is [2,4,5,6].
Example 2:
    Input: nums = [5,2,1,2,5,2,1,2,5]
    Output: 8
    Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

Constraints:
    1 <= nums.length <= 105
    1 <= nums[i] <= 104
Hint #1
    The main point here is for the subarray to contain unique elements for each index. Only the first subarrays
    starting from that index have unique elements.
Hint #2
    This can be solved using the two pointers technique
"""
from typing import List
from collections import deque

# This solution beat 100% of runtime for python3 solutions submitted to leetcode
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum = curr_sum = 0
        queue, set_nums = deque(), set()

        for num in nums:
            if num not in set_nums:
                queue.append(num)
                set_nums.add(num)
                curr_sum += num
                max_sum = max(max_sum, curr_sum)
            else:
                while queue[0] != num:
                    curr_sum -= queue[0]
                    set_nums.remove(queue.popleft())
                queue.rotate(-1)

        return max_sum


# Test cases
obj = Solution()
tests = [
[4,2,4,5,6],
[5,2,1,2,5,2,1,2,5],
[3,5,2,1,2,8,5,2,1,2,5],
[3,5,2,1,2,5,8,2,1,2,5],
[3,5,2,1,2,5,2,1,2,5],
[5,2,1,2,5,2,1,2,5,6],
    [1],
    [1,2,3],
    [1,2,3,4,3,2,1,2],
    [1, 2, 3, 4, 3, 2, 1, 2,3,4,5],

]

for t in tests:
    print(t)
    # print(obj.maximumUniqueSubarray(t), end="\n\n")
