"""
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the
array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:
    Input: nums = [3,6,9,1]
    Output: 3
    Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:
    Input: nums = [10]
    Output: 0
    Explanation: The array contains less than 2 elements, therefore return 0.

Constraints:
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 10^9
"""
from typing import List


# Radix Sort method
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        sorted_places = {str(n): [] for n in range(10)}
        max_length = 0
        for num in nums:
            s = str(num)
            max_length = max(max_length, len(s))
            sorted_places[s[-1]].append(s)
        new_nums = []
        for i in range(10):
            if sorted_places[str(i)] != []:
                new_nums.extend(sorted_places[str(i)])

        for i in range(2, max_length+1):
            sorted_places = {str(n): [] for n in range(10)}
            for n in new_nums:
                if i > len(n):
                    sorted_places["0"].append(n)
                else:
                    sorted_places[n[-i]].append(n)
            new_nums.clear()
            for i in range(10):
                if sorted_places[str(i)] != []:
                    new_nums.extend(sorted_places[str(i)])


        for i in range(len(nums)):
            new_nums[i] = int(new_nums[i])

        return max(new_nums[i] - new_nums[i-1] for i in range(1, len(nums)))


# Test cases
obj = Solution()
tests = [
[3,6,9,1],
[10],
    [1,3,15,33,81,90,40,32,31,24,2,8,70,77],
    [1, 3, 15, 33, 81, 12,5,9,22,11,45,56,63,71,86,90, 40, 32, 31, 24, 2, 8, 70, 77],
    [1, 3, 111,100,99,105,94,15, 33, 81, 12, 5, 9, 22, 11, 45, 56, 63, 71, 86, 90, 40, 32, 31, 24, 2, 8, 70, 77],

]

for t in tests:
    print(t)
    print(obj.maximumGap(t), end="\n\n")


# from random import randint
# def gen_test(length, max_num):
#     li = []
#     for i in range(length):
#         li.append(randint(0,max_num))
#     print(li)
# gen_test(10000, 150000000)




