"""
You are given an array of integers nums, there is a sliding window of size k which is moving from
the very left of the array to the very right. You can only see the k numbers in the window. Each
time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Explanation:
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7
Example 2:
    Input: nums = [1], k = 1
    Output: [1]
Example 3:
    Input: nums = [1,-1], k = 1
    Output: [1,-1]
Example 4:
    Input: nums = [9,11], k = 2
    Output: [11]
Example 5:
    Input: nums = [4,-2], k = 2
    Output: [4]

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    1 <= k <= nums.length
Hint #1
How about using a data structure such as deque (double-ended queue)?
Hint #2
The queue size need not be the same as the window’s size.
Hint #3
Remove redundant elements and the queue should store only elements that need to be considered.
"""

# inefficient with huge nums and k
def maxSlidingWindow2(nums, k: int):
    if len(nums) == k:
        return [max(nums)]
    if k == 1:
        return nums
    curr_max = max(nums[:k])
    window_max = [curr_max]
    front, back = k + 1, 1
    while front <= len(nums):
        if nums[back - 1] == curr_max:
            if curr_max != nums[front - 1]:
                curr_max = max(nums[back: front])
        else:
            curr_max = max(curr_max, nums[front - 1])
        window_max.append(curr_max)
        front += 1
        back += 1

    return window_max


# More efficient method using deque
# deq max space efficiency is O(k)

from collections import deque

def maxSlidingWindow(nums, k: int):
    if len(nums) == k:
        return [max(nums)]
    if k == 1:
        return nums
    deq = deque([])
    window_max = []

    for i, n in enumerate(nums):
        if not deq:
            deq.append(i)
        else:
            while deq:
                if nums[deq[-1]] <= n:
                    deq.pop()
                else:
                    break
            deq.append(i)

        if i - k == deq[0]:
            deq.popleft()

        if i >= k - 1:
            window_max.append(nums[deq[0]])

    return window_max



# Test cases

tests = [
    ([1,3,-1,-3,5,3,6,7], 3),
    ([1], 1),
    ([1,-1], 1),
    ([9,11], 2),
    ([4,-2], 2),
    ([6,5,7,3,2,3,6,9], 8),
    ([6,5,7,3,2,3,6,9], 1),
    ([-8,-10,-9,-7,-9,-10,-6,-2,-4], 5),
    ([-8,-10,-9,-7,-9,-10,-6,-2,-4], 3),
    ([-8,-10,-9,-7,-9,-10,-6,-2,-4], 7)

]

for t, p in tests:
    print(t)
    print(p)

for t in tests:
    print(maxSlidingWindow(*t))
