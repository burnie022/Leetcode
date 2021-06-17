"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

Constraints:
    0 <= nums.length <= 10^5
    -109 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    # this solution based on Leetcode's official solution
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        streak = max_streak = 1

        for num in nums:
            if num - 1 not in num_set:
                n = num
                while n + 1 in num_set:
                    streak += 1
                    n += 1
                max_streak = max(max_streak, streak)
                streak = 1

        return max_streak if len(nums) >= 2 else len(nums)

    # Radix Sort solution: My radix sort function will sort lists of all counting nums including negatives and 0
    def longestConsecutiveRadix(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        def radix_sort(nums):
            buckets = [[] for _ in range(10)]
            negative_buckets = [[] for _ in range(10)]
            max_num = nums[0]
            min_num = nums[0]
            exp, zeroes = 1, 0

            for num in nums:
                if num == 0:
                    zeroes += 1
                elif num < 0:
                    negative_buckets[-num % 10].append(-num)
                    min_num = min(min_num, num)
                else:
                    buckets[num % 10].append(num)
                    max_num = max(max_num, num)

            nums = [n for li in buckets for n in li]
            negative_nums = [n for li in negative_buckets for n in li]
            min_num = -min_num

            while max_num // 10 ** exp > 0:
                buckets = [[] for _ in range(10)]
                for num in nums:
                    if num // 10 ** exp == 0:
                        buckets[0].append(num)
                    else:
                        buckets[(num // 10 ** exp) % 10].append(num)
                exp += 1
                nums = [n for li in buckets for n in li]

            exp = 1
            while min_num // 10 ** exp > 0:
                negative_buckets = [[] for _ in range(10)]
                for num in negative_nums:
                    if num // 10 ** exp == 0:
                        negative_buckets[0].append(num)
                    else:
                        negative_buckets[(num // 10 ** exp) % 10].append(num)
                exp += 1
                negative_nums = [n for li in negative_buckets for n in li]

            return [-n for n in negative_nums][::-1] + [0] * zeroes + nums

        longest_seq = curr = 1
        nums = radix_sort(nums)

        last = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == last:
                continue
            elif last + 1 == nums[i]:
                curr += 1
            else:
                longest_seq = max(longest_seq, curr)
                curr = 1
            last = nums[i]

        return max(longest_seq, curr)


# Test cases
obj = Solution()
tests = [
[100,4,200,1,3,2],
[1],
[2,4],
[1, 2],
[],
[100,4,200,1,3,2],
[0,3,7,2,5,8,4,6,0,1],
[0, 1, -1, 2, -2, 0, 111, -113, 110, -101, 3, -3, 5, -5, -4, 4, 0, -2, 1,13, -12],
]

for t in tests:
    print(t)
    # print(obj.longestConsecutive(t), end="\n\n")


# t = [0, 1, -1, 2, -2, 0, 111, -113, 110, -101, 3, -3, 5, -5, -4, 4, 0, -2, 1,13, -12]
# t2 = [5,4,3,2,1]
# t3 = [0, 0, 0, 0]
# t4 = [-1, -2, -3, -6, -5]
# t5 = [1]
# t6 = [0]
# t7 = [-20345, 0, -1200000, 8690]
# t8 = []
# print(radix_sort(t8))
#
# print([0] * 2)

# print(120 // 100)