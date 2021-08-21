"""
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.
Return the minimum size of the set so that at least half of the integers of the array are removed.

Example 1:
    Input: arr = [3,3,3,3,5,5,5,2,2,7]
    Output: 2
    Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size
        of the old array).
        Possible sets of size 2 are {3,5},{3,2},{5,2}.
        Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than
        half of the size of the old array.

Example 2:
    Input: arr = [7,7,7,7,7,7]
    Output: 1
    Explanation: The only possible set you can choose is {7}. This will make the new array empty.

Example 3:
    Input: arr = [1,9]
    Output: 1

Example 4:
    Input: arr = [1000,1000,3,7]
    Output: 1

Example 5:
    Input: arr = [1,2,3,4,5,6,7,8,9,10]
    Output: 5

Constraints:
    1 <= arr.length <= 10^5
    arr.length is even.
    1 <= arr[i] <= 10^5

Hint #1
    Count the frequency of each integer in the array.
Hint #2
    Start with an empty set, add to the set the integer with the maximum frequency.
Hint #3
    Keep Adding the integer with the max frequency until you remove at least half of the integers.
"""
from typing import List
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        total = 0
        for i, val in enumerate(sorted(count.values(), reverse=True)):
            total += val
            if total >= len(arr) / 2:
                return i + 1




    # Testing above solution with radix sort
    def minSetSizeRadix(self, arr: List[int]) -> int:
        count = Counter(arr)

        def radix_sort(nums):
            max_num, min_num = max(nums), min(nums)
            max_exp = max(len(str(abs(max_num))), len(str(abs(min_num))))
            exp = 0
            while exp <= max_exp:
                buckets = [[] for _ in range(10)]
                for num in nums:
                    mod = num // 10 ** exp
                    if mod == 0:
                        buckets[0].append(num)
                    else:
                        buckets[mod % 10].append(num)
                if exp == max_exp:
                    # print(buckets)
                    return buckets[-1] + buckets[0]
                exp += 1
                nums = [n for li in buckets for n in li]

        total = 0
        values = radix_sort(count.values())
        for i, val in enumerate(values[::-1]):
            total += val
            if total >= len(arr) / 2:
                return i + 1
