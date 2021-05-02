"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
The answer is guaranteed to fit in a 32-bit integer.

Example 1:
    Input: s = "12"
    Output: 2
    Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:
    Input: s = "226"
    Output: 3
    Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:
    Input: s = "0"
    Output: 0
    Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore
    a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.
Example 4:
    Input: s = "1"
    Output: 1

Constraints:
    1 <= s.length <= 100
    s contains only digits and may contain leading zero(s).
"""


def numDecodings(s: str) -> int:
    if s[0] == "0":
        return 0
    twenty = {"0", "1", "2", "3", "4", "5", "6"}
    memo = {}

    def dfs(s):
        if not s:
            return 1
        if s[0] == "0":
            return 0
        if s in memo:
            return memo[s]
        total = 0
        if len(s) >= 1:
            total = dfs(s[1:])
        if len(s) >= 2:
            if s[0] == "1" or (s[0] == "2" and s[1] in twenty):
                total += dfs(s[2:])

        memo[s] = total
        return total

    return dfs(s)


# Test cases

tests = [
    "12",
    "0",
    "0126",
    "10260",
    "12321",
    "555555",
    "155555",
    "151555",
    "151515",
    "1515151515",
    "15151515",
    "15101151",
    "11111111",
    "20134625981720265817111171910202112321112515",
    "2013462598172026581711117191020211232111251500",
    "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
]

for t in tests:
    print(t)
    print(numDecodings(t), end="\n\n")

# for _ in range(100):
#     print(1, end="")
