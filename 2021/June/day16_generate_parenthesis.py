"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
    Input: n = 1
    Output: ["()"]

Constraints:
    1 <= n <= 8
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(open=n, close=n, curr=""):
            if open == close == 0:
                return [curr]
            strings = []
            if open:
                strings.extend(dfs(open-1, close, curr+"("))
            if close > open:
                strings.extend(dfs(open, close-1, curr+")"))
            return strings

        return dfs()


if __name__ == "__main__":
    obj = Solution()
    tests = [
        3, 1, 8
    ]

    for t in tests:
        print(t)
        print(obj.generateParenthesis(t), end="\n\n")

