"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
        Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 2 * 10^5
    s consists only of printable ASCII characters.
"""
from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = []
        s = s.lower()
        for c in s:
            if 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57:
                pal.append(c)

        pal = "".join(pal)
        return pal == pal[::-1]

if __name__ == "__main__":
    obj = Solution()
    tests = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "1p"

    ]

    for t in tests:
        print(t)
        print(obj.isPalindrome(t), end="\n\n")
