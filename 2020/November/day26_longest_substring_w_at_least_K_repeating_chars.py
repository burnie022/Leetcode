"""
Given a string s and an integer k, return the length of the longest substring of s such that the
frequency of each character in this substring is greater than or equal to k.

Example 1:
    Input: s = "aaabb", k = 3
    Output: 3
    Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:
    Input: s = "ababbc", k = 2
    Output: 5
    Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated
        3 times.

Constraints:
    1 <= s.length <= 104
    s consists of only lowercase English letters.
    1 <= k <= 105
"""
from collections import Counter


def longestSubstring(s: str, k: int) -> int:
    if len(s) < k:
        return 0
    count = Counter(s)
    for i in range(len(s)):
        if count[s[i]] < k:
            return max(longestSubstring(s[:i], k), longestSubstring(s[i + 1:], k))

    return len(s)


# Test cases

tests = [
    ("aaabb", 3),
    ("aaabb", 2),
    ("ababbc", 2),
    ("ababbc", 1),
    ("ababbc", 6),
    ("ababbc", 7),
    ("aaabbb", 3),
    ("aaabbb", 2),
    ("aabccddaddccefa", 4),
    ("aabccddaddccefa", 3),
    ("aaabbbcdefcdefcde", 3),
    ("aaabbbcdefcdefgggggggggggggggcde", 3)
]

for s, k in tests:
    print(longestSubstring(s, k))
