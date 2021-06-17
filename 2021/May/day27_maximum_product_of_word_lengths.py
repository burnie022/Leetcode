"""
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not
share common letters. If no such two words exist, return 0.

Example 1:
    Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    Output: 16
    Explanation: The two words can be "abcw", "xtfn".
Example 2:
    Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
    Output: 4
    Explanation: The two words can be "ab", "cd".
Example 3:
    Input: words = ["a","aa","aaa","aaaa"]
    Output: 0
    Explanation: No such pair of words.

Constraints:
    2 <= words.length <= 1000
    1 <= words[i].length <= 1000
    words[i] consists only of lowercase English letters.
"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_product = 0
        lengths = []
        char_dict = {}

        for i in range(len(words)):
            lengths.append(len(words[i]))
            for char in words[i]:
                if char not in char_dict:
                    char_dict[char] = set()
                char_dict[char].add(i)

        for i in range(len(words)):
            other_words = set(i for i in range(len(words)))
            for char in words[i]:
                other_words.difference_update(char_dict[char])
            if other_words:
                max_product = max(max_product, lengths[i] * max(lengths[j] for j in other_words))

        return max_product





# Test cases
obj = Solution()

tests = [
["abcw","baz","foo","bar","xtfn","abcdef"],
["a","ab","abc","d","cd","bcd","abcd"],
["a","aa","aaa","aaaa"],
]

for t in tests:
    print(t)
    print(obj.maxProduct(t), end="\n\n")

