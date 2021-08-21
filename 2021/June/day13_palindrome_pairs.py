"""
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the
concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:
    Input: words = ["abcd","dcba","lls","s","sssll"]
    Output: [[0,1],[1,0],[3,2],[2,4]]
    Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:
    Input: words = ["bat","tab","cat"]
    Output: [[0,1],[1,0]]
    Explanation: The palindromes are ["battab","tabbat"]
Example 3:
    Input: words = ["a",""]
    Output: [[0,1],[1,0]]

Constraints:
    1 <= words.length <= 5000
    0 <= words[i].length <= 300
    words[i] consists of lower-case English letters.
"""
from typing import List



class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pairs = []
        dict_words = {}
        if "" in words:
            i = words.index("")
            for j in range(len(words)):
                if j != i:
                    pairs.append([i, j])
                    pairs.append([j, i])

        for i in range(len(words)):
            if words[i] == "":
                continue
            dict_words[words[i]] = dict_words.get(words[i], []) + [i]
            if len(words[i]) > 2 and words[i][0] == words[i][1]:
                dict_words[words[i][2:]] = dict_words.get(words[i][2:], []) + [i]

        for i in range(len(words)):
            if words[i] == "":
                continue
            if words[i][::-1] in dict_words:
                for j in dict_words[words[i][::-1]]:
                    if j != i:
                        pairs.append([i, j])

            elif len(words[i]) > 2 and words[i][len(words[i])-1] == words[i][len(words[i])-2]:
                w = words[i][len(words[i])-2][::-1]
                if w in dict_words:
                    for j in dict_words[w]:
                        if j != i:
                            pairs.append([i, j])

        return pairs gb

    # A leetcoder's solution
    def palindromePairsLC(self, words):
        dict_words = {word: i for i, word in enumerate(words)}
        pairs = set()
        is_palindrome = lambda s: s == s[::-1] if s else True

        for i, word in enumerate(words):
            if word and is_palindrome(word) and "" in dict_words:
                j = dict_words[""]
                pairs.add((i, j))
                pairs.add((j, i))

            bw = word[::-1]
            if word and bw in dict_words:
                j = dict_words[bw]
                if i != j:
                    pairs.add((i, j))
                    pairs.add((j, i))
            for j in range(1, len(word)):
                left, right = word[:j], word[j:]
                if is_palindrome(left) and right[::-1] in dict_words:
                    pairs.add((dict_words[right[::-1]], i))
                if is_palindrome(right) and left[::-1] in dict_words:
                    pairs.add((i, dict_words[left[::-1]]))

        return list(pairs)



if __name__ == "__main__":
    obj = Solution()
    tests = [
        ["abcd", "dcba", "lls", "s", "sssll"],
        ["bat", "tab", "cat"],
        ["a", ""],
        ["a", "", "b"],
        ["a", "", "b", "c"],

    ]

    for t in tests:
        s = "\",\"".join(t)
        print(f"[\"{s}\"]")

        print(obj.palindromePairsLC(t), end="\n\n")

    # t = ["a", "b"]
    # dt = {val: key for key, val in enumerate(t)}
    # print(dt)



