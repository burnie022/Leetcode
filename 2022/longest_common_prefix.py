"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:
            i, longest = 0, len(prefix)
            for c in word[:longest]:
                if c != prefix[i]:
                    break
                i += 1
            prefix = word[:i]
            if prefix == "":
                return ""

        return prefix






if __name__ == "__main__":
    obj = Solution()
    tests = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["carriage", "racecar", "car"],
        ["carriage"],
        ["flower", "flow"],
        ["flow", "flower"],
        ["flow", "flower", ""],
        ["", "flow", "flower"],
        ["ape", "apple", "apricot", "ankle"],
        ["ankle", "ape", "apple", "apricot"],
        ["ape", "apple", "apricot"],
        ["ape", "apple", "apricot", "blank"],
        [""],
        ["", ""],
        ["a", "", ""],
        ["", "a", "", ""],
    ]

    for t in tests:
        print(t)
        print(obj.longestCommonPrefix(t), end="\n\n")
