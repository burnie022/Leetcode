"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
    Input: strs = [""]
    Output: [[""]]
Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

Constraints:
    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] consists of lower-case English letters.
"""
from typing import List


class Solution:
    # Optimal solution
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            seen.setdefault(tuple(sorted(word)), []).append(word)

        return seen.values()


    def groupAnagramsSol2(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        anagrams = []
        i = 0

        for word in strs:
            s_word = "".join(sorted(word))
            if s_word not in seen:
                seen[s_word] = i
                anagrams.append([])
                i += 1
            anagrams[seen[s_word]].append(word)

        return anagrams

    def groupAnagramsSol3(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        anagrams = []
        i = 0

        for word in strs:
            char_count = [0] * 26
            for c in word:
                char_count[ord(c) - 97] += 1
            char_count = tuple(char_count)
            if char_count not in seen:
                seen[char_count] = i
                anagrams.append([])
                i += 1
            anagrams[seen[char_count]].append(word)

        return anagrams


if __name__ == "__main__":
    obj = Solution()
    tests = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["eat", "tea", "tan", "ate", "nat", "bat", "", ""],
        ["eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat"],
        ["eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat"],

    ]

    for t in tests:
        print(t)
        print(obj.groupAnagramsSol2(t), end="\n\n")
