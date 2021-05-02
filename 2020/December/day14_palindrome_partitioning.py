"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all
possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""
from typing import List

# No good, try again


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        self.result = []

        def is_pal(pal):
            return pal == pal[::-1]

        def dfs(s_part, curr_string, curr_list):
            if not s_part:
                return
            for i in range(len(s_part)):
                if is_pal(curr_string + s_part[i]):
                    curr_list.append(curr_string + s_part[i])
                    dfs(s_part[i:], curr_string + s_part[:i + 1], s_part[i + 1:])
            self.result.append(curr_list)

        dfs(s, "", [])
        # for i, c in enumerate(s):
        #     self.result.append([c] + dfs(s[i:]))








        return self.result if self.result else [[]]



# A leetcode solution

    def partitionLeetcode(self, s: str) -> List[List[str]]:

        def dfs(s, path, result):
            if not s:
                result.append(path[:])
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[i-1::-1]:
                    path.append(s[:i])
                    dfs(s[i:], path, result)
                    path.pop()

        result = []
        dfs(s, [], result)

        return result


# Test cases
s = Solution()

tests = [
"aab"
# "aaab",
# "aaaaaba"
]

for t in tests:
    print(s.partition(t))
