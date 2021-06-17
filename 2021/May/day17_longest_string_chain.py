"""
Given a list of words, each word consists of English lowercase letters.
Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it
equal to word2. For example, "abc" is a predecessor of "abac".
A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of
word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

Example 1:
    Input: words = ["a","b","ba","bca","bda","bdca"]
    Output: 4
    Explanation: One of the longest word chain is "a","ba","bda","bdca".
Example 2:
    Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
    Output: 5

Constraints:
    1 <= words.length <= 1000
    1 <= words[i].length <= 16
    words[i] only consists of English lowercase letters.
Hint #1
    Instead of adding a character, try deleting a character to form a chain in reverse.
Hint #2
    For each word in order of length, for each word2 which is word with one character removed,
        length[word2] = max(length[word2], length[word] + 1).
"""
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        dp_chain_lengths = {words[0]: 1}
        max_length = 1

        for word in words[1:]:
            dp_chain_lengths[word] = 1
            for i in range(len(word)):
                word1 = word[:i]+word[i+1:]
                if word1 in dp_chain_lengths:
                    dp_chain_lengths[word] = max(dp_chain_lengths[word], dp_chain_lengths[word1] + 1)
                    max_length = max(max_length, dp_chain_lengths[word])

        return max_length



# My original solution. Good solution too but a bit slower.
class Solution2:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda w: len(w))
        chain_lengths = [1] * len(words)
        word_lengths = [len(w) for w in words]

        for j in range(1, len(words)):
            diff = word_lengths[j] - 1
            for i in reversed(range(j)):
                if word_lengths[i] == diff and chain_lengths[i] >= chain_lengths[j]:
                    if self.is_predecessor(words[i], words[j]):
                        chain_lengths[j] = chain_lengths[i] + 1

        return max(chain_lengths)

    def is_predecessor(self, word1, word2) -> bool:
        for i in range(len(word1)):
            if word2[i] != word1[i]:
                return word1 == word2[:i] + word2[i+1:]
        return word1 == word2[:len(word2)-1]



# Test cases
obj = Solution()

tests = [
["a","b","ba","bca","bda","bdca"],
["xbc","pcxbcf","xb","cxbc","pcxbc"],
["a"]
]

for t in tests:
    # print(obj.is_predecessor(t[4], t[1]))
    print(obj.longestStrChain(t))
