"""
Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following
procedure:
    - let x be the sum of all elements currently in your array.
    - choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
    - You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise return False.

Example 1:
    Input: target = [9,3,5]
    Output: true
    Explanation: Start with [1, 1, 1]
        [1, 1, 1], sum = 3 choose index 1
        [1, 3, 1], sum = 5 choose index 2
        [1, 3, 5], sum = 9 choose index 0
        [9, 3, 5] Done
Example 2:
    Input: target = [1,1,1,2]
    Output: false
    Explanation: Impossible to create target array from [1,1,1,1].
Example 3:
    Input: target = [8,5]
    Output: true

Constraints:
    N == target.length
    1 <= target.length <= 5 * 10^4
    1 <= target[i] <= 10^9
Hint #1
    Given that the sum is strictly increasing, the largest element in the target must be formed in the last step by
        adding the total sum in the previous step. Thus, we can simulate the process in a reversed way.
Hint #2
    Subtract the largest with the rest of the array, and put the new element into the array. Repeat until all elements
        become one.
"""
from typing import List
import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        x = sum(target)
        heap = [-i for i in target]
        heapq.heapify(heap)

        while heap[0] != -1:
            large = -heapq.heappop(heap)
            if (x - large) == 1:
                return True
            diff = large % (x - large) if (x - large) > 0 else 0
            if diff == 0 or diff == large:
                return False
            x = (x - large) + diff
            if diff == 1:
                heap.append(-1)
            else:
                heapq.heappush(heap, -diff)

        return True


# For testing

obj = Solution()

tests = [
[9,3,5],
[1,1,1,2],
[8,5],
[38, 75, 149, 1, 1, 1, 1, 1, 1, 1, 1185, 1, 1, 1, 1, 1, 297, 1, 1, 1, 1, 1, 1, 2369, 1, 1, 1, 1, 593, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[5057, 1, 1, 80, 1, 10113, 1, 1, 1, 20709377, 1, 1, 10354689, 80897, 1, 1, 1, 1, 1, 1, 1, 5177345, 1, 647169, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2529, 662700033, 1, 41418753, 1, 1, 1, 1, 1, 1, 1, 161793, 1, 1, 1, 633, 1, 1, 1, 1, 323585, 1, 1, 1, 1294337, 1, 1, 165675009, 1, 1, 1, 1, 1265, 331350017, 1, 317, 1, 82837505, 1, 1, 40449, 2588673, 159, 1, 1, 20225],
[5057, 1, 1, 80, 1, 10113, 1, 1, 1, 20709377, 1, 1, 10354689, 80897, 1, 1, 1, 1, 1, 1, 1, 5177345, 1, 647169, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2529, 662700033, 1, 41418753, 1, 1, 1, 1, 1, 1, 1, 161793, 1, 1, 1, 633, 1, 1, 1, 1, 323585, 1, 1, 1, 1294337, 1, 1, 165675009, 1, 1, 1, 1, 1265, 331350017, 1, 317, 1, 82837505, 1, 1, 40449, 2588673, 159, 1, 1, 20224],
[5057, 1, 1, 80, 1, 10113, 1, 1, 1, 20709377, 1, 1, 10354689, 80897, 1, 1, 1, 1, 1, 1, 1, 5177345, 1, 647169, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2529, 662700033, 1, 41418753, 1, 1, 1, 1, 1, 1, 1, 161793, 1, 1, 1, 633, 1, 1, 1, 1, 323585, 1, 1, 1, 1294337, 1, 1, 165675009, 1, 1, 1, 1, 1265, 331350017, 1, 317, 1, 82837505, 1, 1, 40449, 2588673, 159, 1, 1, 20226],
[5057, 1, 1, 80, 1, 10113, 1, 1, 1, 20709377, 1, 1, 10354689, 80897, 1, 1, 1, 1, 1, 1, 1, 5177345, 1, 647169, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2529, 662700033, 1, 41418753, 1, 1, 1, 1, 1, 1, 1, 161793, 1, 1, 1, 633, 1, 1, 1, 1, 323585, 1, 1, 1, 1294337, 1, 1, 165675009, 1, 1, 1, 1, 1265, 331350017, 1, 317, 1, 82837505, 1, 1, 40449, 2588673, 159, 1, 1, 20223],
[5057, 1, 1, 80, 1, 10113, 1, 1, 1, 20709377, 1, 1, 10354689, 80897, 1, 1, 1, 1, 1, 1, 1, 5177345, 1, 647169, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2529, 662700033, 1, 41418753, 1, 1, 1, 1, 1, 1, 1, 161793, 1, 1, 1, 633, 1, 1, 1, 1, 323585, 1, 1, 1, 1294337, 1, 1, 165675009, 1, 1, 1, 1, 1265, 331350017, 1, 317, 1, 82837505, 1, 1, 40449, 2588673, 159, 1, 1, 20227],
[5, 417, 2834, 225, 1],
[1,1000000000],
[175465, 1, 25615, 694387, 1, 2732725, 109, 347617, 1388773, 87950],
[2,900000001],
[8,5],
[2]


]

for t in tests:
    print(t)
    # print(obj.isPossible(t), end="\n\n")



# import random
# def generate_multiple_sums_list(length=10, times_to_shuffle=20):
#     li = [1] * length
#     s = len(li)
#     for _ in range(times_to_shuffle):
#         i = random.randint(0, len(li) - 1)
#         old = li[i]
#         li[i] = s
#         s = s + (s - old)
#         if s > 10 ** 9:
#             break
#
#     random.shuffle(li)
#     return li
#
# print(generate_multiple_sums_list())
