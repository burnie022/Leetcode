"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the
order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4

Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1

Constraints:
    1 <= nums.length <= 2500
    -10^4 <= nums[i] <= 10^4

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
from typing import List
from bisect import bisect_left


class Solution:

# This solution inspired by Leetcode's official solution. Worst case runtime is O(nlogn) as it may perform a binary
# search for every number in nums, however, runtime for long lists is significantly faster than my DP solution below.

# A more detailed explanation of this func from leetcode's official solution is included at the bottom of this module.

    def lengthOfLIS(self, nums: List[int]) -> int:
        subarray = [nums[0]]
        for n in nums[1:]:
            if n < subarray[-1]:
                i = bisect_left(subarray, n)
                subarray[i] = n
            elif n > subarray[-1]:
                subarray.append(n)

        return len(subarray)


# My original solution uses DP. Works just fine but O(n^2) runtime, much slower than the above solution for long lists
    def lengthOfLIS_DP(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)- 1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i]+1)

        return max(dp)


if __name__ == "__main__":
    obj = Solution()
    tests = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7, 7, 7, 7],
        [0, 3, 1, 6, 2, 2, 7],
        [5],
    ]

    for t in tests:
        print(t)
        print(obj.lengthOfLIS(t), end="\n\n")


"""
Approach 2: Intelligently Build a Subsequence
Intuition

As stated in the previous approach, the difficult part of this problem is deciding if an element is worth using or 
not. Consider the example nums = [8, 1, 6, 2, 3, 10]. Let's try to build an increasing subsequence starting with an 
empty one: sub = [].

    - At the first element 8, we might as well take it since it's better than nothing, so sub = [8].

    - At the second element 1, we can't increase the length of the subsequence since 8 >= 1, so we have to choose only
        one element to keep. Well, this is an easy decision, let's take the 1 since there may be elements later on 
        that are greater than 1 but less than 8, now we have sub = [1].

    - At the third element 6, we can build on our subsequence since 6 > 1, now sub = [1, 6].

    - At the fourth element 2, we can't build on our subsequence since 6 >= 2, but can we improve on it for the 
        future? Well, similar to the decision we made at the second element, if we replace the 6 with 2, we will open 
        the door to using elements that are greater than 2 but less than 6 in the future, so sub = [1, 2].

    - At the fifth element 3, we can build on our subsequence since 3 > 2. Notice that this was only possible because 
        of the swap we made in the previous step, so sub = [1, 2, 3].

    - At the last element 10, we can build on our subsequence since 10 > 3, giving a final subsequence 
        sub = [1, 2, 3, 10]. The length of sub is our answer.

It appears the best way to build an increasing subsequence is: for each element num, if num is greater than the
largest element in our subsequence, then add it to the subsequence. Otherwise, perform a linear scan through the 
subsequence starting from the smallest element and replace the first element that is greater than or equal to num 
with num. This opens the door for elements that are greater than num but less than the element replaced to be 
included in the sequence.

One thing to add: this algorithm does not always generate a valid subsequence of the input, but the length of the 
subsequence will always equal the length of the longest increasing subsequence. For example, with the input 
[3, 4, 5, 1], at the end we will have sub = [1, 4, 5], which isn't a subsequence, but the length is still correct. 
The length remains correct because the length only changes when a new element is larger than any element in the 
subsequence. In that case, the element is appended to the subsequence instead of replacing an existing element.

Algorithm

    1. Initialize an array sub which contains the first element of nums.

    2. Iterate through the input, starting from the second element. For each element num:
     - If num is greater than any element in sub, then add num to sub.
     - Otherwise, iterate through sub and find the first element that is greater than or equal to num. Replace that
        element with num.
    3. Return the length of sub.

Implementation

    class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # Find the first element in sub that is greater than or equal to num
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num

        return len(sub)

Complexity Analysis

Given N as the length of nums,

    * Time complexity: O(N^2).

        This algorithm will have a runtime of O(N^2) only in the worst case. Consider an input where the first half is
        [1, 2, 3, 4, ..., 99998, 99999], then the second half is [99998, 99998, 99998, ..., 99998, 99998]. We would 
        need to iterate (N / 2)^2 times for the second half because there are N / 2 elements equal to 99998, and a 
        linear scan for each one takes N / 2 iterations. This gives a time complexity of O(N^2).
        2
         ).

    Despite having the same time complexity as the previous (DP) approach, in the best and average cases, it is much
    more efficient.

    * Space complexity: O(N).

        When the input is strictly increasing, the sub array will be the same size as the input.
        
        
Approach 3: Improve With Binary Search
Intuition

In the previous approach, when we have an element num that is not greater than all the elements in sub, we perform a
linear scan to find the first element in sub that is greater than or equal to num. Since sub is in sorted order, we
can use binary search instead to greatly improve the efficiency of our algorithm.

Algorithm

    1. Initialize an array sub which contains the first element of nums.
    
    2. Iterate through the input, starting from the second element. For each element num:
        - If num is greater than any element in sub, then add num to sub.
        - Otherwise, perform a binary search in sub to find the smallest element that is greater than or equal to num.
            Replace that element with num.
            
    3. Return the length of sub.

Implementation

In Python, the bisect module provides super handy functions that does binary search for us.

    class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)  
        
Complexity Analysis

Given N as the length of nums,

    * Time complexity: O(N⋅log(N)).
    
        Binary search uses log(N) time as opposed to the O(N) time of a linear scan, which improves our time 
            complexity from O(N^2) to O(N⋅log(N)).
    
    * Space complexity: O(N).
    
        When the input is strictly increasing, the sub array will be the same size as the input.
"""
