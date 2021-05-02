"""
Given an array of non-negative integers arr, you are initially positioned at
start index of the array. When you are at index i, you can jump to i + arr[i]
or i - arr[i], check if you can reach to any index with value 0.
Notice that you can not jump outside of the array at any time.

Example 1:
    Input: arr = [4,2,3,0,3,1,2], start = 5
    Output: true
    Explanation:
    All possible ways to reach at index 3 with value 0 are:
    index 5 -> index 4 -> index 1 -> index 3
    index 5 -> index 6 -> index 4 -> index 1 -> index 3
Example 2:
    Input: arr = [4,2,3,0,3,1,2], start = 0
    Output: true
    Explanation:
    One possible way to reach at index 3 with value 0 is:
    index 0 -> index 4 -> index 1 -> index 3
Example 3:
    Input: arr = [3,0,2,1,2], start = 2
    Output: false
    Explanation: There is no way to reach at index 1 with value 0.

Constraints:
    1 <= arr.length <= 5 * 10^4
    0 <= arr[i] < arr.length
    0 <= start < arr.length
Hint #1
Think of BFS to solve the problem.
Hint #2
When you reach a position with a value = 0 then return true.
"""

class Solution:
    def canReach(self, arr, start: int) -> bool:
        if 0 not in arr:
            return False
        self.found = False
        seen = set()

        def jump(start_pos):
            if self.found or start_pos in seen:
                return
            seen.add(start_pos)
            if arr[start_pos] == 0:
                self.found = True
                return

            if start_pos + arr[start_pos] < len(arr):
                jump(start_pos + arr[start_pos])
            if start_pos - arr[start_pos] >= 0:
                jump(start_pos - arr[start_pos])

        jump(start)
        return self.found


# Test cases
s = Solution()

tests = [
    ([4,2,3,0,3,1,2], 5),
    ([4,2,3,0,3,1,2], 0),
    ([3,0,2,1,2], 2),
    ([4,2,3,3,1,2,4,2,3,3,1,2,4,2,3,3,1,2,4,2,3,3,1,2,4,2,3,3,1,2], 2)
]

for t in tests:
    print(s.canReach(*t))
