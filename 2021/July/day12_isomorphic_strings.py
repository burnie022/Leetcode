"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No
two characters may map to the same character, but a character may map to itself.

Example 1:
    Input: s = "egg", t = "add"
    Output: true
Example 2:
    Input: s = "foo", t = "bar"
    Output: false
Example 3:
    Input: s = "paper", t = "title"
    Output: true

Constraints:
    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        seen = set()

        for i, ch in enumerate(t):
            if ch in char_map or s[i] in seen:
                if char_map.get(ch) != s[i]:
                    return False
            else:
                char_map[ch] = s[i]
                seen.add(s[i])

        return True


if __name__ == "__main__":
    obj = Solution()
    tests = [
        ("egg", "add"),
        ("foo", "bar"),
        ("paper", "title"),
        ("13", "42"),
        ("{}", "}{"),
    ]

    for t in tests:
        print(f"\"{t[0]}\"")
        print(f"\"{t[1]}\"")
        print(obj.isIsomorphic(*t), end="\n\n")
        # print(obj.isIsomorphic(t[1], t[0]), end="\n\n")
