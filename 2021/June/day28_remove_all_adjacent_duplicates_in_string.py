"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent
and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:
    Input: s = "abbaca"
    Output: "ca"
    Explanation:
        For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only
        possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the
        final string is "ca".

Example 2:
    Input: s = "azxxzy"
    Output: "ay"

Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase English letters.

Hint #1
    Use a stack to process everything greedily.
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


if __name__ == "__main__":
    obj = Solution()
    tests = [
        "abbaca",
        "azxxzy",

    ]

    for t in tests:
        print(t)
        print(obj.removeDuplicates(t), end="\n\n")
