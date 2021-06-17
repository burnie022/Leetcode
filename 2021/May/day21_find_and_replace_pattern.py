"""
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the
answer in any order.
A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the
pattern with p(x), we get the desired word.
Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and
no two letters map to the same letter.

Example 1:
    Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
    Output: ["mee","aqq"]
    Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
        "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the
        same letter.
Example 2:
    Input: words = ["a","b","c"], pattern = "a"
    Output: ["a","b","c"]

Constraints:
    1 <= pattern.length <= 20
    1 <= words.length <= 50
    words[i].length == pattern.length
    pattern and words[i] are lowercase English letters.
"""
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def pattern_match(pattern_to_match, word):
            letter_map = {}
            used = set()
            for i in range(len(pattern_to_match)):
                if pattern_to_match[i] in letter_map:
                    if letter_map[pattern_to_match[i]] != word[i]:
                        return False
                else:
                    if word[i] in used:
                        return False
                    letter_map[pattern_to_match[i]] = word[i]
                    used.add(word[i])
            return True

        matches = []
        for word in words:
            if pattern_match(pattern, word):
                matches.append(word)

        return matches




# Test cases
obj = Solution()
tests = [
    (["abc","deq","mee","aqq","dkd","ccc"], "abb"),
    (["a","b","c"], "a"),
    (["abcd","deeq","meen","aqaq","dkdd","ccce","eccc"], "abbc"),
    (["abcd","deeq","meen","aqaq","dkdd","ccce","eccc"], "abcd"),
    (["ef","fq","ao","at","lx"], "ya")
]

for w, p in tests:
    print(w)
    print(f"\"{p}\"")
    print(obj.findAndReplacePattern(w, p), end="\n\n")

