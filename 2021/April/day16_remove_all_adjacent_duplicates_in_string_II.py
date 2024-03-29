"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent
and equal letters from s and removing them, causing the left and the right side of the deleted
substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It is guaranteed that
the answer is unique.

Example 1:
    Input: s = "abcd", k = 2
    Output: "abcd"
    Explanation: There's nothing to delete.
Example 2:
    Input: s = "deeedbbcccbdaa", k = 3
    Output: "aa"
    Explanation:
    First delete "eee" and "ccc", get "ddbbbdaa"
    Then delete "bbb", get "dddaa"
    Finally delete "ddd", get "aa"
Example 3:
    Input: s = "pbbcggttciiippooaais", k = 2
    Output: "ps"

Constraints:
    1 <= s.length <= 105
    2 <= k <= 104
    s only contains lower case English letters.
Hint #1
    Use a stack to store the characters, when there are k same characters, delete them.
Hint #2
    To make it more efficient, use a pair to store the value and the count of each character.
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack, count, result = [s[0]], [1], [s[0]]

        for c in s[1:]:
            if stack and c == stack[-1]:
                count[-1] += 1
            else:
                stack.append(c)
                count.append(1)

            result.append(c)
            if count[-1] == k:
                stack.pop()
                count.pop()
                for i in range(k):
                    result.pop()

        return "".join(result)


# Test cases

tests = [
    ("abcd", 2),
    ("deeedbbcccbdaa", 3),
    ("pbbcggttciiippooaais", 2),
    ("aabaa", 4)
]

obj = Solution()

for s, k in tests:
    # print(f"\"{s}\"\n{k}")
    print(obj.removeDuplicates(s, k))

