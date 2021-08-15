"""
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number
of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

Example 1:
    Input: s = "00110"
    Output: 1
    Explanation: We flip the last digit to get 00111.
Example 2:
    Input: s = "010110"
    Output: 2
    Explanation: We flip to get 011111, or alternatively 000111.
Example 3:
    Input: s = "00011000"
    Output: 2
    Explanation: We flip to get 00000000.

Constraints:
    1 <= s.length <= 105
    s[i] is either '0' or '1'.
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeroes = s.count("0")
        if zeroes == len(s) or zeroes == 0:
            return 0

        flips = zeroes
        for i in range(len(s)):
            zeroes += -1 if s[i] == "0" else 1
            flips = min(flips, zeroes)

        return flips




if __name__ == "__main__":
    obj = Solution()
    tests = [
        "00110", "010110", "00011000",
        "0001100011111110000000011100000111111111",
        "11111111110111111111111",
        "0000000100000000",
        "0",
        "1",
        "11111",
        "000000",
    ]

    for t in tests:
        print(f"\"{t}\"")
        print(obj.minFlipsMonoIncr(t), end="\n\n")
