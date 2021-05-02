"""
Given a string s, the power of the string is the maximum length of a non-empty substring
that contains only one unique character.
Return the power of the string.

Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:
Input: s = "triplepillooooow"
Output: 5

Example 4:
Input: s = "hooraaaaaaaaaaay"
Output: 11

Example 5:
Input: s = "tourist"
Output: 1

Constraints:
    1 <= s.length <= 500
    s contains only lowercase English letters.
Hint #1
Keep an array power where power[i] is the maximum power of the i-th character.
Hint #2
The answer is max(power[i]).
"""

def maxPower(s: str) -> int:
    counts = {}
    max_count = -1
    last = None
    count = 0

    for c in s:
        if not last:
            last = c
            count += 1
            continue

        if c != last:
            counts[last] = max(counts.get(last, 0), count)
            max_count = max(max_count, count)
            last = c
            count = 0

        count += 1

    max_count = max(max_count, count)

    return max_count

# Test cases

tests = ["leetcode",
"abbcccddddeeeeedcba",
"triplepillooooow",
"hooraaaaaaaaaaay",
"tourist"
]

for t in tests:
    print(maxPower(t))

